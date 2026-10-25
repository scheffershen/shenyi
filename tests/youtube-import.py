"""Regression checks for YouTube imports and generated video structured data."""
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("youtube_fetch", ROOT / "tools/youtube/fetch.py")
fetch = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fetch)
spec = importlib.util.spec_from_file_location("youtube_build", ROOT / "tools/youtube/build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class PublicationTimestampTest(unittest.TestCase):
    def test_all_video_objects_have_descriptions_and_video_urls(self):
        def videos_in(value):
            if isinstance(value, dict):
                types = value.get("@type", [])
                if types == "VideoObject" or isinstance(types, list) and "VideoObject" in types:
                    yield value
                for child in value.values():
                    yield from videos_in(child)
            elif isinstance(value, list):
                for child in value:
                    yield from videos_in(child)

        issues, count = [], 0
        for page in ROOT.rglob("*.html"):
            relative = page.relative_to(ROOT)
            if any(part.startswith(".") or part in {"node_modules", "tools", "tests", "docs"} for part in relative.parts):
                continue
            blocks = re.findall(r'''<script\b[^>]*\btype=["']application/ld\+json["'][^>]*>(.*?)</script>''',
                                page.read_text(encoding="utf-8"), re.S | re.I)
            for block in blocks:
                if '"VideoObject"' not in block:
                    continue
                for video in videos_in(json.loads(block)):
                    count += 1
                    description = video.get("description")
                    if not isinstance(description, str) or not description.strip():
                        issues.append(f"{relative}: missing description")
                    if not (video.get("contentUrl") or video.get("embedUrl")):
                        issues.append(f"{relative}: missing contentUrl or embedUrl")
                    if video.get("embedUrl") and not re.fullmatch(r"https://www\.youtube-nocookie\.com/embed/[\w-]{11}", video["embedUrl"]):
                        issues.append(f"{relative}: invalid YouTube player URL")
                    if re.search(r"(?:youtube\.com/watch|youtu\.be/)", video.get("contentUrl", "")):
                        issues.append(f"{relative}: contentUrl points to a watch page, not a video file")
        self.assertGreater(count, 0, "No VideoObject markup found")
        self.assertEqual(len(issues), 0, f"{len(issues)} issues across {count} VideoObjects:\n" + "\n".join(issues[:8]))
        print(f"Validated descriptions and video URLs in all {count} VideoObjects")

    def test_sitemap_preserves_page_modification_date_after_timestamp_refresh(self):
        video = {"published": "2026-10-04T07:45:14-07:00"}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            sitemap = root / "sitemap.xml"
            sitemap.write_text('<urlset xmlns:xhtml="http://www.w3.org/1999/xhtml">'
                               '<!-- youtube:start --><url><loc>https://shenyi.dev/youtube/example/</loc>'
                               '<lastmod>2026-10-25</lastmod></url><!-- youtube:end --></urlset>', encoding="utf-8")
            with patch.object(build, "ROOT", root), patch.object(build, "VIDEOS", [video]):
                build.sitemap({"example": {"en": video}})
            dates = {entry.findtext("loc"): entry.findtext("lastmod") for entry in ET.parse(sitemap).getroot()}
        self.assertEqual(dates["https://shenyi.dev/youtube/example/"], "2026-10-25")
        self.assertEqual(dates["https://shenyi.dev/youtube/"], "2026-10-04")

    def test_build_rejects_missing_timezone_or_invalid_date_before_writing(self):
        for value in ("2026-10-04", "2026-10-04T07:45:14", "2026-02-30T07:45:14Z", ""):
            with self.subTest(published=value), patch.object(build, "VIDEOS", [{"id": "example", "published": value}]):
                with self.assertRaises(ValueError):
                    build.main()

    def test_import_preserves_publication_time_and_timezone(self):
        video_id = "dMeYc5HMps8"
        player = {
            "videoDetails": {
                "channelId": fetch.CHANNEL, "title": "Example video",
                "shortDescription": "Example", "lengthSeconds": "296",
                "keywords": [], "viewCount": "1",
            },
            "microformat": {"playerMicroformatRenderer": {
                "publishDate": "2026-10-04T07:45:14-07:00",
                "uploadDate": "2026-10-03T11:00:00-07:00",
            }},
        }
        responses = {
            f"{fetch.HANDLE}/videos": json.dumps({"videoId": video_id}, separators=(",", ":")),
            f"https://www.youtube.com/watch?v={video_id}": "ytInitialPlayerResponse = " + json.dumps(player) + ";",
        }
        with tempfile.TemporaryDirectory() as directory:
            here = Path(directory)
            (here / "topics.json").write_text(json.dumps({video_id: "example"}), encoding="utf-8")
            with patch.object(fetch, "HERE", here), patch.object(fetch, "get", side_effect=responses.__getitem__):
                fetch.main()
            videos = json.loads((here / "videos.json").read_text(encoding="utf-8"))
        self.assertEqual(videos[0]["published"], "2026-10-04T07:45:14-07:00")


if __name__ == "__main__":
    unittest.main()
