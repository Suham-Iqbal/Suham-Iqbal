import urllib.request
import base64
from io import BytesIO
import subprocess
import sys

# Ensure PIL is installed
try:
    from PIL import Image, ImageOps
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image, ImageOps

# Download image
url = "https://github.com/Suham-Iqbal.png"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
img_data = response.read()

# Process with PIL
img = Image.open(BytesIO(img_data)).convert("RGBA")

# Resize
img = img.resize((330, 330), Image.Resampling.LANCZOS)

# Create white background to remove transparency issues
bg = Image.new("RGBA", img.size, (255, 255, 255, 255))
bg.paste(img, mask=img)
img = bg.convert("L")  # Grayscale

# Increase contrast to make the dither look punchy
img = ImageOps.autocontrast(img, cutoff=2)

# Convert to 1-bit dithered using Floyd-Steinberg
img_1bit = img.convert("1", dither=Image.Dither.FLOYDSTEINBERG)

# Colorize
img_color = img_1bit.convert("RGBA")
data = img_color.getdata()

new_data = []
# #a371f7 is a beautiful Hacker Purple (163, 113, 247)
purple = (163, 113, 247, 255)
# #58d1eb is Cyan (88, 209, 235)
cyan = (88, 209, 235, 255)

for item in data:
    if item[0] == 0:
        # Black pixel (dark areas of photo) -> Purple Dither Dots
        new_data.append(purple)
    else:
        # White pixel (bright areas / background) -> Transparent
        new_data.append((0, 0, 0, 0))
        
img_color.putdata(new_data)

# Save to base64
buffer = BytesIO()
img_color.save(buffer, format="PNG")
b64_img = base64.b64encode(buffer.getvalue()).decode('utf-8')
dithered_img_src = f"data:image/png;base64,{b64_img}"

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
    
    @keyframes pulse-anim {{
        0% {{ opacity: 1; }}
        50% {{ opacity: 0.5; }}
        100% {{ opacity: 1; }}
    }}
    .dithered-avatar {{
        animation: pulse-anim 4s infinite ease-in-out;
    }}
  </style>
  
  <!-- Window Background -->
  <rect x="10" y="10" width="980" height="530" rx="10" fill="#0d1117" class="border-line" />
  
  <!-- MAC BUTTONS REMOVED AS REQUESTED -->
  
  <!-- Title -->
  <text x="500" y="34" class="title" text-anchor="middle">profile.sh --live</text>
  
  <!-- Top Divider -->
  <line x1="10" y1="50" x2="990" y2="50" class="border-line" />
  
  <!-- VISUAL.MAP Section (Left) -->
  <rect x="30" y="70" width="400" height="450" rx="5" fill="#010409" class="border-line" />
  <text x="45" y="95" class="text-cyan">VISUAL.MAP</text>
  <text x="415" y="95" class="text-gray" text-anchor="end">300x340 / 1-BIT</text>
  
  <!-- Corner Accents -->
  <path d="M 45 125 L 45 115 L 55 115" class="box-corner" />
  <path d="M 405 115 L 415 115 L 415 125" class="box-corner" />
  <path d="M 45 480 L 45 490 L 55 490" class="box-corner" />
  <path d="M 405 490 L 415 490 L 415 480" class="box-corner" />
  
  <!-- The Dithered Stylized Avatar -->
  <!-- We removed the actual color photo entirely as requested -->
  <clipPath id="avatarClip">
    <rect x="65" y="130" width="330" height="330" rx="10" />
  </clipPath>
  <image class="dithered-avatar" x="65" y="130" width="330" height="330" preserveAspectRatio="xMidYMid slice" href="{dithered_img_src}" clip-path="url(#avatarClip)" />
  
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
print("Updated terminal.svg successfully with true PIL dithering.")
