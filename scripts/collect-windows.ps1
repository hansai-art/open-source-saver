# Read-only current-user/system inventory. No elevation, network, Win32_Product or uninstall calls.
[CmdletBinding()]
param([Parameter(Mandatory=$true)][string]$OutputPath)
$ErrorActionPreference = 'Stop'
if ($env:OS -ne 'Windows_NT') { throw 'Run this collector on the target Windows computer.' }
if (Test-Path -LiteralPath $OutputPath) { throw 'Output already exists; choose a new filename.' }
$apps = [System.Collections.Generic.List[object]]::new()
$warnings = [System.Collections.Generic.List[string]]::new()
$seen = @{}
foreach ($hive in @([Microsoft.Win32.RegistryHive]::LocalMachine, [Microsoft.Win32.RegistryHive]::CurrentUser)) {
    foreach ($view in @([Microsoft.Win32.RegistryView]::Registry64, [Microsoft.Win32.RegistryView]::Registry32)) {
        $base = $null; $uninstall = $null
        try {
            $base = [Microsoft.Win32.RegistryKey]::OpenBaseKey($hive, $view)
            $uninstall = $base.OpenSubKey('SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall')
            if ($null -eq $uninstall) { continue }
            foreach ($id in $uninstall.GetSubKeyNames()) {
                $entry = $null
                try {
                    $entry = $uninstall.OpenSubKey($id)
                    if ($null -eq $entry) { continue }
                    $name = [string]$entry.GetValue('DisplayName')
                    if ([string]::IsNullOrWhiteSpace($name)) { continue }
                    $version = [string]$entry.GetValue('DisplayVersion')
                    $publisher = [string]$entry.GetValue('Publisher')
                    $key = "$name`0$version`0$publisher"
                    if (-not $seen.ContainsKey($key)) {
                        $seen[$key] = $true
                        $apps.Add([ordered]@{name=$name; version=$version; publisher=$publisher; collector='registry'})
                    }
                } catch { $warnings.Add('An uninstall entry could not be read') }
                finally { if ($null -ne $entry) { $entry.Dispose() } }
            }
        } catch { $warnings.Add('A registry scope could not be read') }
        finally {
            if ($null -ne $uninstall) { $uninstall.Dispose() }
            if ($null -ne $base) { $base.Dispose() }
        }
    }
}
try {
    foreach ($app in @(Get-AppxPackage -ErrorAction Stop)) {
        if ($app.IsFramework -or $app.IsResourcePackage) { continue }
        $apps.Add([ordered]@{name=[string]$app.Name; version=[string]$app.Version; package_id=[string]$app.PackageFamilyName; collector='appx-current-user'})
    }
} catch { $warnings.Add('Current-user Appx enumeration unavailable') }
$result = [ordered]@{
    schema_version=1; platform='windows'; collector='registry-and-appx'
    collected_at=[DateTime]::UtcNow.ToString('o')
    coverage='Readable HKLM/HKCU uninstall records and current-user Appx; portable apps and other users may be absent'
    warnings=@($warnings | Sort-Object -Unique); applications=@($apps.ToArray())
}
$json = $result | ConvertTo-Json -Depth 5
$fullPath = [IO.Path]::GetFullPath($OutputPath)
$null = [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($fullPath))
$stream = [IO.File]::Open($fullPath, [IO.FileMode]::CreateNew, [IO.FileAccess]::Write, [IO.FileShare]::None)
try {
    $bytes = [Text.UTF8Encoding]::new($false).GetBytes($json)
    $stream.Write($bytes, 0, $bytes.Length)
} finally { $stream.Dispose() }
Write-Output 'Inventory saved locally; contents were not printed.'
