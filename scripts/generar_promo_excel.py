"""
Genera imagen promocional de los 3 libros de Excel
para la tienda Payhip: https://payhip.com/SistGoy
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math, random

W, H = 1200, 1500
CX = W // 2
FONT_DIR = "C:\\Windows\\Fonts"
OUT = os.path.join(
    r"C:\Users\alexg\OneDrive\Alex_2026\libros epub",
    "promo_excel.jpg"
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
    ("EXCEL BASICO", "#27AE60", "Introduccion a Excel", "Formulas, formato, funciones basicas, graficos"),
    ("EXCEL INTERMEDIO", "#2980B9", "Analisis de datos", "Busquedas, tablas dinamicas, dashboard, escenarios"),
    ("EXCEL AVANZADO", "#8E44AD", "Power Query, DAX, VBA", "Macros, Power Pivot, Solver, Power BI"),
]

def main():
    img = Image.new("RGB", (W, H), (10, 12, 22))
    draw = ImageDraw.Draw(img)

    # grid background (spreadsheet vibe)
    for x in range(0, W, 40):
        a = 8
        draw.line([(x, 0), (x, H)], fill=(30, 35, 50, a))
    for y in range(0, H, 40):
        a = 8
        draw.line([(0, y), (W, y)], fill=(30, 35, 50, a))

    # random dots
    random.seed(456)
    for _ in range(150):
        x = random.randint(0, W)
        y = random.randint(0, H)
        s = random.randint(1, 2)
        draw.ellipse([x, y, x + s, y + s], fill=(100, 200, 100, 30))

    # ── header ──
    f_main = font("georgiab.ttf", 56)
    f_sub = font("georgiai.ttf", 22)
    f_book_title = font("georgiab.ttf", 28)
    f_book_sub = font("georgiai.ttf", 16)
    f_book_desc = font("arial.ttf", 14)
    f_price = font("arialbd.ttf", 34)
    f_tag = font("georgiai.ttf", 18)
    f_small = font("arial.ttf", 13)

    # top decorative line
    for xx in range(80, W - 80, 3):
        yy = 70 + int(math.sin(xx / 40) * 5)
        draw.rectangle([xx, yy, xx + 2, yy + 2], fill="#00B894")

    text_center(draw, "TRILOGIA EXCEL", 30, f_main, "#00B894", shadow=True)
    text_center(draw, "Domina Excel de cero a avanzado con historias interactivas", 100, f_sub, "#AAAAAA")

    # Excel icon placeholder (stylized X)
    icon_size = 80
    ix, iy = CX - icon_size // 2, 140
    draw.rounded_rectangle(
        [ix, iy, ix + icon_size, iy + icon_size],
        radius=16, fill="#27AE60", outline="#00B894", width=2
    )
    xf = font("arialbd.ttf", 50)
    b = draw.textbbox((0, 0), "X", font=xf)
    tw = b[2] - b[0]
    th = b[3] - b[1]
    draw.text((CX - tw // 2, iy + (icon_size - th) // 2 - 4), "X", fill="white", font=xf)

    text_center(draw, "3 libros  |  30 capitulos  |  Proyectos reales", 248, f_sub, "#888888")

    # ── book cards ──
    card_w, card_h = 340, 170
    gap = 30
    total_w = 3 * card_w + 2 * gap
    start_x = (W - total_w) // 2
    start_y = 320

    for i, (name, color, subtitle, desc) in enumerate(BOOKS):
        x = start_x + i * (card_w + gap)
        y = start_y

        # card bg
        draw.rounded_rectangle(
            [x, y, x + card_w, y + card_h],
            radius=14, fill=(18, 20, 35)
        )
        # top color bar
        draw.rounded_rectangle(
            [x + 2, y + 2, x + card_w - 2, y + 12],
            radius=6, fill=color
        )
        # number circle
        cx, cy = x + card_w // 2, y + 40
        draw.ellipse(
            [cx - 20, cy - 20, cx + 20, cy + 20],
            fill=color, outline=(255, 255, 255, 30), width=2
        )
        nf = font("arialbd.ttf", 22)
        b2 = draw.textbbox((0, 0), str(i + 1), font=nf)
        tw = b2[2] - b2[0]
        th = b2[3] - b2[1]
        draw.text((cx - tw // 2, cy - th // 2 - 1), str(i + 1), fill="white", font=nf)

        # book name
        draw.text((x + 20, y + 72), name, fill="white", font=f_book_title)

        # subtitle
        draw.text((x + 20, y + 104), subtitle, fill=color, font=f_book_sub)

        # description
        draw.text((x + 20, y + 128), desc, fill="#999999", font=f_book_desc)

    # ── what you learn section ──
    learn_y = start_y + card_h + 50
    text_center(draw, "QUE APRENDERAS", learn_y, font("georgiab.ttf", 26), "#00B894")
    
    topics = [
        ("1", "Formulas y funciones", "SUM, AVERAGE, BUSCARV, DAX"),
        ("2", "Analisis de datos", "Tablas dinamicas, graficos, Power Query"),
        ("3", "Automatizacion", "Macros VBA, Power Pivot, Power BI"),
        ("4", "Gestion empresarial", "Dashboard, escenarios, Solver"),
    ]
    t_start_y = learn_y + 50
    t_col_w = (W - 120) // 4
    for i, (num, topic, detail) in enumerate(topics):
        x = 60 + i * t_col_w
        y = t_start_y
        # number
        nf2 = font("arialbd.ttf", 28)
        draw.text((x + 10, y), num, fill="#00B894", font=nf2)
        # topic
        draw.text((x + 10, y + 36), topic, fill="white", font=font("georgiab.ttf", 16))
        # detail
        draw.text((x + 10, y + 60), detail, fill="#777777", font=f_small)

    # ── price banner ──
    price_y = t_start_y + 110
    bw, bh = 520, 65
    bx = (W - bw) // 2
    draw.rounded_rectangle([bx, price_y, bx + bw, price_y + bh], radius=35, fill="#00B894")
    text_center(draw, "CADA LIBRO SOLO €1.00  |  LOS 3 POR €2.50", price_y + 16, f_price, "#0a0a1a")

    # ── bottom ──
    text_center(draw, "Descargalos ya en:", price_y + 90, f_tag, "#555555")
    text_center(draw, "https://payhip.com/SistGoy", price_y + 115, font("arialbd.ttf", 18), "#00B894")

    # bottom decor
    for xx in range(80, W - 80, 3):
        yy = price_y + 155 + int(math.sin(xx / 35 + 1) * 4)
        draw.rectangle([xx, yy, xx + 2, yy + 2], fill="#00B894")

    img.save(OUT, quality=95)
    print(f"OK - Imagen guardada: {OUT}")
    print(f"  Dimensiones: {W}x{H}")


if __name__ == "__main__":
    main()
