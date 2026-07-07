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

# Center decorative elements - data visualization inspired
cx, cy = width // 2, height // 2 - 100

# Background glow circles
draw.ellipse([(cx - 320, cy - 320), (cx + 320, cy + 320)], fill=None, outline=ACCENT_BLUE, width=2)
draw.ellipse([(cx - 400, cy - 400), (cx + 400, cy + 400)], fill=None, outline=ACCENT_GREEN, width=1)

# Bar chart bars radiating from center
colors = [ACCENT_BLUE, ACCENT_GREEN, ACCENT_GOLD, ACCENT_ORANGE]
bar_width = 30
for i in range(24):
    angle = (i / 24) * 2 * math.pi
    bar_h = 100 + (i % 5) * 30
    x1 = cx + int(120 * math.cos(angle))
    y1 = cy + int(120 * math.sin(angle))
    x2 = cx + int((120 + bar_h) * math.cos(angle))
    y2 = cy + int((120 + bar_h) * math.sin(angle))
    draw.line([(x1, y1), (x2, y2)], fill=colors[i % 4], width=bar_width)

# Small circles at data points
for i in range(12):
    angle = (i / 12) * 2 * math.pi
    r = 380
    px = cx + int(r * math.cos(angle))
    py = cy + int(r * math.sin(angle))
    draw.ellipse([(px - 6, py - 6), (px + 6, py + 6)], fill=colors[i % 4])

# Connecting lines between outer circles
for i in range(12):
    angle1 = (i / 12) * 2 * math.pi
    angle2 = ((i + 2) / 12) * 2 * math.pi
    r = 380
    px1 = cx + int(r * math.cos(angle1))
    py1 = cy + int(r * math.sin(angle1))
    px2 = cx + int(r * math.cos(angle2))
    py2 = cy + int(r * math.sin(angle2))
    draw.line([(px1, py1), (px2, py2)], fill=ACCENT_BLUE, width=1)

# Small accent dots scattered
for i in range(40):
    angle = (i / 40) * 2 * math.pi
    r = 200 + (i % 5) * 50
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
draw.text((80, 280), "Freelancer", fill=WHITE, font=font_title)
draw.text((80, 400), "de Datos", fill=ACCENT_GOLD, font=font_title)

# Subtitle
try:
    font_subtitle = ImageFont.truetype("arial.ttf", 34)
except:
    font_subtitle = ImageFont.load_default()
draw.text((80, 560), "Guia para vivir del analisis de datos", fill=LIGHT_GRAY, font=font_subtitle)
draw.text((80, 600), "como independiente", fill=LIGHT_GRAY, font=font_subtitle)

# Bottom accent bar
draw.rectangle([(0, height - 80), (width, height - 70)], fill=ACCENT_BLUE, width=0)

# Tag at bottom
try:
    font_price = ImageFont.truetype("arialbd.ttf", 28)
except:
    font_price = ImageFont.load_default()
draw.text((80, height - 140), "GUIA COMPLETA", fill=ACCENT_GOLD, font=font_price)

output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cover.jpg")
img.save(output_path, "JPEG", quality=95)
print(f"Portada generada: {output_path}")
