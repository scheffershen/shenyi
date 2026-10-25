"""Refresh tools/youtube/videos.json from the YouTube channel @shenyi-dev.

  python tools/youtube/fetch.py            # run from the site root

Reads the channel's videos tab for the list of ids, then every watch page for title, description,
length, date and keywords (the public page data, no API key). Each video gets its language from its
title (Chinese characters -> zh, French accents or words -> fr, else en) and its topic from
topics.json; a video without a topic is listed with a warning and gets a slug from its title.
Nothing here runs at build time of the site: videos.json is committed and build.py reads it.
"""
import json, pathlib, re, subprocess, sys, unicodedata

HERE = pathlib.Path(__file__).resolve().parent
CHANNEL = "UCCQrpZA-ULu8jaa0UGuVNtg"
HANDLE = "https://www.youtube.com/@shenyi-dev"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"

def get(url):
    return subprocess.run(["curl", "-s", "-L", "-A", UA, "-H", "Accept-Language: en", "--cookie", "CONSENT=YES+cb; SOCS=CAI", url],
                          capture_output=True).stdout.decode("utf-8", "replace")

def lang_of(title):
    if re.search(r"[一-鿿]", title): return "zh"
    if re.search(r"[éèêàçùœ]|\b(Comment|Votre|votre|vos|Créer|quels|quand|pour|des|les|une|avec|sur|Leçon|Faites|Pourquoi|Automatiser|vraiment)\b|qu'est", title): return "fr"
    return "en"

def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return text[:70].rstrip("-") or "video"

def main():
    topics = {k: v for k, v in json.loads((HERE / "topics.json").read_text(encoding="utf-8")).items() if not k.startswith("_")}
    page = get(f"{HANDLE}/videos")
    ids = []
    for m in re.finditer(r'"videoId":"([A-Za-z0-9_-]{11})"', page):
        if m.group(1) not in ids: ids.append(m.group(1))
    print(len(ids), "video ids on the channel page")
    out = []
    for vid in ids:
        watch = get(f"https://www.youtube.com/watch?v={vid}")
        m = re.search(r"ytInitialPlayerResponse\s*=\s*(\{.*?\});", watch, re.S)
        if not m: print("  no data for", vid); continue
        pr = json.loads(m.group(1))
        vd = pr.get("videoDetails", {}); mf = pr.get("microformat", {}).get("playerMicroformatRenderer", {})
        if vd.get("channelId") != CHANNEL: continue
        title = vd.get("title", "")
        topic = topics.get(vid)
        if not topic:
            topic = slugify(title); print("  WARNING no topic for", vid, "->", topic)
        out.append(dict(id=vid, lang=lang_of(title), topic=topic, title=title, description=vd.get("shortDescription", ""),
                        seconds=int(vd.get("lengthSeconds", 0)), published=mf.get("publishDate", ""),
                        keywords=vd.get("keywords", []), views=int(vd.get("viewCount", 0) or 0)))
        print(" ", out[-1]["published"], vid, out[-1]["lang"], out[-1]["seconds"], "s")
    out.sort(key=lambda v: (v["published"], v["topic"], v["lang"]), reverse=True)
    (HERE / "videos.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(len(out), "videos ->", HERE / "videos.json")

if __name__ == "__main__":
    main()
