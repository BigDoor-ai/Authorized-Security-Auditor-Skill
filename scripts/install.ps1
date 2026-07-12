param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("codex", "claude")]
    [string]$Agent,

    [Parameter(Mandatory = $true)]
    [ValidateSet("project", "user")]
    [string]$Scope,

    [string]$TargetPath = (Get-Location).Path
)

$ErrorActionPreference = "Stop"
$SkillName = "authorized-security-auditor"
$SourceDir = Split-Path -Parent $PSScriptRoot

if ($Agent -eq "codex") {
    if ($Scope -eq "user") {
        $Destination = Join-Path $HOME ".agents\skills\$SkillName"
    } else {
        $Destination = Join-Path (Resolve-Path $TargetPath) ".agents\skills\$SkillName"
    }
} else {
    if ($Scope -eq "user") {
        $Destination = Join-Path $HOME ".claude\skills\$SkillName"
    } else {
        $Destination = Join-Path (Resolve-Path $TargetPath) ".claude\skills\$SkillName"
    }
}

New-Item -ItemType Directory -Force -Path $Destination | Out-Null
Copy-Item (Join-Path $SourceDir "SKILL.md") (Join-Path $Destination "SKILL.md") -Force

foreach ($Folder in @("references", "templates", "assets")) {
    $TargetFolder = Join-Path $Destination $Folder
    if (Test-Path $TargetFolder) {
        Remove-Item $TargetFolder -Recurse -Force
    }
    Copy-Item (Join-Path $SourceDir $Folder) $TargetFolder -Recurse -Force
}

Copy-Item (Join-Path $SourceDir "BRANDING.md") (Join-Path $Destination "BRANDING.md") -Force
Copy-Item (Join-Path $SourceDir "NOTICE") (Join-Path $Destination "NOTICE") -Force

Write-Host "Installed $SkillName for $Agent at $Destination"
Write-Host "Powered by Bigdoor AI Labs Pte. Ltd."
Write-Host "https://bigdoor.ai | viisesh@bigdoor.ai"
