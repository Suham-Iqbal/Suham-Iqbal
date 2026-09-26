import urllib.request
import base64

# Fetch avatar
url = "https://github.com/Suham-Iqbal.png"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        img_data = response.read()
        b64_img = base64.b64encode(img_data).decode('utf-8')
        img_src = f"data:image/png;base64,{b64_img}"
except Exception as e:
    # Fallback if download fails
    img_src = url

svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 550" width="100%" height="100%">
  <style>
    .title {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 14px; fill: #8b949e; }}
    .text-cyan {{ fill: #58d1eb; font-family: 'Courier New', monospace; font-size: 14px; font-weight: bold; }}
    .text-gray {{ fill: #8b949e; font-family: 'Courier New', monospace; font-size: 12px; }}
    .text-white {{ fill: #c9d1d9; font-family: 'Courier New', monospace; font-size: 14px; }}
    .key {{ fill: #8b949e; font-family: 'Courier New', monospace; font-size: 14px; }}
    .value {{ fill: #c9d1d9; font-family: 'Courier New', monospace; font-size: 14px; }}
    .border-line {{ stroke: #30363d; stroke-width: 1; }}
    .box-corner {{ stroke: #30363d; stroke-width: 2; fill: none; }}
  </style>
  
  <!-- Window Background -->
  <rect x="10" y="10" width="980" height="530" rx="10" fill="#0d1117" class="border-line" />
  
  <!-- Mac Buttons -->
  <circle cx="35" cy="30" r="6" fill="#ff5f56" />
  <circle cx="55" cy="30" r="6" fill="#ffbd2e" />
  <circle cx="75" cy="30" r="6" fill="#27c93f" />
  
  <!-- Title -->
  <text x="500" y="34" class="title" text-anchor="middle">profile.sh --live</text>
  
  <!-- Top Divider -->
  <line x1="10" y1="50" x2="990" y2="50" class="border-line" />
  
  <!-- VISUAL.MAP Section (Left) -->
  <rect x="30" y="70" width="400" height="450" rx="5" fill="#010409" class="border-line" />
  <text x="45" y="95" class="text-cyan">VISUAL.MAP</text>
  <text x="415" y="95" class="text-gray" text-anchor="end">300x340 / 32-BIT</text>
  
  <!-- Corner Accents -->
  <path d="M 45 125 L 45 115 L 55 115" class="box-corner" />
  <path d="M 405 115 L 415 115 L 415 125" class="box-corner" />
  <path d="M 45 480 L 45 490 L 55 490" class="box-corner" />
  <path d="M 405 490 L 415 490 L 415 480" class="box-corner" />
  
  <!-- Avatar -->
  <clipPath id="avatarClip">
    <rect x="65" y="130" width="330" height="330" rx="10" />
  </clipPath>
  <image x="65" y="130" width="330" height="330" preserveAspectRatio="xMidYMid slice" href="{img_src}" clip-path="url(#avatarClip)" />
  
  <text x="45" y="505" class="text-gray">PTS 18000 · FS/SERPENTINE</text>
  
  <!-- SYSTEM.INFO Section (Right) -->
  <rect x="450" y="70" width="520" height="450" rx="5" fill="#010409" class="border-line" />
  <text x="470" y="95" class="text-cyan">SYSTEM.INFO</text>
  
  <circle cx="810" cy="91" r="5" fill="#ff5f56" />
  <text x="825" y="95" class="text-gray">LIVE</text>
  
  <rect x="855" y="80" width="100" height="20" rx="10" fill="#1f6feb" opacity="0.3" />
  <text x="905" y="94" class="text-cyan" text-anchor="middle" font-size="12">@Suham-Iqbal</text>
  
  <g transform="translate(470, 140)">
    <text x="0" y="0" class="key">Subject</text><text x="480" y="0" class="value" text-anchor="end">Suham Iqbal Khan</text>
    <text x="0" y="28" class="key">Role</text><text x="480" y="28" class="value" text-anchor="end">Software Engineer | AI</text>
    <text x="0" y="56" class="key">Origin</text><text x="480" y="56" class="value" text-anchor="end">Pakistan</text>
    <text x="0" y="84" class="key">Education</text><text x="480" y="84" class="value" text-anchor="end">BS Computer Science</text>
    <text x="0" y="112" class="key">Status</text><text x="480" y="112" class="value" text-anchor="end">Building + Shipping</text>
    <text x="0" y="140" class="key">ToolChain</text><text x="480" y="140" class="value" text-anchor="end">VS Code • Cursor • Git</text>
    <text x="0" y="168" class="key">Core.Lang</text><text x="480" y="168" class="value" text-anchor="end">TypeScript • Python • Rust</text>
    <text x="0" y="196" class="key">Core.Frontend</text><text x="480" y="196" class="value" text-anchor="end">React • Next.js • Tailwind</text>
    <text x="0" y="224" class="key">Core.Backend</text><text x="480" y="224" class="value" text-anchor="end">Node.js • FastAPI</text>
    <text x="0" y="252" class="key">Core.Database</text><text x="480" y="252" class="value" text-anchor="end">MongoDB • PostgreSQL</text>
    <text x="0" y="280" class="key">Core.Infra</text><text x="480" y="280" class="value" text-anchor="end">Docker • Vercel • Cloudflare</text>
    <text x="0" y="308" class="key">Grid.Mail</text><text x="480" y="308" class="value" text-anchor="end">suham.iqbal7860@gmail.com</text>
    <text x="0" y="336" class="key">Grid.LinkedIn</text><text x="480" y="336" class="value" text-anchor="end">/in/suhamiqbalkhan</text>
  </g>
  
  <circle cx="475" cy="501" r="3" fill="#27c93f" />
  <text x="485" y="505" class="text-cyan" font-size="12">ALL SYSTEMS NOMINAL</text>
  <text x="970" y="505" class="text-gray" text-anchor="end">UTC+5</text>
</svg>
"""

with open("terminal.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)
print("Created terminal.svg successfully.")
