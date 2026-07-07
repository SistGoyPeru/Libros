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
    img = Image.new("RGB", (W, H), (15, 20, 50))
    draw = ImageDraw.Draw(img)

    # Gradient
    for y in range(H):
        phase = y / H
        draw.line([(0, y), (W, y)], fill=(int(15+phase*30), int(20+phase*25), int(50+phase*30)))

    # Grid pattern (like a dashboard grid)
    random.seed(456)
    for x in range(0, W, 40):
        draw.line([(x, 0), (x, H)], fill=(25, 40, 80, 10), width=1)
    for y in range(0, H, 40):
        draw.line([(0, y), (W, y)], fill=(25, 40, 80, 10), width=1)

    # Dashboard nodes
    for _ in range(50):
        x = random.randint(0, W)
        y = random.randint(0, H)
        r = random.randint(4, 12)
        draw.rectangle([x-r, y-r, x+r, y+r], fill=(30, 60, 130, 30), outline=(60, 100, 200, 20), width=1)
        for _2 in range(random.randint(1, 2)):
            x2 = x + random.randint(-80, 80)
            y2 = y + random.randint(-80, 80)
            draw.line([(x, y), (x2, y2)], fill=(50, 80, 180, 15), width=1)

    # Bar chart decoration
    bar_colors = [(200, 100, 50, 60), (50, 130, 200, 60), (80, 180, 80, 60)]
    for bx, h, col in [(200, 300, bar_colors[0]), (350, 200, bar_colors[1]), (500, 400, bar_colors[2]),
                        (1100, 350, bar_colors[0]), (1250, 250, bar_colors[1]), (1400, 180, bar_colors[2])]:
        draw.rectangle([bx, 1800-h, bx+80, 1800], fill=col)

    # Line chart decoration
    points = [(100, 1500), (300, 1480), (500, 1510), (700, 1470), (900, 1490), (1100, 1460), (1300, 1480), (1500, 1450)]
    for i in range(len(points)-1):
        draw.line([points[i], points[i+1]], fill=(100, 200, 255, 80), width=3)
    for px, py in points:
        draw.ellipse([px-5, py-5, px+5, py+5], fill=(100, 200, 255, 120))

    # Badge
    f_badge = load_font("calibrib.ttf", 26)
    btext = "DATA & ANALYTICS MASTERY"
    bb = draw.textbbox((0, 0), btext, font=f_badge)
    bw, bh = bb[2]-bb[0], bb[3]-bb[1]
    bx, by = (W-bw)//2, 65
    draw.rounded_rectangle([bx-30, by-10, bx+bw+30, by+bh+15], radius=20, fill=(200, 100, 30, 200))
    draw.rounded_rectangle([bx-30, by-10, bx+bw+30, by+bh+15], radius=20, outline=(255, 180, 100), width=2)
    text_center(draw, btext, f_badge, by+2, (255, 255, 255))

    # Book number badge
    f_n = load_font("calibrib.ttf", 20)
    ntext = "LIBRO 3 DE 5"
    nb = draw.textbbox((0, 0), ntext, font=f_n)
    nw, nh = nb[2]-nb[0], nb[3]-nb[1]
    nx, ny = (W-nw)//2, 125
    draw.rounded_rectangle([nx-18, ny-6, nx+nw+18, ny+nh+10], radius=12, fill=(220, 170, 40, 230))
    text_center(draw, ntext, f_n, ny+1, (35, 25, 10))

    # Title
    f_t = load_font("calibrib.ttf", 60)
    y = 260
    for line in ["BUSINESS INTELLIGENCE", "Y MODELADO DE", "DATOS"]:
        text_center(draw, line, f_t, y, (230, 230, 255))
        y += 68
    line_y = y + 10
    draw.line([(350, line_y), (1250, line_y)], fill=(255, 180, 80), width=4)
    draw.line([(350, line_y+4), (1250, line_y+4)], fill=(200, 120, 40, 80), width=6)

    # Subtitle
    f_sub = load_font("calibrib.ttf", 28)
    text_center(draw, "Diseña dashboards profesionales y modela", f_sub, line_y+50, (165, 185, 220))
    text_center(draw, "datos como un experto", f_sub, line_y+85, (165, 185, 220))

    # Tool icons
    icons = [("Power BI", "#F2C811"), ("DAX", "#00A3E0"), ("SQL", "#EA4335")]
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
        ("CALCULATE([Ventas], FILTER(...))", (0, 163, 224)),
        ("POWER BI Desktop", (242, 200, 17)),
        ("EVALUATE SUMMARIZECOLUMNS", (0, 163, 224)),
        ("Star Schema Modeling", (242, 200, 17)),
        ("VAR / RETURN in DAX", (0, 163, 224)),
        ("Table.MergedJoin Power Query", (200, 100, 100)),
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
        "Modelado dimensional: hechos y dimensiones",
        "Power BI Desktop: dashboards profesionales",
        "DAX: time intelligence, CALCULATE y KPIs",
        "Power Query ETL y transformación de datos",
        "Power BI Service: RLS, publicación y gobierno",
    ]
    for i, item in enumerate(items):
        iy = lry + 50 + i * 38
        draw.ellipse([430, iy+2, 438, iy+10], fill=(255, 180, 80))
        text_xy(draw, item, f_l, 455, iy, (200, 210, 230))

    # Author + collection
    draw.line([(300, 2100), (1300, 2100)], fill=(60, 100, 160, 100), width=1)
    f_a = load_font("calibrib.ttf", 28)
    text_center(draw, "Alex Goyzueta Delgado", f_a, 2140, (200, 210, 230))
    f_inf = load_font("calibri.ttf", 19)
    text_center(draw, "Colección Data & Analytics Mastery", f_inf, 2210, (130, 150, 180))
    text_center(draw, "5 libros para dominar el análisis de datos", f_inf, 2250, (120, 140, 170))
    text_center(draw, "Power BI · DAX · SQL · ETL · BI Service", f_inf, 2290, (110, 130, 160))
    f_isbn = load_font("calibri.ttf", 15)
    text_center(draw, "ISBN: Pendiente  |  © 2026 Alex Goyzueta Delgado", f_isbn, 2420, (70, 90, 120))

    out = os.path.join(BASE, "cover.jpg")
    img.save(out, quality=95)
    print(f"Portada generada: {out}")

if __name__ == "__main__":
    generar_portada()
