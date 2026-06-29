"""
Genera imagen promocional de la coleccion completa de libros
para la tienda Payhip: https://payhip.com/SistGoy
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math

W, H = 1200, 1500
CX = W // 2
FONT_DIR = "C:\\Windows\\Fonts"
OUT = os.path.join(
    r"C:\Users\alexg\OneDrive\Alex_2026\libros epub",
    "promo_coleccion.jpg"
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


def text_center(draw, text, y, font, fill, shadow=False):
    b = draw.textbbox((0, 0), text, font=font)
    tw = b[2] - b[0]
    x = (W - tw) // 2
    if shadow:
        draw.text((x + 3, y + 3), text, fill=(0, 0, 0, 180), font=font)
    draw.text((x, y), text, fill=fill, font=font)


BOOKS = [
    ("Excel Basico", "#27AE60"),
    ("Excel Intermedio", "#2980B9"),
    ("Excel Avanzado", "#8E44AD"),
    ("SQL Letal", "#E74C3C"),
    ("Estadistica Mortal", "#D35400"),
    ("Codigo Asesino", "#C0392B"),
    ("Codigo de Olas", "#16A085"),
    ("Motor Cuantitativo", "#2C3E50"),
    ("Raices Nuevas", "#1ABC9C"),
    ("print('Sigo Aqui')", "#34495E"),
    ("Graficos para Polos", "#E67E22"),
    ("Graficos Informaticos", "#7F8C8D"),
]

COLS = 3
ROWS = math.ceil(len(BOOKS) / COLS)
CARD_W, CARD_H = 340, 90
START_X = (W - (COLS * CARD_W + (COLS - 1) * 24)) // 2
START_Y = 500

def main():
    img = Image.new("RGB", (W, H), (10, 8, 20))
    draw = ImageDraw.Draw(img)

    # gradient background
    for y in range(H):
        p = y / H
        r = int(10 + p * 30)
        g = int(8 + p * 20)
        b = int(20 + p * 25)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # stars / dots decoration
    import random
    random.seed(123)
    for _ in range(200):
        x = random.randint(0, W)
        y = random.randint(0, H)
        s = random.randint(1, 3)
        a = random.randint(30, 80)
        draw.ellipse([x, y, x + s, y + s], fill=(255, 255, 255, a))

    # title
    f_title = font("georgiab.ttf", 54)
    f_sub = font("georgiai.ttf", 22)
    f_book = font("georgiab.ttf", 18)
    f_price = font("arialbd.ttf", 28)
    f_tag = font("georgiai.ttf", 20)

    # decorative line
    for xx in range(100, W - 100, 4):
        yy = 140 + int(math.sin(xx / 60) * 6)
        draw.rectangle([xx, yy, xx + 2, yy + 2], fill="#F1C40F")

    text_center(draw, "BIBLIOTECA SISTGOY", 80, f_title, "#F1C40F", shadow=True)
    text_center(draw, "Coleccion completa de libros interactivos", 155, f_sub, "#CCCCCC")
    text_center(draw, "Aprende programacion, Excel, SQL y analisis de datos", 185, f_sub, "#999999")

    # book cards
    for i, (name, color) in enumerate(BOOKS):
        col = i % COLS
        row = i // COLS
        x = START_X + col * (CARD_W + 24)
        y = START_Y + row * (CARD_H + 16)

        # card bg
        draw.rounded_rectangle(
            [x, y, x + CARD_W, y + CARD_H],
            radius=10, fill=(25, 22, 40, 220)
        )
        # left color bar
        draw.rounded_rectangle(
            [x + 4, y + 8, x + 12, y + CARD_H - 8],
            radius=4, fill=color
        )
        # book number circle
        cx, cy = x + 32, y + CARD_H // 2
        draw.ellipse(
            [cx - 14, cy - 14, cx + 14, cy + 14],
            fill=color, outline=(255, 255, 255, 40), width=1
        )
        num_f = font("arialbd.ttf", 16)
        b2 = draw.textbbox((0, 0), str(i + 1), font=num_f)
        tw = b2[2] - b2[0]
        th = b2[3] - b2[1]
        draw.text((cx - tw // 2, cy - th // 2 - 1), str(i + 1), fill="white", font=num_f)

        # book name
        draw.text((x + 56, y + 28), name, fill="white", font=f_book)

    # price banner
    by = START_Y + ROWS * (CARD_H + 16) + 40
    bw, bh = 500, 70
    bx = (W - bw) // 2
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=35, fill="#F1C40F")
    text_center(draw, "CADA LIBRO SOLO €1.00", by + 16, f_price, "#1a1a2e")

    # footer
    text_center(draw, "https://payhip.com/SistGoy", by + 100, f_tag, "#666666")

    # bottom decorative line
    for xx in range(100, W - 100, 4):
        yy = by + 130 + int(math.sin(xx / 50 + 2) * 4)
        draw.rectangle([xx, yy, xx + 2, yy + 2], fill="#F1C40F")

    img.save(OUT, quality=95)
    print(f"OK - Imagen guardada: {OUT}")
    print(f"  Dimensiones: {W}x{H}")


if __name__ == "__main__":
    main()
