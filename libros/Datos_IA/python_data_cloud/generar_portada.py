from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, random, math

W, H = 1600, 2560
FONT_DIR = "C:\\Windows\\Fonts"
BASE = os.path.dirname(os.path.abspath(__file__))

def load_font(name, size):
    path = os.path.join(FONT_DIR, name)
    if os.path.exists(path):
        return ImageFont.truetype(path, size)
    for fallback in ["consola.ttf", "arial.ttf", "calibri.ttf"]:
        fp = os.path.join(FONT_DIR, fallback)
        if os.path.exists(fp):
            return ImageFont.truetype(fp, size)
    return ImageFont.load_default()

def text_center(draw, text, font, y, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (W - tw) // 2
    draw.text((x, y), text, fill=fill, font=font)

def text_xy(draw, text, font, x, y, fill):
    draw.text((x, y), text, fill=fill, font=font)

def generar_portada():
    img = Image.new("RGB", (W, H), (10, 15, 35))
    draw = ImageDraw.Draw(img)

    # Gradient
    for y in range(H):
        phase = y / H
        draw.line([(0, y), (W, y)], fill=(int(10+phase*25), int(15+phase*30), int(35+phase*20)))

    # Cloud nodes pattern
    random.seed(123)
    for _ in range(80):
        x = random.randint(0, W)
        y = random.randint(0, H)
        r = random.randint(3, 8)
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(30, 60, 130, 40))
        for _2 in range(random.randint(1, 3)):
            x2 = x + random.randint(-60, 60)
            y2 = y + random.randint(-60, 60)
            draw.line([(x, y), (x2, y2)], fill=(40, 70, 150, 20), width=1)

    # Cloud shapes (decorative)
    for cx, cy, s in [(1200, 200, 1), (300, 1600, 0.7), (1400, 2200, 0.5)]:
        for ox, oy in [(0, 0), (40*s, -20*s), (80*s, 10*s), (-30*s, 15*s)]:
            draw.ellipse([cx+ox-35*s, cy+oy-25*s, cx+ox+35*s, cy+oy+25*s], fill=(20, 40, 100, 30))

    # Badge
    f_badge = load_font("calibrib.ttf", 26)
    btext = "DATA & ANALYTICS MASTERY"
    bb = draw.textbbox((0, 0), btext, font=f_badge)
    bw, bh = bb[2]-bb[0], bb[3]-bb[1]
    bx, by = (W-bw)//2, 65
    draw.rounded_rectangle([bx-30, by-10, bx+bw+30, by+bh+15], radius=20, fill=(50, 90, 190, 200))
    draw.rounded_rectangle([bx-30, by-10, bx+bw+30, by+bh+15], radius=20, outline=(100, 160, 255), width=2)
    text_center(draw, btext, f_badge, by+2, (255, 255, 255))

    # Book number badge
    f_n = load_font("calibrib.ttf", 20)
    ntext = "LIBRO 2 DE 5"
    nb = draw.textbbox((0, 0), ntext, font=f_n)
    nw, nh = nb[2]-nb[0], nb[3]-nb[1]
    nx, ny = (W-nw)//2, 125
    draw.rounded_rectangle([nx-18, ny-6, nx+nw+18, ny+nh+10], radius=12, fill=(220, 170, 40, 230))
    text_center(draw, ntext, f_n, ny+1, (35, 25, 10))

    # Title
    f_t = load_font("calibrib.ttf", 64)
    y = 255
    for line in ["PYTHON PARA DATOS", "Y TU PRIMER DATA", "WAREHOUSE CLOUD"]:
        text_center(draw, line, f_t, y, (230, 230, 255))
        y += 72
    line_y = y + 10
    draw.line([(350, line_y), (1250, line_y)], fill=(100, 170, 255), width=4)
    draw.line([(350, line_y+4), (1250, line_y+4)], fill=(60, 100, 200, 80), width=6)

    # Subtitle
    f_sub = load_font("calibrib.ttf", 30)
    text_center(draw, "De Pandas a BigQuery: análisis profesional en la nube", f_sub, line_y+50, (165, 185, 220))

    # Python + Cloud icons
    icons = [("Python", "#3776AB"), ("BigQuery", "#4285F4"), ("Cloud", "#EA4335")]
    iy = 680
    for i, (name, col) in enumerate(icons):
        cx = 250 + i * 450
        r = 55
        cr, cg, cb = int(col[1:3], 16), int(col[3:5], 16), int(col[5:7], 16)
        draw.ellipse([cx-r, iy-r, cx+r, iy+r], fill=(cr, cg, cb), outline=(200, 220, 255), width=2)
        f_ic = load_font("calibrib.ttf", 28)
        fb = draw.textbbox((0, 0), name, font=f_ic)
        fw, fh = fb[2]-fb[0], fb[3]-fb[1]
        draw.text((cx-fw//2, iy-fh//2-fb[1]), name, fill=(255, 255, 255), font=f_ic)

    # Code snippets
    f_code = load_font("consola.ttf", 16)
    snippets = [
        ("import pandas as pd", (55, 118, 171)),
        ("import bigquery as bq", (66, 133, 244)),
        ("df = pd.read_csv('datos.csv')", (55, 118, 171)),
        ("bq.query('SELECT * FROM ventas')", (66, 133, 244)),
        ("sns.barplot(data=df, x='region')", (200, 100, 100)),
        ("df.groupby('mes')['total'].sum()", (55, 118, 171)),
    ]
    sy = 860
    for text, col in snippets:
        text_xy(draw, text, f_code, 150, sy, col)
        sy += 35

    # What you'll learn
    f_lh = load_font("calibrib.ttf", 22)
    f_l = load_font("calibri.ttf", 19)
    lry = 1200
    text_center(draw, "EN ESTE LIBRO APRENDERÁS", f_lh, lry, (180, 200, 230))
    items = [
        "pandas avanzado: merge, groupby, pivot, apply",
        "Limpieza y transformación de datos reales",
        "BigQuery: data warehouse serverless",
        "Looker Studio: dashboards cloud profesionales",
        "Pipelines automatizados en la nube",
    ]
    for i, item in enumerate(items):
        iy = lry + 50 + i * 38
        draw.ellipse([430, iy+2, 438, iy+10], fill=(100, 170, 255))
        text_xy(draw, item, f_l, 455, iy, (200, 210, 230))

    # Author + collection
    draw.line([(300, 2100), (1300, 2100)], fill=(60, 100, 160, 100), width=1)
    f_a = load_font("calibrib.ttf", 28)
    text_center(draw, "Alex Goyzueta Delgado", f_a, 2140, (200, 210, 230))
    f_inf = load_font("calibri.ttf", 19)
    text_center(draw, "Colección Data & Analytics Mastery", f_inf, 2210, (130, 150, 180))
    text_center(draw, "5 libros para dominar el análisis de datos", f_inf, 2250, (120, 140, 170))
    text_center(draw, "Python · BigQuery · Looker · Cloud · IA", f_inf, 2290, (110, 130, 160))
    f_isbn = load_font("calibri.ttf", 15)
    text_center(draw, "ISBN: Pendiente  |  © 2026 Alex Goyzueta Delgado", f_isbn, 2420, (70, 90, 120))

    out = os.path.join(BASE, "cover.jpg")
    img.save(out, quality=95)
    print(f"Portada generada: {out}")

if __name__ == "__main__":
    generar_portada()
