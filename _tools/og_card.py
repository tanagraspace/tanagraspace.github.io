"""Render 1200x630 share cards in the Tanagra Space brand with headless Chrome.

Home card (the hero artwork with the mark and wordmark):
    python3 _tools/og_card.py --out assets/img/og-card.png

Feature card (eyebrow, title, and tagline on the left, framed art on the right):
    python3 _tools/og_card.py --out card.png --eyebrow "Open source" \
        --title "Boresight" --tagline "One line." --art path/to/art.png

Run from the repository root after python3 _tools/hero_orbit.py. Set CHROME to
override the Chrome binary.
"""
import argparse
import base64
import html
import mimetypes
import os
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
FONTS = "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500&family=Nunito+Sans:opsz,wght@6..12,300..800&display=block"

BASE_CSS = """
html, body { margin: 0; width: 1200px; height: 630px; overflow: hidden; background: #161616; }
.card { position: relative; width: 1200px; height: 630px; isolation: isolate; font-family: "Nunito Sans", sans-serif; color: #fff; }
.ts-orbit { position: absolute; inset: 0; width: 100%; height: 100%; z-index: -2; }
.ts-orbit__packet, .ts-orbit__pulse { display: none; }
.url { position: absolute; left: 88px; bottom: 56px; font-family: "IBM Plex Mono", monospace; font-weight: 500;
  font-size: 20px; letter-spacing: .12em; color: #ffcb24; text-transform: uppercase; }
"""

HOME_CSS = """
.card::before { content: ""; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(90deg, rgba(22,22,22,.95) 0%, rgba(22,22,22,.7) 42%, rgba(22,22,22,0) 70%); }
.copy { position: absolute; left: 88px; top: 50%; transform: translateY(-54%); }
.brand { display: flex; align-items: center; gap: 26px; }
.brand svg { width: 58px; height: auto; }
.brand h1 { margin: 0; font-weight: 300; font-size: 84px; letter-spacing: .005em; line-height: 1; }
.tag { margin: 34px 0 0; color: #d9d4ca; font-size: 34px; line-height: 1.3; max-width: 640px; }
"""

FEATURE_CSS = """
.card::before { content: ""; position: absolute; inset: 0; z-index: -1; background: rgba(22,22,22,.82); }
.brand { position: absolute; left: 88px; top: 60px; display: flex; align-items: center; gap: 14px; }
.brand svg { width: 26px; height: auto; }
.brand span { font-weight: 300; font-size: 30px; }
.copy { position: absolute; left: 88px; top: 50%; transform: translateY(-50%); width: 520px; }
.eyebrow { margin: 0 0 18px; font-family: "IBM Plex Mono", monospace; font-weight: 500; font-size: 20px;
  letter-spacing: .12em; text-transform: uppercase; color: #ffcb24; }
.copy h1 { margin: 0; font-weight: 800; font-size: 58px; line-height: 1.05; letter-spacing: -.015em; }
.tag { margin: 22px 0 0; color: #d9d4ca; font-size: 26px; line-height: 1.35; }
.art { position: absolute; right: 72px; top: 50%; transform: translateY(-50%); width: 480px;
  border-radius: 18px; overflow: hidden; border: 1px solid #3a3a3a; box-shadow: 0 24px 60px rgba(0,0,0,.55); }
.art img { display: block; width: 100%; height: auto; }
"""


def svg(path):
    return re.sub(r"<\?xml[^>]*\?>", "", (ROOT / path).read_text())


def data_uri(path):
    mime = mimetypes.guess_type(str(path))[0] or "image/png"
    return f"data:{mime};base64,{base64.b64encode(Path(path).read_bytes()).decode()}"


def page(args):
    hero = svg("_includes/hero-orbit.svg")
    mark = svg("assets/brand/mark-yellow.svg")
    esc = html.escape
    if args.title is None:
        css = HOME_CSS
        body = f"""<div class="copy"><div class="brand">{mark}<h1>Tanagra Space</h1></div>
  <p class="tag">{esc(args.tagline)}</p></div>"""
    else:
        css = FEATURE_CSS
        body = f"""<div class="brand">{mark}<span>Tanagra Space</span></div>
<div class="copy"><p class="eyebrow">{esc(args.eyebrow)}</p><h1>{esc(args.title)}</h1><p class="tag">{esc(args.tagline)}</p></div>
<div class="art"><img src="{data_uri(args.art)}" alt=""></div>"""
    return f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="{FONTS}">
<style>{BASE_CSS}{css}</style></head><body><div class="card">{hero}{body}
<div class="url">{esc(args.url_label)}</div></div></body></html>"""


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--out", required=True)
    p.add_argument("--title", help="feature card title; omit for the home card")
    p.add_argument("--eyebrow", default="")
    p.add_argument("--tagline", default="Launching artificial intelligence into orbit.")
    p.add_argument("--art", help="image shown on the right of a feature card")
    p.add_argument("--url-label", default="tanagraspace.com")
    args = p.parse_args()
    if args.title is not None and not args.art:
        p.error("--art is required with --title")
    with tempfile.TemporaryDirectory() as tmp:
        src, shot = Path(tmp) / "card.html", Path(tmp) / "card.png"
        src.write_text(page(args))
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=4000",
                        "--window-size=1200,630", f"--screenshot={shot}", src.as_uri()],
                       check=True, capture_output=True, timeout=60)
        from PIL import Image
        Image.open(shot).convert("RGB").save(args.out, optimize=True)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
