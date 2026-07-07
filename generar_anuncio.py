from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(BASE, "distribucion")

W, H = 2000, 1200  # 16:9 aspect ratio for social media

# Books info
books = [
    ("fundamentos_analista_datos", "Los Fundamentos\ndel Analista de Datos"),
    ("python_data_cloud", "Python para Datos\ny tu Primer Data\nWarehouse Cloud"),
    ("business_intelligence_bi", "Business Intelligence\ny Modelado de Datos"),
    ("ingenieria_datos_moderna", "Ingenier\u00eda de\nDatos Moderna"),
    ("big_data_ml_ia", "Big Data,\nML e IA"),
]

# Create canvas
img = Image.new("RGB", (W, H), "#0D1117")
draw = ImageDraw.Draw(img)

# Gradient background
for y in range(H):
    progress = y / H
    r = int(13 * (1 - progress) + 30 * progress)
    g = int(17 * (1 - progress) + 40 * progress)
    b = int(23 * (1 - progress) + 60 * progress)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Abstract grid pattern
for x in range(0, W, 60):
    draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 2), width=1)
for y in range(0, H, 60):
    draw.line([(0, y), (W, y)], fill=(255, 255, 255, 2), width=1)

# Glowing accent circles
draw.ellipse([(-100, -100), (200, 200)], fill=(88, 166, 255, 60), outline=None)
draw.ellipse([(1700, 800), (2100, 1200)], fill=(188, 140, 255, 50), outline=None)
draw.ellipse([(800, -50), (1000, 150)], fill=(63, 185, 80, 40), outline=None)

# Top badge
try:
    font_badge = ImageFont.truetype("arialbd.ttf", 28)
except:
    font_badge = ImageFont.load_default()

badge_x, badge_y = 60, 50
draw.rounded_rectangle([(badge_x, badge_y), (badge_x + 400, badge_y + 55)], radius=28, fill="#BC8CFF", outline=None)
draw.text((badge_x + 30, badge_y + 12), "COLECCI\u00d3N COMPLETA", fill="#FFFFFF", font=font_badge)

# Main headline
try:
    font_headline = ImageFont.truetype("arialbd.ttf", 72)
    font_sub = ImageFont.truetype("arial.ttf", 32)
    font_body = ImageFont.truetype("arial.ttf", 24)
    font_book = ImageFont.truetype("arialbd.ttf", 18)
    font_book_num = ImageFont.truetype("arial.ttf", 22)
    font_cta = ImageFont.truetype("arialbd.ttf", 36)
    font_price = ImageFont.truetype("arial.ttf", 26)
    font_tag = ImageFont.truetype("arial.ttf", 20)
except:
    font_headline = ImageFont.load_default()
    font_sub = ImageFont.load_default()
    font_body = ImageFont.load_default()
    font_book = ImageFont.load_default()
    font_book_num = ImageFont.load_default()
    font_cta = ImageFont.load_default()
    font_price = ImageFont.load_default()
    font_tag = ImageFont.load_default()

draw.text((60, 140), "DATA & ANALYTICS", fill="#58A6FF", font=font_headline)
draw.text((60, 210), "MASTERY", fill="#FFFFFF", font=font_headline)

# Subheadline
draw.text((60, 295), "La colecci\u00f3n definitiva para dominar el ecosistema de datos completo", fill="#8B949E", font=font_sub)

# Tags line
tags = ["SQL", "Python", "Power BI", "dbt", "Airflow", "PySpark", "ML", "IA"]
tag_x = 60
tag_y = 360
for tag in tags:
    tw = draw.textlength(tag, font=font_tag) + 30
    draw.rounded_rectangle([(tag_x, tag_y), (tag_x + tw, tag_y + 35)], radius=18, fill="#161B22", outline="#58A6FF")
    draw.text((tag_x + 15, tag_y + 7), tag, fill="#58A6FF", font=font_tag)
    tag_x += tw + 12

# Book covers row
cover_w = 220
cover_h = 350
gap = 18
total_w = 5 * cover_w + 4 * gap
start_x = (W - total_w) // 2
cover_y = 440

loaded = []
for folder, _ in books:
    path = os.path.join(DIST, folder, "cover.jpg")
    try:
        c = Image.open(path).resize((cover_w, cover_h), Image.LANCZOS)
        loaded.append(c)
    except:
        loaded.append(None)

for i, (fld, title) in enumerate(books):
    cx = start_x + i * (cover_w + gap)

    # Card shadow
    draw.rounded_rectangle([(cx + 4, cover_y + 4), (cx + cover_w + 4, cover_y + cover_h + 4)],
                           radius=10, fill=(0, 0, 0, 100), outline=None)

    # Book cover
    if loaded[i]:
        paste_x = cx
        paste_y = cover_y
        img.paste(loaded[i], (int(paste_x), int(paste_y)))

    # Book number
    num_cx = cx + cover_w // 2
    draw.ellipse([(num_cx - 18, cover_y + cover_h + 14), (num_cx + 18, cover_y + cover_h + 50)],
                 fill="#BC8CFF", outline=None)
    draw.text((num_cx - 7, cover_y + cover_h + 20), str(i + 1), fill="#0D1117", font=font_book_num)

    # Book title below
    title_y = cover_y + cover_h + 60
    lines = title.split("\n")
    for j, line in enumerate(lines):
        tw = draw.textlength(line, font=font_book)
        draw.text((cx + (cover_w - tw) // 2, title_y + j * 24), line, fill="#E6EDF3", font=font_book)

# Bundle section
bundle_y = 950
draw.rounded_rectangle([(120, bundle_y), (W - 120, bundle_y + 200)], radius=18, fill="#161B22", outline="#3FB950")

# Bundle pills
pills = [
    "5 LIBROS", "1.50\u20ac c/u", "DESCARGAS DIGITALES", "APRENDE HACIENDO", "DATASET TECHSTORE"
]
pill_x = 180
pill_y_bundle = bundle_y + 20
for pill in pills:
    pw = draw.textlength(pill, font=font_tag) + 30
    draw.rounded_rectangle([(pill_x, pill_y_bundle), (pill_x + pw, pill_y_bundle + 32)], radius=16, fill="#3FB950", outline=None)
    draw.text((pill_x + 15, pill_y_bundle + 6), pill, fill="#0D1117", font=font_tag)
    pill_x += pw + 12

# Description
draw.text((180, bundle_y + 70), "5 libros que te llevan desde cero hasta IA Generativa,", fill="#C9D1D9", font=font_body)
draw.text((180, bundle_y + 105), "con proyectos reales basados en el dataset TechStore.", fill="#C9D1D9", font=font_body)

# CTA Button
cta_x = W - 380
cta_y = bundle_y + 70
draw.rounded_rectangle([(cta_x, cta_y), (cta_x + 250, cta_y + 60)], radius=30, fill="#3FB950", outline=None)
draw.text((cta_x + 30, cta_y + 14), "COMPRAR AHORA \U0001F449", fill="#0D1117", font=font_cta)

# Small URL text
url_text = "payhip.com/SistGoy"
tw = draw.textlength(url_text, font=font_tag)
draw.text(((W - tw) // 2, bundle_y + 165), url_text, fill="#58A6FF", font=font_tag)

# Footer
draw.line([(60, 1150), (W - 60, 1150)], fill="#30363D", width=1)
draw.text((60, 1160), "Data & Analytics Mastery \u00a9 2026", fill="#8B949E", font=font_tag)
draw.text((W - 350, 1160), "Formato EPUB + PDF", fill="#8B949E", font=font_tag)

output_path = os.path.join(BASE, "anuncio_coleccion.png")
img.save(output_path, "PNG", optimize=True)
print(f"Anuncio generado: {output_path}")
print(f"Tamaño: {os.path.getsize(output_path) // 1024} KB")
