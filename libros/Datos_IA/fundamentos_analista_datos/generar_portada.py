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

def draw_bar_chart(draw, x0, y0, x1, y1, values, colors):
    n = len(values)
    max_val = max(values) if max(values) > 0 else 1
    chart_w = x1 - x0
    chart_h = y1 - y0
    bar_w = chart_w // (n * 2)
    for i, (v, c) in enumerate(zip(values, colors)):
        bh = (v / max_val) * chart_h
        bx = x0 + i * (bar_w * 2) + bar_w // 2
        by = y1 - bh
        draw.rectangle([bx, by, bx + bar_w, y1], fill=c)
        if bh > 3:
            draw.rectangle([bx, by, bx + bar_w, y1], outline=(255, 255, 255, 40), width=1)

def draw_line_chart(draw, x0, y0, x1, y1, values, line_color, dot_color):
    n = len(values)
    max_val = max(values) if max(values) > 0 else 1
    chart_w = x1 - x0
    chart_h = y1 - y0
    pts = []
    for i, v in enumerate(values):
        px = x0 + (i / (n - 1)) * chart_w
        py = y1 - (v / max_val) * chart_h
        pts.append((px, py))
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=line_color, width=3)
    for px, py in pts:
        draw.ellipse([px - 5, py - 5, px + 5, py + 5], fill=dot_color)

def generar_portada():
    img = Image.new("RGB", (W, H), (7, 10, 25))
    draw = ImageDraw.Draw(img)

    # === DARK GRADIENT BACKGROUND ===
    for y in range(H):
        phase = y / H
        r = int(7 + phase * 22)
        g = int(10 + phase * 28)
        b = int(25 + phase * 20)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # === DATA VISUALIZATION BACKGROUND ELEMENTS ===

    # Background bar chart (large, subtle)
    bg_bars = [80, 55, 95, 70, 85, 60, 90, 75]
    bg_colors = [(20, 40, 90, 60) for _ in bg_bars]
    draw_bar_chart(draw, 100, 400, 700, 900, bg_bars, bg_colors)

    # Background line chart
    draw_line_chart(draw, 900, 400, 1500, 900,
                    [30, 55, 45, 70, 60, 85, 75, 90, 80, 95],
                    (40, 80, 160, 80), (60, 120, 220, 80))

    # Second small chart row
    draw_bar_chart(draw, 100, 1600, 500, 1850, [45, 70, 55, 85, 60], [(30, 60, 130, 50) for _ in range(5)])

    # Scatter dots (simulating data points)
    random.seed(42)
    for _ in range(200):
        x = random.randint(0, W)
        y = random.randint(0, H)
        size = random.randint(1, 4)
        alpha = random.randint(10, 35)
        draw.ellipse([x-size, y-size, x+size, y+size], fill=(60, 120, 200, alpha))

    # Grid lines (like graph paper)
    for x in range(0, W, 200):
        draw.line([(x, 0), (x, H)], fill=(25, 40, 80, 30), width=1)
    for y in range(0, H, 200):
        draw.line([(0, y), (W, y)], fill=(25, 40, 80, 30), width=1)

    # === TOP COLLECTION BADGE ===
    f_badge = load_font("calibrib.ttf", 26)
    badge_text = "DATA & ANALYTICS MASTERY"
    bb = draw.textbbox((0, 0), badge_text, font=f_badge)
    bw = bb[2] - bb[0]
    bh = bb[3] - bb[1]
    bx = (W - bw) // 2
    by = 65
    draw.rounded_rectangle([bx-30, by-10, bx+bw+30, by+bh+15], radius=20, fill=(50, 90, 190, 200))
    draw.rounded_rectangle([bx-30, by-10, bx+bw+30, by+bh+15], radius=20, outline=(100, 160, 255), width=2)
    text_center(draw, badge_text, f_badge, by + 2, (255, 255, 255))

    # === LIBRO 1 DE 5 BADGE ===
    f_booknum = load_font("calibrib.ttf", 20)
    num_text = "LIBRO 1 DE 5"
    nb = draw.textbbox((0, 0), num_text, font=f_booknum)
    nw = nb[2] - nb[0]
    nh = nb[3] - nb[1]
    nx = (W - nw) // 2
    ny = 125
    draw.rounded_rectangle([nx-18, ny-6, nx+nw+18, ny+nh+10], radius=12, fill=(220, 170, 40, 230))
    text_center(draw, num_text, f_booknum, ny + 1, (35, 25, 10))

    # === MAIN TITLE ===
    f_title = load_font("calibrib.ttf", 74)

    # Calcular altura real del texto para espaciado preciso
    def centered_text_bbox(text, font, y):
        bb = draw.textbbox((0, 0), text, font=font)
        tw = bb[2] - bb[0]
        th = bb[3] - bb[1]
        x = (W - tw) // 2
        draw.text((x, y), text, fill=(235, 235, 255), font=font)
        return y + th

    y_title = 270
    y_title = centered_text_bbox("LOS FUNDAMENTOS", f_title, y_title)
    y_title = centered_text_bbox("DEL ANALISTA", f_title, y_title + 10)
    y_title = centered_text_bbox("DE DATOS", f_title, y_title + 10)
    line_y = y_title + 20

    # Accent line
    draw.line([(350, line_y), (1250, line_y)], fill=(100, 170, 255), width=4)
    draw.line([(350, line_y + 4), (1250, line_y + 4)], fill=(60, 100, 200, 80), width=6)

    # === SUBTITLE ===
    f_sub = load_font("calibrib.ttf", 32)
    text_center(draw, "Domina SQL, Excel y Python desde cero", f_sub, line_y + 50, (165, 185, 220))

    # === CENTRAL DATA VISUALIZATION ===
    # Main bar chart (prominent)
    chart_values = [82, 95, 65, 78, 88, 72, 91]
    chart_colors = ["#4479A1", "#217346", "#3776AB", "#D9541A", "#6B3FA0", "#E8A415", "#4479A1"]
    chart_colors_rgb = [(int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16)) for c in chart_colors]
    draw_bar_chart(draw, 250, 700, 750, 900, chart_values, chart_colors_rgb)

    # Line chart overlay
    draw_line_chart(draw, 850, 700, 1350, 900,
                    [40, 65, 55, 78, 62, 88, 72, 92],
                    (80, 180, 255), (180, 220, 255))

    # === KPI CARDS ===
    kpi_data = [
        ("1.2M", "Ingresos", 200),
        ("5,250", "Pedidos", 700),
        ("250", "Clientes", 1200),
    ]
    f_kpi_val = load_font("calibrib.ttf", 36)
    f_kpi_lbl = load_font("calibri.ttf", 16)
    for val, lbl, kx in kpi_data:
        # Card background
        draw.rounded_rectangle([kx-8, 960, kx+140, 1010], radius=6, fill=(20, 40, 90, 100),
                               outline=(40, 80, 160, 80), width=1)
        text_xy(draw, val, f_kpi_val, kx+4, 960, (200, 220, 255))
        text_xy(draw, lbl, f_kpi_lbl, kx+4, 1000, (140, 170, 200))

    # === CODE SNIPPET ROW ===
    f_code = load_font("consola.ttf", 16)
    snippets = [
        ("SELECT region, SUM(total)", (68, 121, 161)),
        ("FROM ventas GROUP BY region;", (68, 121, 161)),
        ("  df.groupby('region')['total'].sum()", (55, 118, 171)),
        ("=TABLA DINAMICA(ventas; regiones)", (33, 115, 70)),
    ]
    sx = 130
    for text, col in snippets:
        text_xy(draw, text, f_code, sx, 1070, col)
        sx += 28

    # === THREE PILLAR ICONS ===
    icons_data = [
        ("SQL", "#4479A1", 1),
        ("Excel", "#217346", 2),
        ("Python", "#3776AB", 3),
    ]
    icons_y = 1240
    for name, col, idx in icons_data:
        cx = 200 + idx * 400
        r = 60
        cr, cg, cb = int(col[1:3], 16), int(col[3:5], 16), int(col[5:7], 16)
        # Outer glow
        for g_r in range(65, r, -8):
            alpha = max(0, 20 - (r - g_r) * 2)
            draw.ellipse([cx - g_r, icons_y - g_r, cx + g_r, icons_y + g_r],
                         fill=(cr//2, cg//2, cb//2, alpha))
        # Main circle
        draw.ellipse([cx - r, icons_y - r, cx + r, icons_y + r],
                     fill=(cr, cg, cb), outline=(200, 220, 255), width=2)
        # Inner shadow effect
        draw.ellipse([cx - r + 3, icons_y - r + 3, cx + r - 3, icons_y + r - 3],
                     outline=(cr+30, cg+30, cb+30, 60), width=1)
        f_icon = load_font("calibrib.ttf", 34)
        # Centrar texto VERTICAL y HORIZONTAL dentro del círculo
        fb = draw.textbbox((0, 0), name, font=f_icon)
        fw = fb[2] - fb[0]
        fh = fb[3] - fb[1]
        tx = cx - fw // 2
        ty = icons_y - fh // 2 - fb[1]
        draw.text((tx, ty), name, fill=(255, 255, 255), font=f_icon)

    # === WHAT YOU'LL LEARN ===
    f_learn_h = load_font("calibrib.ttf", 22)
    f_learn = load_font("calibri.ttf", 20)
    learn_y = 1400
    text_center(draw, "EN ESTE LIBRO APRENDERÁS", f_learn_h, learn_y, (180, 200, 230))

    items = [
        "SQL completo: desde SELECT hasta Window Functions",
        "Excel avanzado: Power Query, DAX y dashboards",
        "Python: pandas, automatización y pipelines",
        "Pipeline integrado: SQL + Python + Excel",
        "4 proyectos reales con datos de TechStore",
    ]
    for i, item in enumerate(items):
        iy = learn_y + 50 + i * 40
        # Bullet point
        draw.ellipse([430, iy + 2, 438, iy + 10], fill=(100, 170, 255))
        text_xy(draw, item, f_learn, 455, iy, (200, 210, 230))

    # === BOTTOM DATA VISUALIZATION ===
    # Small bar chart at bottom
    draw_bar_chart(draw, 1200, 1800, 1500, 1900, [60, 80, 70, 85, 90], [(40, 80, 170, 50) for _ in range(5)])

    # === BOTTOM SECTION ===
    draw.line([(300, 2100), (1300, 2100)], fill=(60, 100, 160, 100), width=1)

    # Author
    f_author = load_font("calibrib.ttf", 28)
    text_center(draw, "Alex Goyzueta Delgado", f_author, 2140, (200, 210, 230))

    # Collection
    f_info = load_font("calibri.ttf", 19)
    text_center(draw, "Colección Data & Analytics Mastery", f_info, 2210, (130, 150, 180))
    text_center(draw, "5 libros para dominar el análisis de datos", f_info, 2250, (120, 140, 170))
    text_center(draw, "SQL · Excel · Python · BI · Big Data · IA", f_info, 2290, (110, 130, 160))

    # ISBN
    f_isbn = load_font("calibri.ttf", 15)
    text_center(draw, "ISBN: Pendiente  |  © 2026 Alex Goyzueta Delgado", f_isbn, 2420, (70, 90, 120))

    out = os.path.join(BASE, "cover.jpg")
    img.save(out, quality=95)
    print(f"Portada generada: {out}")

if __name__ == "__main__":
    generar_portada()
