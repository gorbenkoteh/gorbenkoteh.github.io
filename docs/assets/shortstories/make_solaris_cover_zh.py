"""Генератор обложки «Аномалий не наблюдал» (SVG 1600x2400, пропорции 2:3)."""
import random
import sys

random.seed(7)
W, H = 1600, 2400
HZ = 1500            # линия горизонта
RS = (440, HZ)       # красное солнце касается горизонта
BS = (1230, 830)     # голубое солнце стоит высоко

out = []
a = out.append

a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
a('''<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1500" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#05070f"/>
    <stop offset="0.45" stop-color="#121427"/>
    <stop offset="0.75" stop-color="#2c1a2e"/>
    <stop offset="0.93" stop-color="#6a2a2a"/>
    <stop offset="1" stop-color="#a5432c"/>
  </linearGradient>
  <radialGradient id="redGlow" cx="440" cy="1500" r="820" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#ff7a3c" stop-opacity="0.55"/>
    <stop offset="0.35" stop-color="#e0452a" stop-opacity="0.18"/>
    <stop offset="1" stop-color="#e0452a" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="redDisc" cx="0.45" cy="0.4" r="0.6">
    <stop offset="0" stop-color="#ffd2a0"/>
    <stop offset="0.5" stop-color="#ff8a4a"/>
    <stop offset="1" stop-color="#d9381f"/>
  </radialGradient>
  <radialGradient id="blueGlow" cx="1230" cy="830" r="460" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#bfe2ff" stop-opacity="0.42"/>
    <stop offset="0.25" stop-color="#6fa8e8" stop-opacity="0.14"/>
    <stop offset="1" stop-color="#6fa8e8" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="sea" x1="0" y1="1500" x2="0" y2="2400" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#2a1418"/>
    <stop offset="0.3" stop-color="#120b10"/>
    <stop offset="1" stop-color="#04050a"/>
  </linearGradient>
  <linearGradient id="mist" x1="0" y1="1380" x2="0" y2="1600" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#ff9a6a" stop-opacity="0"/>
    <stop offset="0.55" stop-color="#ffb08a" stop-opacity="0.16"/>
    <stop offset="1" stop-color="#ff9a6a" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="chalice" x1="0" y1="1160" x2="0" y2="1500" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#cfe6ff" stop-opacity="0.34"/>
    <stop offset="0.5" stop-color="#9ab6e0" stop-opacity="0.14"/>
    <stop offset="1" stop-color="#ff8a5a" stop-opacity="0.30"/>
  </linearGradient>
  <linearGradient id="mimoid" x1="0" y1="1880" x2="0" y2="2400" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#4a3632"/>
    <stop offset="0.12" stop-color="#2c211f"/>
    <stop offset="1" stop-color="#0d0a0a"/>
  </linearGradient>
  <linearGradient id="vignette" x1="0" y1="0" x2="0" y2="2400" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#000" stop-opacity="0.35"/>
    <stop offset="0.2" stop-color="#000" stop-opacity="0"/>
    <stop offset="0.8" stop-color="#000" stop-opacity="0"/>
    <stop offset="1" stop-color="#000" stop-opacity="0.45"/>
  </linearGradient>
  <filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="table" tableValues="0 0.10"/></feComponentTransfer>
  </filter>
  <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
  <clipPath id="aboveHz"><rect x="0" y="0" width="1600" height="1500"/></clipPath>
</defs>''')

# небо, свечения, звёзды
a('<rect width="1600" height="2400" fill="url(#sky)"/>')
for _ in range(140):
    x, y = random.uniform(30, 1570), random.uniform(20, 1150)
    r = random.choice([0.8, 1.0, 1.2, 1.6, 2.0])
    op = random.uniform(0.25, 0.85) * (1 - y / 1500)
    a(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#dfe8ff" opacity="{op:.2f}"/>')
a('<rect width="1600" height="1500" fill="url(#blueGlow)"/>')
a('<rect width="1600" height="2400" fill="url(#redGlow)"/>')

# голубое солнце — маленькое, высокое, холодное
a(f'<circle cx="{BS[0]}" cy="{BS[1]}" r="70" fill="#bfe2ff" opacity="0.25" filter="url(#soft)"/>')
a(f'<circle cx="{BS[0]}" cy="{BS[1]}" r="38" fill="#eef7ff"/>')

# красное солнце — касается горизонта
a(f'<g clip-path="url(#aboveHz)"><circle cx="{RS[0]}" cy="{RS[1]+30}" r="150" fill="url(#redDisc)"/></g>')

# чаша-формация на горизонте («рука, раскрытая ладонью вверх»)
cx = 1080
a('<g>')
a(f'<path d="M {cx-38},1500 C {cx-36},1420 {cx-30},1360 {cx-46},1320 '
  f'C {cx-90},1260 {cx-170},1230 {cx-205},1196 '
  f'C {cx-120},1222 {cx+120},1222 {cx+205},1196 '
  f'C {cx+170},1230 {cx+90},1260 {cx+46},1320 '
  f'C {cx+30},1360 {cx+36},1420 {cx+38},1500 Z" '
  'fill="url(#chalice)" stroke="#e6f0ff" stroke-opacity="0.45" stroke-width="2"/>')
a(f'<ellipse cx="{cx}" cy="1196" rx="205" ry="24" fill="#d8e9ff" fill-opacity="0.12" '
  'stroke="#eef5ff" stroke-opacity="0.55" stroke-width="2"/>')
# внутренние «прожилки» — вещество то отражает небо, то пропускает его
for dx in (-120, -60, 0, 60, 120):
    a(f'<path d="M {cx+dx*0.25:.0f},1490 C {cx+dx*0.2:.0f},1380 {cx+dx*0.6:.0f},1270 {cx+dx:.0f},1205" '
      'fill="none" stroke="#e6f0ff" stroke-opacity="0.13" stroke-width="1.5"/>')
a('</g>')

# дымка над горизонтом
a('<rect x="0" y="1380" width="1600" height="220" fill="url(#mist)"/>')

# океан
a('<rect x="0" y="1500" width="1600" height="900" fill="url(#sea)"/>')
a('<rect x="0" y="1499" width="1600" height="2" fill="#ffb48a" opacity="0.35"/>')
# дорожка красного солнца
y = 1504
while y < 1990:
    t = (y - HZ) / 490
    w = 70 + t * 520 * random.uniform(0.5, 1.1)
    off = random.uniform(-0.25, 0.25) * w
    op = (1 - t) ** 1.6 * random.uniform(0.35, 0.8)
    hgt = 1.5 + t * 4
    col = "#ffc08a" if t < 0.25 else "#ff7a45"
    a(f'<rect x="{RS[0]-w/2+off:.0f}" y="{y:.0f}" width="{w:.0f}" height="{hgt:.1f}" rx="{hgt/2:.1f}" fill="{col}" opacity="{op:.2f}"/>')
    y += 5 + t * 16
# отражение чаши
for i in range(14):
    yy = 1508 + i * 9
    w = random.uniform(30, 120) * (1 - i / 18)
    a(f'<rect x="{cx-w/2+random.uniform(-10,10):.0f}" y="{yy}" width="{w:.0f}" height="1.5" fill="#cfe2ff" opacity="{0.22*(1-i/14):.2f}"/>')
# фосфоресцирующие прожилки
for _ in range(9):
    y0 = random.uniform(1560, 1860)
    x0 = random.uniform(700, 1500)
    L = random.uniform(120, 320)
    a(f'<path d="M {x0:.0f},{y0:.0f} q {L/4:.0f},{random.uniform(-6,6):.0f} {L/2:.0f},0 t {L/2:.0f},0" '
      f'fill="none" stroke="#4fc3c8" stroke-width="1.6" opacity="{random.uniform(0.12,0.3):.2f}"/>')

# мимоид — передний план
contour = 'M 0,1950 C 260,1915 420,1912 560,1912 C 760,1912 980,1934 1220,1962 C 1400,1984 1520,2002 1600,2012'
a(f'<path d="{contour} L 1600,2400 L 0,2400 Z" fill="url(#mimoid)"/>')
a(f'<path d="{contour}" fill="none" stroke="#ff8a55" stroke-opacity="0.55" stroke-width="3"/>')
for i in range(7):
    yy = 1990 + i * 48
    a(f'<path d="M {random.uniform(-80,200):.0f},{yy+40:.0f} C 500,{yy:.0f} 1000,{yy+30:.0f} 1700,{yy+70:.0f}" '
      f'fill="none" stroke="#a06a55" stroke-opacity="{0.10-i*0.011:.3f}" stroke-width="2"/>')

# фигуры: взрослый и мальчик, держатся за руки; ноги на y≈1912
FY = 1912
# две тени: от красного солнца — длинная, к зрителю; от голубого — короткая, влево
a(f'<path d="M 470,{FY} L 534,{FY} L 585,2140 L 415,2140 Z" fill="#000" opacity="0.32"/>')
a(f'<path d="M 470,{FY} L 534,{FY} L 420,1990 L 340,1990 Z" fill="#000" opacity="0.22"/>')
sil = '#080607'
rim = 'stroke="#ff9a66" stroke-opacity="0.75" stroke-width="2.2" stroke-linejoin="round"'
# взрослый (x≈480, рост ≈170)
a(f'<circle cx="480" cy="1752" r="13.5" fill="{sil}" {rim}/>')
a(f'<path d="M 463,1772 Q 480,1764 497,1772 L 502,1838 L 496,1912 L 485,1912 L 481,1848 L 477,1912 L 466,1912 L 460,1838 Z" fill="{sil}" {rim}/>')
a(f'<path d="M 464,1776 L 456,1846" stroke="{sil}" stroke-width="8" stroke-linecap="round"/>')
a(f'<path d="M 497,1776 L 516,1858" stroke="{sil}" stroke-width="8" stroke-linecap="round"/>')
# мальчик (x≈540, рост ≈105)
a(f'<circle cx="542" cy="1820" r="10" fill="{sil}" {rim}/>')
a(f'<path d="M 531,1834 Q 542,1829 553,1834 L 556,1874 L 552,1912 L 545,1912 L 542,1882 L 539,1912 L 532,1912 L 528,1874 Z" fill="{sil}" {rim}/>')
a(f'<path d="M 531,1838 L 518,1860" stroke="{sil}" stroke-width="6" stroke-linecap="round"/>')
a(f'<path d="M 553,1838 L 559,1868" stroke="{sil}" stroke-width="6" stroke-linecap="round"/>')

# зерно и виньетка
a('<rect width="1600" height="2400" filter="url(#grain)"/>')
a('<rect width="1600" height="2400" fill="url(#vignette)"/>')

# типографика
a('''<g text-anchor="middle">
  <text x="800" y="238" font-family="Droid Sans Fallback, sans-serif" font-size="40" letter-spacing="22" fill="#8fb6dc">索拉里斯</text>
  <rect x="740" y="276" width="120" height="1.5" fill="#8fb6dc" opacity="0.6"/>
  <text x="800" y="510" font-family="Noto Serif CJK SC, Droid Sans Fallback, serif" font-size="220" letter-spacing="24" fill="#f1e7d8">未见异常</text>
  <text x="800" y="2208" font-family="Noto Serif CJK SC, Droid Sans Fallback, serif" font-size="44" letter-spacing="3" fill="#d8c4b0">斯坦尼斯瓦夫·莱姆小说续篇</text>
</g>
<g font-family="Droid Sans Fallback, sans-serif" font-size="25" fill="#cdb9a6" opacity="0.55" text-anchor="middle">
  <text x="800" y="2316">异常活动：<tspan fill="#e0cbb8">未发现</tspan></text>
  <rect x="825" y="2326" width="75" height="1.2"/>
</g>''')
a('</svg>')

with open(sys.argv[1], "w", encoding="utf-8") as f:
    f.write("\n".join(out))
