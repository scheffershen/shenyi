$ErrorActionPreference = 'Stop'

# The YouTube section: tools/youtube/build.py generates <locale>/youtube/ and one page per video.
# This script checks the generated pages, the menu entry on every page, and the sitemap block.

$videos = Get-Content -Raw -Encoding UTF8 'tools/youtube/videos.json' | ConvertFrom-Json
$locales = @{ en = ''; fr = 'fr/'; zh = 'zh/' }
$forbiddenIdentifiers = @('Universal Medica', 'UMP', 'universalmedica.com')

foreach ($lang in $locales.Keys) {
  $list = "$($locales[$lang])youtube/index.html"
  if (-not (Test-Path $list)) { throw "$list is missing." }
  $content = [System.IO.File]::ReadAllText($list, [System.Text.Encoding]::UTF8)
  $expected = @($videos | Where-Object { $_.lang -eq $lang }).Count
  $cards = ([regex]::Matches($content, '<article class="card yt-card">')).Count
  if ($cards -ne $expected) { throw "$list has $cards cards, expected $expected." }
  if ($content -notmatch 'hreflang="x-default"') { throw "$list has no x-default alternate." }
  if ($content -notmatch 'aria-current="page"') { throw "$list does not mark the YouTube menu entry current." }
  if (([regex]::Matches($content, 'youtube-nocookie|i\.ytimg\.com')).Count -lt 1) { throw "$list shows no thumbnail." }
}

foreach ($v in $videos) {
  $page = "$($locales[$v.lang])youtube/$($v.topic)/index.html"
  if (-not (Test-Path $page)) { throw "$page is missing." }
  $content = [System.IO.File]::ReadAllText($page, [System.Text.Encoding]::UTF8)
  $embed = 'src="https://www.youtube-nocookie.com/embed/' + $v.id + '"'
  if (([regex]::Matches($content, [regex]::Escape($embed))).Count -ne 1) { throw "$page must embed $($v.id) exactly once." }
  if ($content -notmatch '"@type": ?"VideoObject"') { throw "$page has no VideoObject structured data." }
  $videoData = @([regex]::Matches($content, '<script type="application/ld\+json">(.*?)</script>', 'Singleline') | ForEach-Object {
    $json = $_.Groups[1].Value
    if (($json | ConvertFrom-Json).'@type' -eq 'VideoObject') { $json }
  })
  if ($videoData.Count -ne 1) { throw "$page must contain exactly one VideoObject." }
  # Inspect the literal: ConvertFrom-Json can convert ISO strings to local DateTime objects.
  $uploadDate = [regex]::Match($videoData[0], '"uploadDate"\s*:\s*"([^"]+)"').Groups[1].Value
  if ($uploadDate -notmatch '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$') {
    throw "$page uploadDate must include an ISO 8601 time and timezone: $uploadDate"
  }
  $parsedDate = [DateTimeOffset]::MinValue
  if (-not [DateTimeOffset]::TryParse($uploadDate, [System.Globalization.CultureInfo]::InvariantCulture, [System.Globalization.DateTimeStyles]::None, [ref]$parsedDate)) {
    throw "$page has an invalid uploadDate: $uploadDate"
  }
  if ($parsedDate.ToUniversalTime() -ne ([DateTimeOffset]$v.published).ToUniversalTime()) {
    throw "$page uploadDate differs from the imported publication timestamp."
  }
  if ($content -notmatch 'rel="canonical" href="https://shenyi.dev/' + [regex]::Escape($locales[$v.lang] + 'youtube/' + $v.topic + '/') + '"') { throw "$page has a wrong canonical." }
  foreach ($identifier in $forbiddenIdentifiers) {
    if ($content -match [regex]::Escape($identifier)) { throw "$page exposes the prohibited identifier: $identifier" }
  }
}

# Alternates: a video page links every sibling of its topic, and only those.
$byTopic = $videos | Group-Object topic
foreach ($g in $byTopic) {
  foreach ($v in $g.Group) {
    $content = [System.IO.File]::ReadAllText("$($locales[$v.lang])youtube/$($v.topic)/index.html", [System.Text.Encoding]::UTF8)
    foreach ($sib in $g.Group) {
      $alt = 'hreflang="' + $sib.lang + '" href="https://shenyi.dev/' + $locales[$sib.lang] + 'youtube/' + $sib.topic + '/"'
      if ($content -notlike "*$alt*") { throw "$($v.id) page lacks the $($sib.lang) alternate." }
    }
  }
}

# The menu entry on every page that has the site navigation.
$pages = Get-ChildItem -Recurse -Filter *.html | Where-Object { $_.FullName -notmatch '\\(\.git|node_modules|tools|tests|docs)\\' }
foreach ($p in $pages) {
  $content = [System.IO.File]::ReadAllText($p.FullName, [System.Text.Encoding]::UTF8)
  if ($content -notmatch 'class="nav-desktop"' -or $content -notmatch 'class="drawer"') { continue }
  $nav = [regex]::Match($content, '<nav class="nav-desktop".*?</nav>', 'Singleline').Value
  if ($nav -notmatch 'href="[^"]*youtube/"') { throw "$($p.FullName) has no YouTube entry in the desktop menu." }
  $drawer = [regex]::Match($content, '<div class="drawer".*?</nav>', 'Singleline').Value
  if ($drawer -notmatch 'href="[^"]*youtube/"') { throw "$($p.FullName) has no YouTube entry in the drawer." }
  $numbers = [regex]::Matches($drawer, '<i>(\d+)</i>') | ForEach-Object { [int]$_.Groups[1].Value }
  for ($i = 0; $i -lt $numbers.Count; $i++) { if ($numbers[$i] -ne $i + 1) { throw "$($p.FullName) drawer numbering is not sequential." } }
}

# The sitemap block.
$sitemap = [System.IO.File]::ReadAllText('sitemap.xml', [System.Text.Encoding]::UTF8)
if (([regex]::Matches($sitemap, '<!-- youtube:start -->')).Count -ne 1) { throw 'sitemap.xml must contain exactly one youtube block.' }
foreach ($v in $videos) {
  $loc = '<loc>https://shenyi.dev/' + $locales[$v.lang] + 'youtube/' + $v.topic + '/</loc>'
  if ($sitemap -notlike "*$loc*") { throw "sitemap.xml lacks $loc" }
}

Write-Output "YouTube pages assertions passed ($($videos.Count) videos, $($byTopic.Count) topics)."
