#!/bin/sh
# Render assets/img/og-card.png (1200x630) from _tools/og-card.html with headless Chrome.
# Run from the repository root after python3 _tools/hero_orbit.py.
set -e
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
TMP="$(mktemp -d)"
python3 - "$TMP/card.html" <<'PY'
import sys, re
from pathlib import Path
html = Path("_tools/og-card.html").read_text()
hero = Path("_includes/hero-orbit.svg").read_text()
mark = Path("assets/brand/mark-yellow.svg").read_text()
mark = re.sub(r"<\?xml[^>]*\?>", "", mark)
Path(sys.argv[1]).write_text(html.replace("HERO_SVG", hero).replace("MARK_SVG", mark))
PY
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=4000 \
  --window-size=1200,630 --screenshot="$TMP/card.png" "file://$TMP/card.html" >/dev/null 2>&1
python3 -c "from PIL import Image; Image.open('$TMP/card.png').convert('RGB').save('assets/img/og-card.png', optimize=True)"
rm -rf "$TMP"
echo "wrote assets/img/og-card.png"
