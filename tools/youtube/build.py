"""Generate the YouTube section of the site from tools/youtube/videos.json.

  python tools/youtube/build.py            # run from the site root

Writes, for each locale (en at the root, fr/, zh/):
  <locale>/youtube/index.html               the channel page: every video of that language, newest first
  <locale>/youtube/<topic>/index.html       one page per video: player, description with chapters, links
and
  the "YouTube" entry in the desktop and mobile menus of every page of the site (idempotent),
  the youtube block of sitemap.xml (between the youtube:start / youtube:end comments).

The chrome (header, drawer, footer) is copied from the AI Lab pages of the same locale and depth, so
the section stays consistent with the rest of the site without a template system. Videos of one topic
in different languages are each other's hreflang alternates.
"""
import html, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
VIDEOS = json.load(open(ROOT / "tools" / "youtube" / "videos.json", encoding="utf-8"))
SITE = "https://shenyi.dev"
CHANNEL_URL = "https://www.youtube.com/@shenyi-dev"
LOCALES = {"en": "", "fr": "fr/", "zh": "zh/"}
T = {
    "en": dict(menu="YouTube", menu_drawer="YouTube channel", lang_names={"en": "English", "fr": "Français", "zh": "中文"},
               change="Change language", eyebrow="YouTube channel", title="Videos on AI engineering, multi-agent development and SaaS.",
               sub="Short, practical videos from the shenyi-dev channel: Claude Code and Codex at work, RAG systems in production, multi-agent kits for regulated software, and SaaS copilots. Every video exists in English, French and Chinese.",
               subscribe="Subscribe on YouTube", all_videos="All videos", watch="Watch on YouTube", watch_card="Watch", also="Also in",
               more="More videos", more_title="Continue with the channel.", chapters="Chapters", minutes="min", list_eyebrow="All videos · English",
               list_title="videos, newest first.", page_title="YouTube channel | SHEN YI",
               page_desc="Videos by SHEN YI on AI engineering, multi-agent development with Claude Code, RAG systems and SaaS, in English, French and Chinese.",
               og_locale="en_US", links="Links", skip="Skip to content"),
    "fr": dict(menu="YouTube", menu_drawer="Chaîne YouTube", lang_names={"en": "English", "fr": "Français", "zh": "中文"},
               change="Changer de langue", eyebrow="Chaîne YouTube", title="Des vidéos sur l’ingénierie IA, le développement multi-agents et le SaaS.",
               sub="Des vidéos courtes et pratiques de la chaîne shenyi-dev : Claude Code et Codex au travail, des systèmes RAG en production, des kits multi-agents pour le logiciel réglementé, des copilotes SaaS. Chaque vidéo existe en français, en anglais et en chinois.",
               subscribe="S’abonner sur YouTube", all_videos="Toutes les vidéos", watch="Regarder sur YouTube", watch_card="Regarder", also="Aussi en",
               more="Autres vidéos", more_title="Continuer avec la chaîne.", chapters="Chapitres", minutes="min", list_eyebrow="Toutes les vidéos · Français",
               list_title="vidéos, les plus récentes d’abord.", page_title="Chaîne YouTube | SHEN YI",
               page_desc="Les vidéos de SHEN YI sur l’ingénierie IA, le développement multi-agents avec Claude Code, les systèmes RAG et le SaaS, en français, anglais et chinois.",
               og_locale="fr_FR", links="Liens", skip="Aller au contenu"),
    "zh": dict(menu="YouTube", menu_drawer="YouTube 频道", lang_names={"en": "English", "fr": "Français", "zh": "中文"},
               change="切换语言", eyebrow="YouTube 频道", title="关于 AI 工程、多智能体开发和 SaaS 的视频。",
               sub="shenyi-dev 频道的短视频，讲实际的做法：Claude Code 和 Codex 的日常使用、生产环境里的 RAG 系统、面向受监管软件的多智能体工具包、SaaS 副驾驶。每条视频都有中文、英文和法文版本。",
               subscribe="在 YouTube 上订阅", all_videos="全部视频", watch="在 YouTube 上观看", watch_card="观看", also="其他语言",
               more="更多视频", more_title="继续看这个频道。", chapters="章节", minutes="分钟", list_eyebrow="全部视频 · 中文",
               list_title="条视频，最新的在前。", page_title="YouTube 频道 | SHEN YI",
               page_desc="SHEN YI 的视频：AI 工程、用 Claude Code 做多智能体开发、RAG 系统和 SaaS，有中文、英文和法文版本。",
               og_locale="zh_CN", links="链接", skip="跳到正文"),
}
MONTHS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MONTHS_FR = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

def fmt_date(d, lang):
    y, m, day = int(d[:4]), int(d[5:7]), int(d[8:10])
    if lang == "fr": return f"{day} {MONTHS_FR[m-1]} {y}"
    if lang == "zh": return f"{y} 年 {m} 月 {day} 日"
    return f"{day} {MONTHS_EN[m-1]} {y}"

def fmt_dur(s, lang):
    m, sec = divmod(int(s), 60)
    if lang == "zh": return f"{m} 分 {sec:02d} 秒" if m else f"{sec} 秒"
    return f"{m}:{sec:02d} {T[lang]['minutes']}" if m else f"0:{sec:02d} {T[lang]['minutes']}"

def iso_dur(s):
    m, sec = divmod(int(s), 60); h, m = divmod(m, 60)
    return "PT" + (f"{h}H" if h else "") + (f"{m}M" if m else "") + f"{sec}S"

def esc(s): return html.escape(s, quote=True)

# ---------------------------------------------------------------- description rendering
URL = re.compile(r"(https?://[^\s<>\"]+[^\s<>\".,;:!?)])")
CHAPTER = re.compile(r"^((?:\d{1,2}:)?\d{1,2}:\d{2})\s+(.+)$")

def linkify(text):
    parts, last = [], 0
    for m in URL.finditer(text):
        parts.append(esc(text[last:m.start()]))
        u = m.group(1); parts.append(f'<a href="{esc(u)}" target="_blank" rel="noopener noreferrer">{esc(u)}</a>'); last = m.end()
    parts.append(esc(text[last:]))
    return "".join(parts)

def to_seconds(ts):
    p = [int(x) for x in ts.split(":")]
    return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]

def render_description(v, lang):
    out, para, bullets, chapters = [], [], [], []
    def flush_para():
        if para: out.append("<p>" + "<br>".join(para) + "</p>"); para.clear()
    def flush_bullets():
        if bullets: out.append("<ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>"); bullets.clear()
    def flush_chapters():
        if chapters:
            out.append(f'<ul class="yt-chapters">' + "".join(
                f'<li><a href="https://www.youtube.com/watch?v={v["id"]}&amp;t={to_seconds(ts)}s" target="_blank" rel="noopener noreferrer"><time>{esc(ts)}</time><span>{linkify(label)}</span></a></li>'
                for ts, label in chapters) + "</ul>"); chapters.clear()
    for raw in v["description"].splitlines():
        line = raw.strip()
        if not line:
            flush_para(); flush_bullets(); flush_chapters(); continue
        m = CHAPTER.match(line)
        if m:
            flush_para(); flush_bullets(); chapters.append((m.group(1), m.group(2))); continue
        flush_chapters()
        if line.startswith("#") and not line.startswith("#!") and re.match(r"^#{1,4}\s", line):
            flush_para(); flush_bullets(); out.append(f"<h3>{linkify(line.lstrip('#').strip())}</h3>"); continue
        if re.match(r"^[-•*]\s", line):
            flush_para(); bullets.append(linkify(line[1:].strip())); continue
        flush_bullets(); para.append(linkify(line))
    flush_para(); flush_bullets(); flush_chapters()
    return "\n".join(out)

def excerpt(text, n=150):
    t = re.sub(r"\s+", " ", text.split("\n\n")[0]).strip()
    t = re.sub(r"https?://\S+", "", t).strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0].rstrip(",;:") + "…"

# ---------------------------------------------------------------- chrome
def chrome(lang, depth):
    src = ROOT / LOCALES[lang] / ("ai-lab/index.html" if depth == 1 else "ai-lab/rag-engineer/index.html")
    s = src.read_text(encoding="utf-8")
    top = s[s.index("<header"):s.index("<main")]
    bottom = s[s.index("</main>") + len("</main>"):s.index("<script type=\"application/ld+json\">")]
    top = top.replace(' aria-current="page"', "")
    return top, bottom

def lang_block(lang, alternates, depth):
    rel = "../" * depth
    flags = {"en": "🇬🇧", "fr": "🇫🇷", "zh": "🇨🇳"}
    items = []
    for l in ("en", "fr", "zh"):
        href = "./" if l == lang else rel + LOCALES[l] + alternates[l]
        items.append(f'<a href="{href}" hreflang="{l}"{" aria-current=\"true\"" if l == lang else ""} role="menuitem">{T[lang]["lang_names"][l]}</a>')
    return (f'<div class="lang"><button class="lang-toggle" type="button" aria-expanded="false" aria-controls="lang-menu"><span aria-hidden="true">{flags[lang]}</span>'
            f'<span>{lang.upper()}</span><span class="lang-caret" aria-hidden="true">⌄</span><span class="sr-only">{T[lang]["change"]}</span></button>'
            f'<div class="lang-menu" id="lang-menu" role="menu">{"".join(items)}</div></div>')

def with_menu(top, lang, depth, current):
    """Insert the YouTube entry in a chrome's two menus and mark it current; replace the language block."""
    rel = "../" * depth
    top = add_menu_item(top, lang, rel)
    top = re.sub(r'(<a href="[^"]*youtube/")(>)', lambda m: m.group(1) + ' aria-current="page"' + m.group(2), top, count=1) if current else top
    return top

def add_menu_item(s, lang, rel):
    """The menu entry, in nav-desktop and in the drawer, after the AI Lab item (idempotent)."""
    href = rel + "youtube/"
    if re.search(r'<nav class="nav-desktop".*?href="[^"]*youtube/".*?</nav>', s, re.S): return s
    def ins_nav(m):
        block = m.group(0)
        li = re.search(r'<li><a href="[^"]*ai-lab[^"]*"[^>]*>.*?</a></li>', block, re.S)
        new = f'<li><a href="{href}">{T[lang]["menu"]}</a></li>'
        if li: return block[:li.end()] + new + block[li.end():]
        return block.replace("</ul>", new + "</ul>", 1)
    s = re.sub(r'<nav class="nav-desktop".*?</nav>', ins_nav, s, count=1, flags=re.S)
    def ins_drawer(m):
        block = m.group(0)
        li = re.search(r'<li><a href="[^"]*ai-lab[^"]*"[^>]*><i>\d+</i>.*?</a></li>', block, re.S)
        new = f'<li><a href="{href}"><i>00</i>{T[lang]["menu_drawer"]}</a></li>'
        block = (block[:li.end()] + new + block[li.end():]) if li else block.replace("</ul>", new + "</ul>", 1)
        n = [0]
        def renum(mm):
            n[0] += 1; return f"<i>{n[0]:02d}</i>"
        return re.sub(r"<i>\d+</i>", renum, block)
    s = re.sub(r'<div class="drawer".*?</nav>', ins_drawer, s, count=1, flags=re.S)
    return s

def head(lang, depth, title, desc, canonical, alternates, image, ld):
    rel = "../" * depth
    alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}/{LOCALES[l]}{p}">' for l, p in alternates.items())
    xdef = alternates.get("en", alternates[lang]); xdef_loc = "en" if "en" in alternates else lang
    alt += f'<link rel="alternate" hreflang="x-default" href="{SITE}/{LOCALES[xdef_loc]}{xdef}">'
    others = [l for l in alternates if l != lang]
    ogalt = "".join(f'<meta property="og:locale:alternate" content="{T[l]["og_locale"]}">' for l in others)
    return f'''<!DOCTYPE html>
<html lang="{ {"en": "en", "fr": "fr", "zh": "zh-CN"}[lang] }">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-S0YRBQKHLZ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('consent', 'default', {{
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'analytics_storage': 'denied'
  }});
  gtag('js', new Date());
  gtag('config', 'G-S0YRBQKHLZ');
</script>
<title>{esc(title)}</title>
<meta name="author" content="SHEN YI">
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}/{canonical}">{alt}
<meta property="og:type" content="{'video.other' if ld.get('@type') == 'VideoObject' else 'website'}"><meta property="og:site_name" content="SHEN YI — Full-Stack &amp; AI Solutions Developer"><meta property="og:locale" content="{T[lang]["og_locale"]}">{ogalt}<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:image" content="{image}"><meta property="og:url" content="{SITE}/{canonical}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{image}">
<link rel="icon" href="{rel}{"../" if lang != "en" else ""}assets/img/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{rel}{"../" if lang != "en" else ""}assets/css/style.css"><script>document.documentElement.classList.add("js");</script>
</head>
'''

def ld_json(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

# ---------------------------------------------------------------- pages
def by_topic():
    t = {}
    for v in VIDEOS: t.setdefault(v["topic"], {})[v["lang"]] = v
    return t

def card(v, lang, href_prefix, topics):
    tr = T[lang]; sib = topics[v["topic"]]
    also = " · ".join(f'<a href="{"../" * (1 if href_prefix == "" else 2)}{LOCALES[l]}youtube/{v["topic"]}/" hreflang="{l}">{l.upper()}</a>' for l in ("en", "fr", "zh") if l != lang and l in sib)
    return (f'<article class="card yt-card"><a class="yt-card-media" href="{href_prefix}{v["topic"]}/" aria-hidden="true" tabindex="-1">'
            f'<img src="https://i.ytimg.com/vi/{v["id"]}/hqdefault.jpg" width="480" height="360" loading="lazy" alt=""></a>'
            f'<span class="ai-lab-status">{fmt_dur(v["seconds"], lang)} · {fmt_date(v["published"], lang)}</span>'
            f'<h3><a href="{href_prefix}{v["topic"]}/">{esc(v["title"])}</a></h3><p class="card-focus">{esc(excerpt(v["description"]))}</p>'
            + (f'<p class="yt-langs">{tr["also"]}: {also}</p>' if also else "")
            + f'<a class="card-link" href="{href_prefix}{v["topic"]}/">{tr["watch_card"]} <span aria-hidden="true">→</span></a></article>')

def list_page(lang, topics):
    tr = T[lang]; vids = [v for v in VIDEOS if v["lang"] == lang]
    top, bottom = chrome(lang, 1)
    top = with_menu(top, lang, 1, current=True)
    top = re.sub(r'<div class="lang">.*?</div></div>', lang_block(lang, {l: "youtube/" for l in LOCALES}, 1), top, count=1, flags=re.S)
    top = re.sub(r'<a class="skip-link" href="#main">[^<]*</a>', f'<a class="skip-link" href="#main">{tr["skip"]}</a>', top, count=1)
    alternates = {l: "youtube/" for l in LOCALES}
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": tr["page_title"], "description": tr["page_desc"],
          "url": f"{SITE}/{LOCALES[lang]}youtube/", "inLanguage": lang, "author": {"@type": "Person", "name": "SHEN YI", "url": SITE + "/"},
          "hasPart": [{"@type": "VideoObject", "name": v["title"], "url": f"{SITE}/{LOCALES[lang]}youtube/{v['topic']}/", "thumbnailUrl": f"https://i.ytimg.com/vi/{v['id']}/hqdefault.jpg", "uploadDate": v["published"], "duration": iso_dur(v["seconds"])} for v in vids]}
    image = f"https://i.ytimg.com/vi/{vids[0]['id']}/maxresdefault.jpg" if vids else f"{SITE}/assets/img/og-image.png"
    body = (f'<body class="ai-lab-page yt-list-page">{top}<main id="main"><section class="hero wrap"><div class="hero-grid"><div><p class="eyebrow">{tr["eyebrow"]}</p><h1>{esc(tr["title"])}</h1>'
            f'<p class="ai-lab-hero-note">{esc(tr["sub"])}</p><div class="ai-lab-cta"><a class="btn btn-primary" href="{CHANNEL_URL}?sub_confirmation=1" target="_blank" rel="noopener noreferrer">{tr["subscribe"]} <span aria-hidden="true">↗</span></a></div></div>'
            f'<div><a class="yt-hero-media" href="{vids[0]["topic"]}/"><img src="https://i.ytimg.com/vi/{vids[0]["id"]}/hqdefault.jpg" width="480" height="360" alt="{esc(vids[0]["title"])}"><span class="yt-hero-play" aria-hidden="true">▶</span></a></div></div></section>'
            f'<section class="section wrap" id="videos"><div class="section-head"><p class="eyebrow">{tr["list_eyebrow"]}</p><h2 class="section-title">{len(vids)} {tr["list_title"]}</h2></div>'
            f'<div class="ai-lab-grid yt-grid">{"".join(card(v, lang, "", topics) for v in vids)}</div></section></main>'
            + bottom + ld_json(ld) + f'<script src="{"../" * (2 if lang != "en" else 1)}assets/js/main.js" defer></script></body></html>')
    page = head(lang, 1, tr["page_title"], tr["page_desc"], f"{LOCALES[lang]}youtube/", alternates, image, ld) + body
    out = ROOT / LOCALES[lang] / "youtube" / "index.html"; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out

def video_page(v, lang, topics):
    tr = T[lang]; sib = topics[v["topic"]]
    top, bottom = chrome(lang, 2)
    top = with_menu(top, lang, 2, current=False)
    alternates = {l: f"youtube/{v['topic']}/" for l in ("en", "fr", "zh") if l in sib}
    top = re.sub(r'<div class="lang">.*?</div></div>', lang_block(lang, {l: alternates.get(l, "youtube/") for l in LOCALES}, 2), top, count=1, flags=re.S)
    top = re.sub(r'<a class="skip-link" href="#main">[^<]*</a>', f'<a class="skip-link" href="#main">{tr["skip"]}</a>', top, count=1)
    vids = [x for x in VIDEOS if x["lang"] == lang]
    i = vids.index(v); neighbours = [x for x in (vids[i - 1] if i > 0 else None, vids[i + 1] if i + 1 < len(vids) else None) if x]
    also = " · ".join(f'<a href="../../{LOCALES[l]}youtube/{v["topic"]}/" hreflang="{l}">{T[lang]["lang_names"][l]}</a>' for l in ("en", "fr", "zh") if l != lang and l in sib)
    desc = excerpt(v["description"], 200)
    ld = {"@context": "https://schema.org", "@type": "VideoObject", "name": v["title"], "description": excerpt(v["description"], 300),
          "thumbnailUrl": [f"https://i.ytimg.com/vi/{v['id']}/maxresdefault.jpg", f"https://i.ytimg.com/vi/{v['id']}/hqdefault.jpg"],
          "uploadDate": v["published"], "duration": iso_dur(v["seconds"]), "embedUrl": f"https://www.youtube-nocookie.com/embed/{v['id']}",
          "contentUrl": f"https://www.youtube.com/watch?v={v['id']}", "url": f"{SITE}/{LOCALES[lang]}youtube/{v['topic']}/", "inLanguage": lang,
          "author": {"@type": "Person", "name": "SHEN YI", "url": SITE + "/"}, "publisher": {"@type": "Person", "name": "SHEN YI"}}
    body = (f'<body class="ai-lab-page yt-page">{top}<main id="main"><section class="hero wrap"><p class="eyebrow">{tr["eyebrow"]} · {fmt_date(v["published"], lang)} · {fmt_dur(v["seconds"], lang)}</p><h1>{esc(v["title"])}</h1>'
            + (f'<p class="yt-langs">{tr["also"]}: {also}</p>' if also else "")
            + f'<div class="video-embed"><iframe src="https://www.youtube-nocookie.com/embed/{v["id"]}" title="{esc(v["title"])}" loading="lazy" allow="accelerometer; encrypted-media; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'
            f'<div class="ai-lab-cta"><a class="btn btn-primary" href="https://www.youtube.com/watch?v={v["id"]}" target="_blank" rel="noopener noreferrer">{tr["watch"]} <span aria-hidden="true">↗</span></a><a class="btn btn-ghost" href="../">{tr["all_videos"]}</a></div></section>'
            f'<section class="section wrap"><div class="yt-desc">{render_description(v, lang)}</div></section>'
            + (f'<section class="section wrap"><div class="section-head"><p class="eyebrow">{tr["more"]}</p><h2 class="section-title">{esc(tr["more_title"])}</h2></div><div class="ai-lab-grid yt-grid">{"".join(card(x, lang, "../", topics) for x in neighbours)}</div></section>' if neighbours else "")
            + '</main>' + bottom + ld_json(ld) + f'<script src="../../{"../" if lang != "en" else ""}assets/js/main.js" defer></script></body></html>')
    page = head(lang, 2, f'{v["title"]} | SHEN YI', desc, f"{LOCALES[lang]}youtube/{v['topic']}/", alternates, f"https://i.ytimg.com/vi/{v['id']}/maxresdefault.jpg", ld) + body
    out = ROOT / LOCALES[lang] / "youtube" / v["topic"] / "index.html"; out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out

# ---------------------------------------------------------------- site-wide menu and sitemap
def add_menu_everywhere():
    changed = 0
    for p in ROOT.rglob("*.html"):
        rel_parts = p.relative_to(ROOT).parts
        if rel_parts[0] in (".git", "node_modules", "tools", "tests", "docs"): continue
        if "youtube" in rel_parts: continue
        lang = rel_parts[0] if rel_parts[0] in ("fr", "zh") else "en"
        depth = len(rel_parts) - 1 - (1 if lang != "en" else 0)
        s = p.read_text(encoding="utf-8")
        if 'class="nav-desktop"' not in s or 'class="drawer"' not in s: continue   # lesson pages carry a local nav, not the site menu
        new = add_menu_item(s, lang, "../" * depth)
        if new != s: p.write_text(new, encoding="utf-8"); changed += 1
    return changed

def sitemap(topics):
    sm = ROOT / "sitemap.xml"; s = sm.read_text(encoding="utf-8")
    s = re.sub(r"\s*<!-- youtube:start -->.*?<!-- youtube:end -->", "", s, flags=re.S)
    today = max(v["published"] for v in VIDEOS)
    def url(loc, lastmod, prio, alts):
        links = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{h}"/>' for l, h in alts)
        return f"\n  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>{prio}</priority>{links}\n  </url>"
    block = ["\n  <!-- youtube:start -->"]
    alts = [(l, f"{SITE}/{LOCALES[l]}youtube/") for l in LOCALES] + [("x-default", f"{SITE}/youtube/")]
    for l in LOCALES: block.append(url(f"{SITE}/{LOCALES[l]}youtube/", today, "0.8", alts))
    for topic, sib in topics.items():
        alts = [(l, f"{SITE}/{LOCALES[l]}youtube/{topic}/") for l in ("en", "fr", "zh") if l in sib]
        alts.append(("x-default", f"{SITE}/{LOCALES['en' if 'en' in sib else list(sib)[0]]}youtube/{topic}/"))
        for l, v in sib.items(): block.append(url(f"{SITE}/{LOCALES[l]}youtube/{topic}/", v["published"], "0.6", alts))
    block.append("\n  <!-- youtube:end -->\n")
    s = s.replace("</urlset>", "".join(block) + "</urlset>")
    sm.write_text(s, encoding="utf-8")

def main():
    topics = by_topic()
    pages = [list_page(l, topics) for l in LOCALES] + [video_page(v, v["lang"], topics) for v in VIDEOS]
    n = add_menu_everywhere()
    sitemap(topics)
    print(f"{len(pages)} pages written, menu added on {n} other pages, sitemap updated; {len(topics)} topics, {len(VIDEOS)} videos")

if __name__ == "__main__":
    main()
