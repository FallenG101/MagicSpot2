param(
    [Parameter(Mandatory=$true)][string]$Binary,
    [Parameter(Mandatory=$true)][string]$OutputDir
)
$ErrorActionPreference = 'Stop'
$repoPath = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$binaryPath = (Resolve-Path -LiteralPath $Binary).Path
$manifest = Get-Content -Raw -LiteralPath (Join-Path $repoPath 'Cargo.toml')
$version = [regex]::Match($manifest, '(?m)^version = "([^"]+)"').Groups[1].Value
if (-not $version) { throw 'No package version found' }
$reported = (& $binaryPath --version | Out-String).Trim()
if ($LASTEXITCODE -ne 0 -or $reported -ne "magicspot2 $version") {
    throw "Wrong binary/version: $reported"
}
$outputPath = [IO.Path]::GetFullPath($OutputDir)
$stem = "magicspot2-v$version-x86_64-pc-windows-msvc"
$folder = Join-Path $outputPath $stem
if (Test-Path -LiteralPath $folder) { throw 'Use a fresh output directory' }
New-Item -ItemType Directory -Path $folder -Force | Out-Null
Copy-Item -LiteralPath $binaryPath -Destination (Join-Path $folder 'magicspot2.exe')
Copy-Item -LiteralPath (Join-Path $repoPath 'LICENSE') -Destination $folder
Copy-Item -LiteralPath (Join-Path $repoPath 'README.md') -Destination $folder
New-Item -ItemType Directory -Path (Join-Path $folder 'licenses') | Out-Null
foreach ($license in @('assets\fonts\Inter-LICENSE.txt','assets\fonts\NotoEmoji-LICENSE.txt','assets\icons\LICENSE.txt')) {
    $name = $license.Replace('assets\','').Replace('\','-')
    Copy-Item -LiteralPath (Join-Path $repoPath $license) -Destination (Join-Path $folder "licenses\$name")
}
$archive = Join-Path $outputPath "$stem.zip"
Compress-Archive -LiteralPath $folder -DestinationPath $archive -CompressionLevel Optimal
$hash = (Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant()
Set-Content -LiteralPath (Join-Path $outputPath 'checksums.txt') -Value "$hash  $stem.zip" -Encoding ascii
Write-Output $archive
