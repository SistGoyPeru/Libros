"""
Genera imagen promocional de los 5 libros de Excel
para la tienda Payhip: https://payhip.com/SistGoy
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math, random

W, H = 1200, 1500
CX = W // 2
FONT_DIR = "C:\\Windows\\Fonts"
OUT = os.path.join(
    r"C:\Users\alexg\OneDrive\Alex_2026\libros epub",
    "promociones",
    "promo_excel_5.jpg"
)


def font(name, size):
    p = os.path.join(FONT_DIR, name)
    if os.path.exists(p):
        return ImageFont.truetype(p, size)
    for f in ["arial.ttf", "calibri.ttf", "consola.ttf"]:
        fp = os.path.join(FONT_DIR, f)
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()


def text_center(draw, text, y, fnt, fill, shadow=False):
    b = draw.textbbox((0, 0), text, font=fnt)
    tw = b[2] - b[0]
    x = (W - tw) // 2
    if shadow:
        draw.text((x + 3, y + 3), text, fill=(0, 0, 0, 180), font=fnt)
    draw.text((x, y), text, fill=fill, font=fnt)


BOOKS = [
    ("EXCEL BASICO", "#27AE60", "Formulas, formato, funciones basicas"),
    ("EXCEL INTERMEDIO", "#2980B9", "Busquedas, tablas dinamicas, escenarios"),
    ("EXCEL AVANZADO", "#8E44AD", "Power Query, VBA, Power Pivot, Solver"),
    ("EXCEL CONTADORES", "#00B894", "Catalogo, diario, finanzas, dashboards"),
    ("EXCEL ANALISIS", "#0A7E5C", "Limpieza, EDA, Power Query, proyecto final"),
]

def main():
    img = Image.new("RGB", (W, H), (10, 12, 22))
    draw = ImageDraw.Draw(img)

    # grid background
    for x in range(0, W, 40):
        draw.line([(x, 0), (x, H)], fill=(30, 35, 50, 8))
    for y in range(0, H, 40):
        draw.line([(0, y), (W, y)], fill=(30, 35, 50, 8))

    # random dots
    random.seed(456)
    for _ in range(150):
        x = random.randint(0, W)
        y = random.randint(0, H)
        s = random.randint(1, 2)
        draw.ellipse([x, y, x + s, y + s], fill=(100, 200, 100, 30))

    f_main = font("georgiab.ttf", 48)
    f_sub = font("georgiai.ttf", 20)
    f_book_title = font("georgiab.ttf", 24)
    f_book_desc = font("arial.ttf", 13)
    f_price = font("arialbd.ttf", 32)
    f_tag = font("georgiai.ttf", 18)
    f_small = font("arial.ttf", 13)

    # top decorative line
    for xx in range(80, W - 80, 3):
        yy = 60 + int(math.sin(xx / 40) * 5)
        draw.rectangle([xx, yy, xx + 2, yy + 2], fill="#00B894")

    text_center(draw, "COLECCION EXCEL", 25, f_main, "#00B894", shadow=True)
    text_center(draw, "5 libros para dominar Excel de cero a avanzado", 85, f_sub, "#AAAAAA")

    # Excel icon
    icon_size = 70
    ix, iy = CX - icon_size // 2, 120
    draw.rounded_rectangle([ix, iy, ix + icon_size, iy + icon_size], radius=16, fill="#00B894", outline="#00B894", width=2)
    xf = font("arialbd.ttf", 42)
    b = draw.textbbox((0, 0), "X", font=xf)
    tw = b[2] - b[0]
    th = b[3] - b[1]
    draw.text((CX - tw // 2, iy + (icon_size - th) // 2 - 4), "X", fill="white", font=xf)

    text_center(draw, "50+ capitulos  |  Proyectos reales  |  Enigmas practicos", 210, f_sub, "#888888")

    # book cards — 3 on top row, 2 on bottom row
    card_w, card_h = 340, 150
    gap_h = 30
    gap_v = 25

    # row 1: 3 cards
    total_w_3 = 3 * card_w + 2 * gap_h
    start_x_3 = (W - total_w_3) // 2
    start_y_1 = 270

    # row 2: 2 cards
    total_w_2 = 2 * card_w + gap_h
    start_x_2 = (W - total_w_2) // 2
    start_y_2 = start_y_1 + card_h + gap_v

    positions = [
        (start_x_3 + 0 * (card_w + gap_h), start_y_1),
        (start_x_3 + 1 * (card_w + gap_h), start_y_1),
        (start_x_3 + 2 * (card_w + gap_h), start_y_1),
        (start_x_2 + 0 * (card_w + gap_h), start_y_2),
        (start_x_2 + 1 * (card_w + gap_h), start_y_2),
    ]

    for i, ((x, y), (name, color, desc)) in enumerate(zip(positions, BOOKS)):
        # card bg
        draw.rounded_rectangle([x, y, x + card_w, y + card_h], radius=12, fill=(18, 20, 35))
        # top color bar
        draw.rounded_rectangle([x + 2, y + 2, x + card_w - 2, y + 10], radius=5, fill=color)
        # number circle
        cx, cy = x + card_w // 2, y + 35
        draw.ellipse([cx - 18, cy - 18, cx + 18, cy + 18], fill=color, outline=(255, 255, 255, 30), width=2)
        nf = font("arialbd.ttf", 20)
        b2 = draw.textbbox((0, 0), str(i + 1), font=nf)
        tw2 = b2[2] - b2[0]
        th2 = b2[3] - b2[1]
        draw.text((cx - tw2 // 2, cy - th2 // 2 - 1), str(i + 1), fill="white", font=nf)
        # book name
        draw.text((x + 18, y + 65), name, fill="white", font=f_book_title)
        # description
        draw.text((x + 18, y + 95), desc, fill="#999999", font=f_book_desc)

    # what you learn section
    learn_y = start_y_2 + card_h + 40
    text_center(draw, "QUE APRENDERAS", learn_y, font("georgiab.ttf", 24), "#00B894")

    topics = [
        ("1", "Formulas basicas", "SUM, BUSCARV, formato"),
        ("2", "Analisis de datos", "Tablas dinamicas, Power Query"),
        ("3", "Automatizacion", "Macros VBA, Power Pivot"),
        ("4", "Contabilidad", "Diario, finanzas, KPIs"),
        ("5", "Ciencia de datos", "Limpieza, EDA, pipeline"),
    ]
    t_start_y = learn_y + 45
    t_col_w = (W - 80) // 5
    for i, (num, topic, detail) in enumerate(topics):
        x = 40 + i * t_col_w
        y = t_start_y
        nf2 = font("arialbd.ttf", 24)
        draw.text((x + 5, y), num, fill="#00B894", font=nf2)
        draw.text((x + 5, y + 30), topic, fill="white", font=font("georgiab.ttf", 13))
        draw.text((x + 5, y + 50), detail, fill="#777777", font=f_small)

    # price banner
    price_y = t_start_y + 95
    bw, bh = 540, 60
    bx = (W - bw) // 2
    draw.rounded_rectangle([bx, price_y, bx + bw, price_y + bh], radius=35, fill="#00B894")
    text_center(draw, "CADA LIBRO SOLO €1.00  |  COLECCION €4.00", price_y + 15, f_price, "#0a0a1a")

    # bottom
    text_center(draw, "Descargalos ya en:", price_y + 85, f_tag, "#555555")
    text_center(draw, "https://payhip.com/SistGoy", price_y + 110, font("arialbd.ttf", 18), "#00B894")

    # bottom decor
    for xx in range(80, W - 80, 3):
        yy = price_y + 150 + int(math.sin(xx / 35 + 1) * 4)
        draw.rectangle([xx, yy, xx + 2, yy + 2], fill="#00B894")

    img.save(OUT, quality=95)
    print(f"OK - Imagen guardada: {OUT}")
    print(f"  Dimensiones: {W}x{H}")


if __name__ == "__main__":
    main()
