"""
Genera la portada (cover.jpg) del libro Excel para Análisis de Datos
"""

from PIL import Image, ImageDraw, ImageFont
import os, math

BASE = r"C:\Users\alexg\OneDrive\Alex_2026\libros epub"
OUT = os.path.join(BASE, "excel_analisis_datos", "cover.jpg")
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
    img = Image.new("RGB", (W, H), (8, 12, 18))
    draw = ImageDraw.Draw(img)

    # subtle grid
    for x in range(0, W, 40):
        draw.line([(x, 0), (x, H)], fill=(18, 25, 40, 10))
    for y in range(0, H, 40):
        draw.line([(0, y), (W, y)], fill=(18, 25, 40, 10))

    # top accent bar
    accent = "#0A7E5C"
    for i in range(200, W - 200, 2):
        yoff = 70 + int(math.sin(i / 60) * 6)
        draw.rectangle([i, yoff, i + 3, yoff + 3], fill=accent)

    # book title
    f_main = font("georgiab.ttf", 52)
    f_sub = font("georgiai.ttf", 24)
    f_author = font("georgiai.ttf", 22)
    f_small = font("arial.ttf", 14)

    draw.text((80, 100), "EXCEL PARA", fill=accent, font=f_main)
    draw.text((80, 160), "ANALISIS DE", fill="white", font=font("georgiab.ttf", 68))
    draw.text((80, 232), "DATOS", fill="white", font=font("georgiab.ttf", 68))

    # tagline
    draw.text((80, 310), "De los datos crudos a las decisiones inteligentes", fill="#AAAAAA", font=f_sub)

    # decorated line
    for i in range(80, 500, 3):
        yoff = 380 + int(math.sin(i / 30) * 3)
        draw.rectangle([i, yoff, i + 2, yoff + 2], fill=accent)

    # what's inside
    topics = [
        "Proceso de Analisis",
        "Limpieza y Preparacion",
        "Analisis Exploratorio (EDA)",
        "Funciones de Analisis",
        "Tendencias y Patrones",
        "Tablas Dinamicas",
        "Visualizacion de Datos",
        "Escenarios y Sensibilidad",
        "Power Query",
        "Proyecto Final",
    ]
    f_bullet = font("arial.ttf", 16)
    y = 410
    for t in topics:
        draw.text((100, y), "  " + t, fill="#CCCCCC", font=f_bullet)
        draw.rectangle([90, y + 3, 96, y + 11], fill=accent)
        y += 30

    # highlight box
    bx, by, bw, bh = 80, 760, 520, 120
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=16, fill=(10, 126, 92, 180), outline=accent, width=2)
    f_hl = font("georgiab.ttf", 22)
    draw.text((bx + 30, by + 20), " 10 Capitulos  |  50+ Ejemplos", fill="white", font=f_hl)
    draw.text((bx + 30, by + 60), "  Enigmas practicos  |  Pipeline completo", fill="#CCDDDD", font=font("georgiai.ttf", 18))

    # author
    draw.text((80, 940), "Alex Goyzueta Delgado", fill=accent, font=f_author)

    # bottom
    draw.text((80, 1020), "SistGoy  |  https://payhip.com/SistGoy", fill="#555555", font=f_small)

    # right side decoration - large X icon
    xs = 780
    f_xl = font("georgiab.ttf", 200)
    draw.text((xs, 400), "X", fill=(10, 126, 92, 25), font=f_xl)

    # bottom bar
    for i in range(200, W - 200, 2):
        yoff = 1100 + int(math.sin(i / 50 + 1) * 4)
        draw.rectangle([i, yoff, i + 3, yoff + 3], fill=accent)

    img.save(OUT, quality=95)
    print(f"OK - Cover generada: {OUT}")

if __name__ == "__main__":
    main()
