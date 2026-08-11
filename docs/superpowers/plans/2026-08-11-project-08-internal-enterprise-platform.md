# Project 08 — Internal Enterprise Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a confidential, multilingual Project 08 case-study card that credits Yi SHEN as Lead Developer of an internal enterprise platform.

**Architecture:** The static site has one portfolio grid per language page. Add the same card structure after Project 07 on each page, with localised copy and a shared technology stack. A PowerShell regression test asserts the required card content and rules out corporate identifiers.

**Tech Stack:** HTML5, existing portfolio CSS, PowerShell static-content assertions.

---

## File structure

- `tests/portfolio-project-08.ps1` — asserts the three cards, their headings and tags, and the absence of corporate identifiers.
- `index.html` — English Project 08 card.
- `fr/index.html` — French Project 08 card.
- `zh/index.html` — Chinese Project 08 card.

### Task 1: Add a failing portfolio regression test

**Files:**
- Create: `tests/portfolio-project-08.ps1`

- [ ] **Step 1: Write the failing test**

Create `tests/portfolio-project-08.ps1`:

```powershell
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
  if (([regex]::Matches($content, [regex]::Escape($case.Marker))).Count -ne 1) { throw "$($case.Path) must contain exactly one Project 08 marker." }
  if ($content -notlike "*$($case.Title)*") { throw "$($case.Path) is missing the Project 08 title." }
  foreach ($tag in $requiredTags) {
    $tagPattern = '*<li class="tag">' + $tag + '</li>*'
    if ($content -notlike $tagPattern) { throw "$($case.Path) is missing the $tag technology tag." }
  }
  foreach ($identifier in $forbiddenIdentifiers) {
    if ($content -match [regex]::Escape($identifier)) { throw "$($case.Path) exposes the prohibited identifier: $identifier" }
  }
}
Write-Output 'Project 08 portfolio assertions passed.'
```

- [ ] **Step 2: Run the test to verify it fails**

Run: `powershell -ExecutionPolicy Bypass -File tests/portfolio-project-08.ps1`

Expected: failure because none of the three Project 08 markers exists.

### Task 2: Add the three confidential Project 08 cards

**Files:**
- Modify: `index.html:443`, immediately after the Project 07 closing `</article>`.
- Modify: `fr/index.html:451`, immediately after the Project 07 closing `</article>`.
- Modify: `zh/index.html:430`, immediately after the Project 07 closing `</article>`.

- [ ] **Step 1: Add the English card**

Insert after Project 07 in `index.html`:

```html
      <article class="card reveal" data-delay="0.56">
        <p class="card-index">PROJECT 08 — INTERNAL ENTERPRISE PLATFORM</p>
        <h3>Internal Enterprise Platform</h3>
        <p class="card-focus">As Lead Developer, led the development of a confidential enterprise operations platform, bringing together project administration, time and leave tracking, expense approvals, organisational access controls, reporting and engineering-activity data.</p>
        <div class="metric"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 17l6-6 4 4 7-7"/><path d="M14 8h6v6"/></svg><p>A single secure workspace for operations, approvals and reporting, with enterprise authentication and role-based access.</p></div>
        <ul class="tags"><li class="tag">PHP 8.1</li><li class="tag">Symfony 6.4</li><li class="tag">Doctrine ORM</li><li class="tag">PostgreSQL</li><li class="tag">Docker</li><li class="tag">LDAP</li><li class="tag">GitLab API</li><li class="tag">FullCalendar</li></ul>
      </article>
```

- [ ] **Step 2: Add the French card**

Insert after Project 07 in `fr/index.html`:

```html
      <article class="card reveal" data-delay="0.56">
        <p class="card-index">PROJET 08 — PLATEFORME D'ENTREPRISE INTERNE</p>
        <h3>Plateforme d'entreprise interne</h3>
        <p class="card-focus">En tant que Lead Developer, j'ai piloté le développement d'une plateforme opérationnelle d'entreprise confidentielle, centralisant la gestion de projets, le suivi du temps et des absences, les notes de frais, les permissions organisationnelles, le reporting et les données d'activité d'ingénierie.</p>
        <div class="metric"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 17l6-6 4 4 7-7"/><path d="M14 8h6v6"/></svg><p>Un espace de travail sécurisé unique pour les opérations, les validations et le reporting, avec authentification d'entreprise et accès fondé sur les rôles.</p></div>
        <ul class="tags"><li class="tag">PHP 8.1</li><li class="tag">Symfony 6.4</li><li class="tag">Doctrine ORM</li><li class="tag">PostgreSQL</li><li class="tag">Docker</li><li class="tag">LDAP</li><li class="tag">GitLab API</li><li class="tag">FullCalendar</li></ul>
      </article>
```

- [ ] **Step 3: Add the Chinese card**

Insert after Project 07 in `zh/index.html`:

```html
      <article class="card reveal" data-delay="0.56">
        <p class="card-index">项目 08 — 内部企业平台</p>
        <h3>内部企业运营平台</h3>
        <p class="card-focus">作为 Lead Developer，主导开发一套保密的企业运营平台，整合项目管理、工时与休假追踪、费用审批、组织权限控制、报表以及工程活动数据。</p>
        <div class="metric"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 17l6-6 4 4 7-7"/><path d="M14 8h6v6"/></svg><p>一个统一、安全的工作空间，支持运营、审批与报表，并提供企业级身份认证和基于角色的访问控制。</p></div>
        <ul class="tags"><li class="tag">PHP 8.1</li><li class="tag">Symfony 6.4</li><li class="tag">Doctrine ORM</li><li class="tag">PostgreSQL</li><li class="tag">Docker</li><li class="tag">LDAP</li><li class="tag">GitLab API</li><li class="tag">FullCalendar</li></ul>
      </article>
```

- [ ] **Step 4: Run the test to verify it passes**

Run: `powershell -ExecutionPolicy Bypass -File tests/portfolio-project-08.ps1`

Expected: `Project 08 portfolio assertions passed.`

### Task 3: Check and commit the focused change

**Files:**
- Verify: `index.html`, `fr/index.html`, `zh/index.html`, `tests/portfolio-project-08.ps1`

- [ ] **Step 1: Confirm structural balance and confidentiality**

Run:

```powershell
$pages = 'index.html', 'fr/index.html', 'zh/index.html'
foreach ($page in $pages) {
  $content = Get-Content -Raw -Encoding UTF8 $page
  if (([regex]::Matches($content, '<article\\b')).Count -ne ([regex]::Matches($content, '</article>')).Count) { throw "$page has unbalanced article tags." }
  if ($content -match 'Universal Medica|UMP|universalmedica\\.com') { throw "$page contains a prohibited corporate identifier." }
}
Write-Output 'HTML structure and confidentiality checks passed.'
```

Expected: `HTML structure and confidentiality checks passed.`

- [ ] **Step 2: Review the focused diff**

Run: `git diff --check; git diff -- index.html fr/index.html zh/index.html tests/portfolio-project-08.ps1`

Expected: no whitespace errors and a diff limited to Project 08 cards and its regression test.

- [ ] **Step 3: Commit the feature**

Run: `git add index.html fr/index.html zh/index.html tests/portfolio-project-08.ps1 docs/superpowers/plans/2026-08-11-project-08-internal-enterprise-platform.md; git commit -m "feat: add internal enterprise platform portfolio project"`

Expected: a commit containing only the new cards, regression test, and implementation plan.
