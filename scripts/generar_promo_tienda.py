from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math, random

W, H = 1200, 1500
CX = W // 2
FONT_DIR = "C:\\Windows\\Fonts"
OUT = os.path.join(
    r"C:\Users\alexg\OneDrive\Alex_2026\libros epub",
    "promo_tienda.jpg"
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
    ("Excel Basico", "#27AE60"),
    ("Excel Intermedio", "#2980B9"),
    ("Excel Avanzado", "#8E44AD"),
    ("Excel Contadores", "#1ABC9C"),
    ("Excel Analisis Datos", "#2ECC71"),
    ("Excel con Copilot", "#9B59B6"),
    ("HTML Basico", "#E67E22"),
    ("CSS Basico", "#1ABC9C"),
    ("JS Basico", "#F1C40F"),
    ("SQL Letal", "#E74C3C"),
    ("Estadistica Mortal", "#D35400"),
    ("Codigo Asesino", "#C0392B"),
    ("Codigo de Olas", "#16A085"),
    ("Motor Cuantitativo", "#2C3E50"),
    ("Raices Nuevas", "#1ABC9C"),
    ("print('Sigo Aqui')", "#34495E"),
]

COLS = 4
ROWS = 4
CARD_W, CARD_H = 250, 80
GAP_X = 20
GAP_Y = 14
START_X = (W - (COLS * CARD_W + (COLS - 1) * GAP_X)) // 2
START_Y = 460

TAGS = [
    "Excel", "HTML", "CSS", "JavaScript",
    "SQL", "Python", "Data Science", "Estadistica",
]


def main():
    img = Image.new("RGB", (W, H), (10, 8, 20))
    draw = ImageDraw.Draw(img)

    # gradient
    for y in range(H):
        p = y / H
        r = int(10 + p * 35)
        g = int(8 + p * 25)
        b = int(20 + p * 30)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # dots
    random.seed(456)
    for _ in range(250):
        x = random.randint(0, W)
        y = random.randint(0, H)
        s = random.randint(1, 3)
        a = random.randint(20, 70)
        draw.ellipse([x, y, x + s, y + s], fill=(255, 255, 255, a))

    # top decorative line
    for xx in range(60, W - 60, 3):
        yy = 85 + int(math.sin(xx / 40) * 5)
        draw.rectangle([xx, yy, xx + 2, yy + 2], fill="#00B894")

    # header
    f_main = font("georgiab.ttf", 50)
    f_sub = font("georgiai.ttf", 22)
    f_tag_l = font("georgiab.ttf", 18)
    f_book = font("georgiab.ttf", 16)
    f_price = font("arialbd.ttf", 32)
    f_small = font("arial.ttf", 14)
    f_url = font("arialbd.ttf", 20)

    text_center(draw, "APRENDE CON NOVELAS", 30, f_main, "#00B894", shadow=True)
    text_center(draw, "16 libros interactivos de programacion, Excel y datos", 100, f_sub, "#AAAAAA")
    text_center(draw, "Cada libro combina una historia emocionante con enseñanza tecnica real", 128, f_sub, "#777777")

    # book grid
    for i, (name, color) in enumerate(BOOKS):
        col = i % COLS
        row = i // COLS
        x = START_X + col * (CARD_W + GAP_X)
        y = START_Y + row * (CARD_H + GAP_Y)

        draw.rounded_rectangle(
            [x, y, x + CARD_W, y + CARD_H],
            radius=8, fill=(22, 20, 38)
        )
        # color bar left
        draw.rounded_rectangle(
            [x + 3, y + 6, x + 10, y + CARD_H - 6],
            radius=3, fill=color
        )
        # number
        cx, cy = x + 28, y + CARD_H // 2
        draw.ellipse(
            [cx - 13, cy - 13, cx + 13, cy + 13],
            fill=color, outline=(255, 255, 255, 40), width=1
        )
        nf = font("arialbd.ttf", 14)
        b2 = draw.textbbox((0, 0), str(i + 1), font=nf)
        tw = b2[2] - b2[0]
        th = b2[3] - b2[1]
        draw.text((cx - tw // 2, cy - th // 2 - 1), str(i + 1), fill="white", font=nf)

        draw.text((x + 50, y + 28), name, fill="white", font=f_book)

    # tags row
    tag_y = START_Y + ROWS * (CARD_H + GAP_Y) + 25
    tag_total_w = len(TAGS) * 100 + (len(TAGS) - 1) * 10
    tag_start_x = (W - tag_total_w) // 2
    for i, tag in enumerate(TAGS):
        tx = tag_start_x + i * 110
        draw.rounded_rectangle(
            [tx, tag_y, tx + 90, tag_y + 28],
            radius=14, fill=(40, 38, 55)
        )
        draw.text((tx + 14, tag_y + 5), tag, fill="#999999", font=f_small)

    # price banner
    price_y = tag_y + 55
    bw, bh = 500, 65
    bx = (W - bw) // 2
    draw.rounded_rectangle([bx, price_y, bx + bw, price_y + bh], radius=35, fill="#00B894")
    text_center(draw, "CADA LIBRO SOLO €1.00", price_y + 16, f_price, "#0a0a1a")

    # bottom
    text_center(draw, "Descarga inmediata - EPUB + PDF + Codigos", price_y + 95, f_small, "#666666")
    text_center(draw, "https://payhip.com/SistGoy", price_y + 120, f_url, "#00B894")
    text_center(draw, "Alex Goyzueta Delgado", price_y + 150, f_small, "#555555")

    # bottom decorative line
    for xx in range(60, W - 60, 3):
        yy = price_y + 170 + int(math.sin(xx / 35 + 1) * 4)
        draw.rectangle([xx, yy, xx + 2, yy + 2], fill="#00B894")

    img.save(OUT, quality=95)
    print(f"OK - Imagen guardada: {OUT}")
    print(f"  Dimensiones: {W}x{H}")


if __name__ == "__main__":
    main()
