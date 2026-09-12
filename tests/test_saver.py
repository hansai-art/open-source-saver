"""Synthetic fixtures only; no real installed-app lists or network calls."""
import contextlib
import io
import json
import os
import plistlib
import stat
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import saver
import collect_macos


class SaverTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = saver.read_json(saver.ROOT / 'data/products.json')
        cls.products = cls.catalog['products']
        cls.mappings = saver.read_json(saver.ROOT / 'data/alternatives.json')['mappings']

    def test_catalog_integrity(self):
        saver.validate(self.catalog, self.mappings)

    def test_duplicate_names_and_urls_rejected(self):
        original = self.products[0]
        for duplicate in [dict(original, id='test-duplicate'),
                          dict(original, id='test-duplicate', name='Different name')]:
            with self.assertRaises(ValueError):
                saver.validate({'products': [original, duplicate]}, [])

    def test_bilingual_use_and_evidence_cannot_be_empty(self):
        for changed in [dict(self.products[0], sources=[]),
                        dict(self.products[0], zh={'use': '用途', 'limits': ''})]:
            with self.assertRaises(ValueError):
                saver.validate({'products': [changed]}, [])

    def test_upstream_discovery_stays_separate_and_translates_keywords(self):
        entries = [dict(id='lead-1', name='Example Wiki', aliases=[], tags=['Wikis']),
                   dict(id='lead-2', name='Example CRM', aliases=[], tags=['CRM'])]
        with mock.patch.object(saver, 'read_json', return_value={'知識庫': ['wiki']}), \
             mock.patch.object(Path, 'exists', return_value=True):
            results, total = saver.discover(entries, '知識庫', 1)
        self.assertEqual([e['id'] for e in results], ['lead-1'])
        self.assertEqual(total, 1)
        self.assertEqual(saver.discover(entries, 'not-present'), ([], 0))

    def test_web_services_do_not_masquerade_as_mac_installers(self):
        service = dict(self.products[0], platforms=['web'], delivery='self-hosted')
        self.assertEqual(saver.search([service], [], '', platform='macos'), [])
        self.assertEqual(saver.search([service], [], '', platform='web'), [service])

    def test_exact_aliases_and_years_do_not_match_other_products(self):
        self.assertIsNotNone(saver.source_match('Adobe Premiere Pro 2024', self.mappings))
        self.assertIsNone(saver.source_match('Adobe Premiere Pro Helper', self.mappings))
        self.assertIsNone(saver.source_match('WordPress', self.mappings))
        self.assertIsNone(saver.source_match('Not Word', self.mappings))

    def test_screen_studio_platform_and_engine_filter(self):
        results = saver.search(self.products, self.mappings, 'Screen Studio', 'macos')
        self.assertTrue(results)
        self.assertTrue(all('macos' in p['platforms'] for p in results))
        self.assertTrue(all(p['delivery'] != 'engine' for p in results))
        windows = saver.search(self.products, self.mappings, 'Screen Studio', 'windows')
        self.assertTrue(all('windows' in p['platforms'] for p in windows))
        self.assertNotIn('Apple Dictation', [p['name'] for p in saver.search(self.products, self.mappings, 'dictation', 'windows')])

    def test_engine_opt_in_and_unknown_platform(self):
        engine = dict(self.products[0], delivery='engine', platforms=[])
        self.assertEqual(saver.search([engine], [], ''), [])
        self.assertEqual(saver.search([engine], [], '', include_engines=True), [engine])
        self.assertEqual(saver.search([engine], [], '', 'macos', True), [])

    def test_chinese_bom_input_and_deduplication(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'apps.txt'
            p.write_text('範例軟體\nWord\n word \n\n', encoding='utf-8-sig')
            self.assertEqual(saver.inventory(p), (['範例軟體', 'Word'], False))

    def test_json_envelope_discards_private_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'apps.json'
            p.write_text(json.dumps({'applications': [{'display_name': 'Word', 'path': '/private/secret'}], 'warnings': ['PRIVATE_WARNING']}))
            names, warnings = saver.inventory(p)
            self.assertEqual(names, ['Word'])
            result = saver.report(names, self.products, self.mappings, 'macos', 'en', warnings)
            self.assertIn('coverage limitations', result)
            self.assertNotIn('PRIVATE_WARNING', result)
            self.assertNotIn('/private/secret', result)

    def test_malformed_json_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'apps.json'
            for value in [{'applications': 'Word'}, [123], [{'name': None}]]:
                p.write_text(json.dumps(value))
                with self.assertRaises(ValueError):
                    saver.inventory(p)

    def test_private_output_does_not_overwrite_and_has_restricted_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'report.md'
            saver.write_output(p, 'original')
            with self.assertRaises(FileExistsError):
                saver.write_output(p, 'replacement')
            self.assertEqual(p.read_text(), 'original')
            if os.name == 'posix':
                self.assertEqual(stat.S_IMODE(p.stat().st_mode), 0o600)

    def test_report_cli_keeps_private_contents_and_paths_off_stdout(self):
        with tempfile.TemporaryDirectory() as tmp:
            p, output = Path(tmp) / 'PRIVATE_PATH.txt', Path(tmp) / 'report.md'
            p.write_text('PRIVATE_APP\nWord\n', encoding='utf-8')
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = saver.main(['report', '--input', str(p), '--output', str(output), '--platform', 'macos'])
            self.assertEqual(code, 0)
            self.assertIn('PRIVATE_APP', output.read_text())
            self.assertNotIn('PRIVATE', out.getvalue() + err.getvalue())
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = saver.main(['report', '--input', str(p), '--output', str(output), '--platform', 'macos'])
            self.assertEqual(code, 2)
            self.assertNotIn('PRIVATE', out.getvalue() + err.getvalue())

    def test_untrusted_names_are_rendered_as_data(self):
        value = '[click](https://example.test) | <script>\n`command`'
        result = saver.report([value], self.products, self.mappings, 'macos', 'en')
        self.assertNotIn('<script>', result)
        self.assertNotIn('[click](', result)
        self.assertNotIn('`command`', result)
        self.assertIn('\\|', result)

    def test_versions_group_once_and_unknowns_remain_visible(self):
        result = saver.report(['Adobe Premiere Pro 2024', 'Adobe Premiere Pro 2025', 'UnknownExample'], self.products, self.mappings, 'macos', 'en')
        self.assertIn('mapped product groups: 1; unmatched: 1', result)
        self.assertIn('UnknownExample', result)
        self.assertIn('paid subscriptions and savings are not established', result)

    def test_mac_fixture_handles_corrupt_metadata_depth_and_symlinks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            def bundle(relative, metadata):
                p = root / relative / 'Contents'
                p.mkdir(parents=True)
                (p / 'Info.plist').write_bytes(plistlib.dumps(metadata))
            bundle('Good.app', {'CFBundleName': 'Example 中文', 'CFBundleIdentifier': 'test.example', 'CFBundleShortVersionString': '1.0'})
            bundle('Bad.app', ['not', 'a', 'dictionary'])
            bundle('one/two/three/TooDeep.app', {'CFBundleName': 'TooDeep'})
            if os.name != 'nt':
                (root / 'Alias.app').symlink_to(root / 'Good.app', target_is_directory=True)
            with mock.patch('socket.create_connection', side_effect=AssertionError('No network allowed')):
                data = collect_macos.collect([root])
            self.assertEqual([a['name'] for a in data['applications']], ['Example 中文'])
            self.assertTrue(data['warnings'])
            self.assertNotIn(tmp, json.dumps(data))


if __name__ == '__main__':
    unittest.main()
