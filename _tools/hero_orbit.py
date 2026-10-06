"""Write _includes/hero-orbit.svg, the homepage hero artwork.

Star positions and the orbit ellipse come from hero-geom.json, measured from the
original hero render. Run from the repository root: python3 _tools/hero_orbit.py
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
geom = json.loads((ROOT / "_tools" / "hero-geom.json").read_text())

W, H = 1920, 880
PLANET_CX, PLANET_CY, PLANET_R = 960, 2372, 1821
GROUND = (806, 556)
SAT = (1596, 461)
ocx, ocy, orx, ory, oang = geom["orbit"]

stars = []
for x, y, size, bright in geom["stars"]:
    r = max(0.9, math.sqrt(size / math.pi))
    o = min(1.0, max(0.25, (bright - 40) / 90))
    stars.append(f'<circle cx="{x:g}" cy="{y:g}" r="{r:.1f}" opacity="{o:.2f}"/>')

uplink_len = math.dist(GROUND, SAT)

svg = f'''<svg class="ts-orbit" viewBox="0 0 {W} {H}" preserveAspectRatio="xMaxYMid slice" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" style="--uplink: {uplink_len:.0f}">
  <g fill="#bdb8ae">{"".join(stars)}</g>
  <circle cx="{PLANET_CX}" cy="{PLANET_CY}" r="{PLANET_R}" fill="#1f1e1b" stroke="#615f5b" stroke-width="3"/>
  <ellipse cx="{ocx:.1f}" cy="{ocy:.1f}" rx="{orx:.1f}" ry="{ory:.1f}" transform="rotate({oang:.1f} {ocx:.1f} {ocy:.1f})" fill="none" stroke="#ffcb24" stroke-opacity=".45" stroke-width="6" stroke-linecap="round" stroke-dasharray="0 57"/>
  <line class="ts-orbit__uplink" x1="{GROUND[0]}" y1="{GROUND[1]}" x2="{SAT[0]}" y2="{SAT[1]}" stroke="#ffcb24" stroke-opacity=".55" stroke-width="2.5" stroke-dasharray="16 44"/>
  <line class="ts-orbit__packet" x1="{GROUND[0]}" y1="{GROUND[1]}" x2="{SAT[0]}" y2="{SAT[1]}" stroke="#ffcb24" stroke-width="4" stroke-linecap="round"/>
  <circle class="ts-orbit__pulse" cx="{SAT[0]}" cy="{SAT[1]}" r="18" fill="none" stroke="#ffcb24" stroke-width="2.5"/>
  <circle cx="{SAT[0]}" cy="{SAT[1]}" r="18" fill="none" stroke="#ffcb24" stroke-opacity=".6" stroke-width="2.5"/>
  <circle class="ts-orbit__sat" cx="{SAT[0]}" cy="{SAT[1]}" r="10" fill="#ffcb24"/>
  <circle cx="{GROUND[0]}" cy="{GROUND[1]}" r="7" fill="#d8d4cc"/>
</svg>
'''
(ROOT / "_includes" / "hero-orbit.svg").write_text(svg)
print(f"wrote _includes/hero-orbit.svg ({len(svg)} bytes), uplink {uplink_len:.0f}px")
