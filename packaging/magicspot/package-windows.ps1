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
$headers = & dumpbin /headers $binaryPath | Out-String
if ($LASTEXITCODE -ne 0 -or $headers -notmatch '8664 machine \(x64\)') {
    throw 'The Windows download must be an x64 PE executable'
}
$imports = & dumpbin /dependents $binaryPath | Out-String
if ($LASTEXITCODE -ne 0 -or $imports -match 'MSVCP[0-9_]*\.dll|VCRUNTIME[0-9_]*\.dll') {
    throw "The Windows download requires an external MSVC runtime: $imports"
}
$outputPath = [IO.Path]::GetFullPath($OutputDir)
$stem = "magicspot2-v$version-x86_64-pc-windows-msvc"
$exeName = "$stem.exe"
$licensesName = "magicspot2-v$version-THIRD-PARTY-LICENSES.txt"
if (Test-Path -LiteralPath $outputPath) { throw 'Use a fresh output directory' }
New-Item -ItemType Directory -Path $outputPath | Out-Null
$exeOutput = Join-Path $outputPath $exeName
Copy-Item -LiteralPath $binaryPath -Destination $exeOutput

$licenses = @(
    @{ Name = 'MagicSpot (MIT License)'; Path = 'LICENSE' },
    @{ Name = 'Inter (SIL Open Font License 1.1)'; Path = 'assets\fonts\Inter-LICENSE.txt' },
    @{ Name = 'Noto Emoji (SIL Open Font License 1.1)'; Path = 'assets\fonts\NotoEmoji-LICENSE.txt' },
    @{ Name = 'Lucide icons (ISC License)'; Path = 'assets\icons\LICENSE.txt' },
    @{ Name = 'projectM (GNU Lesser General Public License 2.1)'; Path = 'assets\licenses\projectM-LICENSE.txt' }
)
$sections = foreach ($license in $licenses) {
    $path = Join-Path $repoPath $license.Path
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Missing license file: $path" }
    "===== $($license.Name) =====`r`n$([IO.File]::ReadAllText($path, [Text.Encoding]::UTF8).Trim())"
}
$licensesOutput = Join-Path $outputPath $licensesName
[IO.File]::WriteAllText($licensesOutput, (($sections -join "`r`n`r`n") + "`r`n"), [Text.UTF8Encoding]::new($false))

$checksumLines = @($exeOutput, $licensesOutput) |
    Sort-Object { [IO.Path]::GetFileName($_) } |
    ForEach-Object { "$((Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash.ToLowerInvariant())  $([IO.Path]::GetFileName($_))" }
[IO.File]::WriteAllLines((Join-Path $outputPath 'checksums.txt'), [string[]]$checksumLines, [Text.Encoding]::ASCII)
Write-Output $exeOutput
