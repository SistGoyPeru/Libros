from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, random

W, H = 1600, 2560
CX, CY = W // 2, H // 2
FONT_DIR = "C:\\Windows\\Fonts"
OUTPUT_DIR = r"C:\Users\alexg\OneDrive\Alex_2026\libros epub\print_Sigo_Aqui"

img = Image.new("RGB", (W, H), (20, 20, 30))
draw = ImageDraw.Draw(img)

# --- Gradient background ---
for y in range(H):
    ratio = y / H
    r = int(15 + ratio * 40)
    g = int(15 + ratio * 25)
    b = int(30 - ratio * 15)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# --- Warm circle accent (like an orange / sunset) ---
circle_center = (CX, CY - 200)
circle_radius = 500
for r in range(circle_radius, 0, -2):
    ratio = r / circle_radius
    alpha = int(20 * (1 - ratio))
    if alpha <= 0:
        continue
    color_r = int(200 + 55 * (1 - ratio))
    color_g = int(120 + 40 * (1 - ratio))
    color_b = int(30 + 20 * (1 - ratio))
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.ellipse(
        [circle_center[0] - r, circle_center[1] - r, circle_center[0] + r, circle_center[1] + r],
        fill=(color_r, color_g, color_b, alpha),
    )
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

# --- Subtle code lines in background ---
consola = ImageFont.truetype(os.path.join(FONT_DIR, "consola.ttf"), 20)
code_lines = [
    "import pandas as pd",
    "import numpy as np",
    "datos = pd.read_csv('vida.csv')",
    "print('Sigo Aqui')",
    "for ciudad in ['Valencia', 'Barcelona', 'Asturias']:",
    "    print(f'Estuve en {ciudad}')",
    "medicamentos_mes = 300",
    "euros_ahorrados = 0",
    "while esperanza > 0:",
    "    seguir()",
    "naranjas_amargas = True",
    "codigo_dulce = False",
    "if miedo < 0:",
    "    print('Bienvenido a Espana')",
    "print('Fin del viaje')",
]

random.seed(42)
for line in code_lines:
    x = random.randint(40, W - 400)
    y = random.randint(80, H - 80)
    draw.text((x, y), line, fill=(60, 60, 80), font=consola)

# --- Title ---
try:
    font_title = ImageFont.truetype(os.path.join(FONT_DIR, "consolab.ttf"), 100)
except:
    font_title = ImageFont.truetype(os.path.join(FONT_DIR, "consola.ttf"), 100)

try:
    font_sub = ImageFont.truetype(os.path.join(FONT_DIR, "calibri.ttf"), 36)
except:
    font_sub = ImageFont.truetype(os.path.join(FONT_DIR, "ariali.ttf"), 36)

try:
    font_author = ImageFont.truetype(os.path.join(FONT_DIR, "calibri.ttf"), 30)
except:
    font_author = ImageFont.truetype(os.path.join(FONT_DIR, "ariali.ttf"), 30)

title = 'print("Sigo Aquí")'
sub = "El viaje de un informático sin papeles"
sub2 = "que cruzó España para salvar a quien amaba"
author = "Alex Goyzueta Delgado"

# Title shadow
for dx, dy in [(4, 4), (5, 5)]:
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (W - tw) // 2 + dx
    ty = CY - 280 + dy
    draw.text((tx, ty), title, fill=(0, 0, 0), font=font_title)

# Title main
bbox = draw.textbbox((0, 0), title, font=font_title)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
tx = (W - tw) // 2
ty = CY - 280
draw.text((tx, ty), title, fill=(230, 190, 70), font=font_title)

# Terminal cursor
cursor_x = tx + tw + 8
cursor_y = ty + 4
draw.rectangle([cursor_x, cursor_y, cursor_x + 18, cursor_y + th - 8], fill=(230, 190, 70))

# Subtitle line 1
bbox = draw.textbbox((0, 0), sub, font=font_sub)
tw = bbox[2] - bbox[0]
tx = (W - tw) // 2
ty = CY - 120
draw.text((tx, ty), sub, fill=(200, 200, 210), font=font_sub)

# Subtitle line 2
bbox = draw.textbbox((0, 0), sub2, font=font_sub)
tw = bbox[2] - bbox[0]
tx = (W - tw) // 2
ty = CY - 70
draw.text((tx, ty), sub2, fill=(200, 200, 210), font=font_sub)

# Author
bbox = draw.textbbox((0, 0), author, font=font_author)
tw = bbox[2] - bbox[0]
tx = (W - tw) // 2
ty = H - 120
draw.text((tx, ty), author, fill=(160, 160, 170), font=font_author)

# --- Decorative bottom line ---
draw.rectangle([CX - 120, H - 150, CX + 120, H - 147], fill=(230, 190, 70))

# --- Save ---
output_path = os.path.join(OUTPUT_DIR, "cover_pretty.jpg")
img.save(output_path, "JPEG", quality=95)
print(f"Cover saved: {output_path}")
print(f"Size: {os.path.getsize(output_path) // 1024} KB")
