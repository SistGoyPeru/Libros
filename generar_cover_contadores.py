"""
Genera la portada (cover.jpg) del libro Excel para Contadores
"""

from PIL import Image, ImageDraw, ImageFont
import os, math

BASE = r"C:\Users\alexg\OneDrive\Alex_2026\libros epub"
OUT = os.path.join(BASE, "excel_contadores", "cover.jpg")
FONT_DIR = "C:\\Windows\\Fonts"
W, H = 1200, 1500

def font(name, size):
    p = os.path.join(FONT_DIR, name)
    if os.path.exists(p):
        return ImageFont.truetype(p, size)
    for f in ["arial.ttf", "calibri.ttf", "consola.ttf"]:
        fp = os.path.join(FONT_DIR, f)
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

def main():
    img = Image.new("RGB", (W, H), (8, 10, 20))
    draw = ImageDraw.Draw(img)

    # subtle grid
    for x in range(0, W, 40):
        draw.line([(x, 0), (x, H)], fill=(20, 25, 45, 10))
    for y in range(0, H, 40):
        draw.line([(0, y), (W, y)], fill=(20, 25, 45, 10))

    # top accent bar
    for i in range(200, W - 200, 2):
        yoff = 70 + int(math.sin(i / 60) * 6)
        draw.rectangle([i, yoff, i + 3, yoff + 3], fill="#00B894")

    # book title
    f_main = font("georgiab.ttf", 60)
    f_sub = font("georgiai.ttf", 26)
    f_tag = font("georgiai.ttf", 18)
    f_author = font("georgiai.ttf", 22)
    f_small = font("arial.ttf", 14)

    draw.text((80, 100), "EXCEL PARA", fill="#00B894", font=f_main)
    draw.text((80, 168), "CONTADORES", fill="white", font=font("georgiab.ttf", 72))

    # tagline
    draw.text((80, 260), "Domina Excel en el mundo contable y financiero", fill="#AAAAAA", font=f_sub)

    # decorated line
    for i in range(80, 500, 3):
        yoff = 330 + int(math.sin(i / 30) * 3)
        draw.rectangle([i, yoff, i + 2, yoff + 2], fill="#00B894")

    # what's inside
    topics = [
        "Catalogo de Cuentas",
        "Libro Diario y Mayor",
        "Funciones Financieras",
        "Tablas Dinamicas",
        "Consolidacion Contable",
        "Auditoria en Excel",
        "Dashboard de KPIs",
        "Macros VBA Contables",
    ]
    f_bullet = font("arial.ttf", 16)
    y = 360
    for t in topics:
        draw.text((100, y), "  " + t, fill="#CCCCCC", font=f_bullet)
        draw.rectangle([90, y + 3, 96, y + 11], fill="#00B894")
        y += 32

    # highlight box
    bx, by, bw, bh = 80, 680, 520, 120
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=16, fill=(15, 120, 90, 180), outline="#00B894", width=2)
    f_hl = font("georgiab.ttf", 22)
    draw.text((bx + 30, by + 20), " 10 Capitulos  |  50+ Ejemplos", fill="white", font=f_hl)
    draw.text((bx + 30, by + 60), "  Enigmas practicos  |  100% Contable", fill="#CCDDDD", font=font("georgiai.ttf", 18))

    # author
    draw.text((80, 860), "Alex Goyzueta Delgado", fill="#00B894", font=f_author)

    # bottom
    draw.text((80, 940), "SistGoy  |  https://payhip.com/SistGoy", fill="#555555", font=f_small)

    # right side decoration - large X icon
    xs = 780
    f_xl = font("georgiab.ttf", 200)
    draw.text((xs, 360), "X", fill=(0, 184, 148, 25), font=f_xl)

    # bottom bar
    for i in range(200, W - 200, 2):
        yoff = 1010 + int(math.sin(i / 50 + 1) * 4)
        draw.rectangle([i, yoff, i + 3, yoff + 3], fill="#00B894")

    img.save(OUT, quality=95)
    print(f"OK - Cover generada: {OUT}")

if __name__ == "__main__":
    main()
