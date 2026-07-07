from PIL import Image, ImageDraw, ImageFont
import os
import math

DARK_BG = "#0D1117"
ACCENT_BLUE = "#58A6FF"
ACCENT_GREEN = "#3FB950"
ACCENT_GOLD = "#D29922"
ACCENT_ORANGE = "#FF7B72"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#8B949E"

width, height = 1600, 2560
img = Image.new("RGB", (width, height), DARK_BG)
draw = ImageDraw.Draw(img)

# Gradient background
for y in range(height):
    progress = y / height
    r = int(13 * (1 - progress) + 22 * progress)
    g = int(17 * (1 - progress) + 27 * progress)
    b = int(23 * (1 - progress) + 34 * progress)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# Center decorative elements - AI / network inspired
cx, cy = width // 2, height // 2 - 100

# Background glow circles
draw.ellipse([(cx - 320, cy - 320), (cx + 320, cy + 320)], fill=None, outline=ACCENT_BLUE, width=2)
draw.ellipse([(cx - 400, cy - 400), (cx + 400, cy + 400)], fill=None, outline=ACCENT_GREEN, width=1)

# Connected network nodes
colors = [ACCENT_BLUE, ACCENT_GREEN, ACCENT_GOLD, ACCENT_ORANGE]
nodes = []
for i in range(8):
    angle = (i / 8) * 2 * math.pi
    r = 180 + (i % 3) * 40
    px = cx + int(r * math.cos(angle))
    py = cy + int(r * math.sin(angle))
    nodes.append((px, py))
    draw.ellipse([(px - 12, py - 12), (px + 12, py + 12)], fill=colors[i % 4])
    draw.ellipse([(px - 6, py - 6), (px + 6, py + 6)], fill=DARK_BG)

# Connection lines between nodes
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        if (j - i) % 3 == 0 or (j - i) % 4 == 0:
            draw.line([nodes[i], nodes[j]], fill=ACCENT_BLUE, width=1)

# Outer ring of smaller nodes
for i in range(16):
    angle = (i / 16) * 2 * math.pi
    r = 380
    px = cx + int(r * math.cos(angle))
    py = cy + int(r * math.sin(angle))
    draw.ellipse([(px - 5, py - 5), (px + 5, py + 5)], fill=colors[i % 4])

# Connecting lines between outer nodes
for i in range(16):
    angle1 = (i / 16) * 2 * math.pi
    angle2 = ((i + 3) / 16) * 2 * math.pi
    r = 380
    px1 = cx + int(r * math.cos(angle1))
    py1 = cy + int(r * math.sin(angle1))
    px2 = cx + int(r * math.cos(angle2))
    py2 = cy + int(r * math.sin(angle2))
    draw.line([(px1, py1), (px2, py2)], fill=ACCENT_GREEN, width=1)

# Small accent dots
for i in range(30):
    angle = (i / 30) * 2 * math.pi
    r = 220 + (i % 5) * 40
    px = cx + int(r * math.cos(angle))
    py = cy + int(r * math.sin(angle))
    draw.ellipse([(px - 3, py - 3), (px + 3, py + 3)], fill=colors[i % 4])

# Author line at top
try:
    font_author = ImageFont.truetype("arial.ttf", 26)
except:
    font_author = ImageFont.load_default()
draw.text((80, 80), "ALEX GOYZUETA DELGADO", fill=LIGHT_GRAY, font=font_author)

# Series
try:
    font_series = ImageFont.truetype("arial.ttf", 22)
except:
    font_series = ImageFont.load_default()
draw.text((80, 120), "DATA & ANALYTICS MASTERY", fill=ACCENT_BLUE, font=font_series)

# Decorative line
draw.rectangle([(80, 170), (350, 174)], fill=ACCENT_GOLD, width=0)

# Title
try:
    font_title = ImageFont.truetype("arialbd.ttf", 110)
except:
    font_title = ImageFont.load_default()
draw.text((80, 280), "Agentes", fill=WHITE, font=font_title)
draw.text((80, 400), "de IA para", fill=ACCENT_GOLD, font=font_title)
draw.text((80, 520), "Pequeñas", fill=WHITE, font=font_title)
draw.text((80, 640), "Empresas", fill=ACCENT_GOLD, font=font_title)

# Subtitle
try:
    font_subtitle = ImageFont.truetype("arial.ttf", 34)
except:
    font_subtitle = ImageFont.load_default()
draw.text((80, 800), "Guia practica para transformar tu negocio", fill=LIGHT_GRAY, font=font_subtitle)
draw.text((80, 840), "con inteligencia artificial sin ser tecnico", fill=LIGHT_GRAY, font=font_subtitle)

# Bottom accent bar
draw.rectangle([(0, height - 80), (width, height - 70)], fill=ACCENT_BLUE, width=0)

# Tag at bottom
try:
    font_price = ImageFont.truetype("arialbd.ttf", 28)
except:
    font_price = ImageFont.load_default()
draw.text((80, height - 140), "GUIA PRACTICA", fill=ACCENT_GOLD, font=font_price)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cover.jpg")
img.save(output_path, "JPEG", quality=95)
print(f"Portada generada: {output_path}")
