$ErrorActionPreference = 'Stop'

$emDash = [char]0x2014
$chineseProject = [string]([char]0x9879) + [char]0x76EE
$chinesePlatform = [string]([char]0x5185) + [char]0x90E8 + [char]0x4F01 + [char]0x4E1A + [char]0x5E73 + [char]0x53F0
$chineseTitle = [string]([char]0x5185) + [char]0x90E8 + [char]0x4F01 + [char]0x4E1A + [char]0x8FD0 + [char]0x8425 + [char]0x5E73 + [char]0x53F0

$cases = @(
  @{ Path = 'index.html'; Marker = "PROJECT 08 $emDash INTERNAL ENTERPRISE PLATFORM"; Title = '<h3>Internal Enterprise Platform</h3>' },
  @{ Path = 'fr/index.html'; Marker = "PROJET 08 $emDash PLATEFORME D'ENTREPRISE INTERNE"; Title = '<h3>Plateforme d''entreprise interne</h3>' },
  @{ Path = 'zh/index.html'; Marker = "$chineseProject 08 $emDash $chinesePlatform"; Title = "<h3>$chineseTitle</h3>" }
)

$requiredTags = @('PHP 8.1', 'Symfony 6.4', 'Doctrine ORM', 'PostgreSQL', 'Docker', 'LDAP', 'GitLab API', 'FullCalendar')
$forbiddenIdentifiers = @('Universal Medica', 'UMP', 'universalmedica.com')

foreach ($case in $cases) {
  $content = [System.IO.File]::ReadAllText($case.Path, [System.Text.Encoding]::UTF8)

  if (([regex]::Matches($content, [regex]::Escape($case.Marker))).Count -ne 1) {
    throw "$($case.Path) must contain exactly one Project 08 marker."
  }

  if ($content -notlike "*$($case.Title)*") {
    throw "$($case.Path) is missing the Project 08 title."
  }

  foreach ($tag in $requiredTags) {
    $tagPattern = '*<li class="tag">' + $tag + '</li>*'
    if ($content -notlike $tagPattern) {
      throw "$($case.Path) is missing the $tag technology tag."
    }
  }

  foreach ($identifier in $forbiddenIdentifiers) {
    if ($content -match [regex]::Escape($identifier)) {
      throw "$($case.Path) exposes the prohibited identifier: $identifier"
    }
  }
}

Write-Output 'Project 08 portfolio assertions passed.'
