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
    img = Image.new("RGB", (W, H), (5, 12, 25))
    draw = ImageDraw.Draw(img)

    # Gradient (dark blue tech feel)
    for y in range(H):
        phase = y / H
        draw.line([(0, y), (W, y)], fill=(int(5+phase*20), int(12+phase*18), int(25+phase*25)))

    # Pipeline nodes with connections (like a DAG)
    random.seed(789)
    nodes = []
    for _ in range(60):
        x = random.randint(50, W-50)
        y = random.randint(50, H-50)
        r = random.randint(5, 10)
        nodes.append((x, y, r))
        draw.ellipse([x-r, y-r, x+r, y+r], fill=(30, 120, 200, 60), outline=(60, 180, 255, 40), width=1)

    # Connect nodes like a DAG
    for i in range(len(nodes)-1):
        if random.random() < 0.15:
            x1, y1, _ = nodes[i]
            x2, y2, _ = nodes[i+1]
            draw.line([(x1, y1), (x2, y2)], fill=(60, 160, 255, 20), width=1)

    # DAG flow arrows (bottom area)
    arrow_y = 1750
    for ax, label in [(200, "Extract"), (500, "Transform"), (800, "Load"), (1100, "Orchestrate"), (1400, "Deploy")]:
        draw.rounded_rectangle([ax-10, arrow_y-15, ax+130, arrow_y+15], radius=8, fill=(20, 80, 160, 100), outline=(80, 180, 255, 60), width=1)
        f_ar = load_font("calibrib.ttf", 14)
        fb = draw.textbbox((0, 0), label, font=f_ar)
        fw = fb[2]-fb[0]
        draw.text((ax+60-fw//2, arrow_y-10), label, fill=(180, 220, 255), font=f_ar)

    # Connector arrows
    for ax in [330, 630, 930, 1230]:
        draw.polygon([(ax, arrow_y), (ax+20, arrow_y-5), (ax+20, arrow_y+5)], fill=(80, 180, 255, 80))

    # Badge
    f_badge = load_font("calibrib.ttf", 26)
    btext = "DATA & ANALYTICS MASTERY"
    bb = draw.textbbox((0, 0), btext, font=f_badge)
    bw, bh = bb[2]-bb[0], bb[3]-bb[1]
    bx, by = (W-bw)//2, 65
    draw.rounded_rectangle([bx-30, by-10, bx+bw+30, by+bh+15], radius=20, fill=(30, 100, 180, 200))
    draw.rounded_rectangle([bx-30, by-10, bx+bw+30, by+bh+15], radius=20, outline=(80, 200, 255), width=2)
    text_center(draw, btext, f_badge, by+2, (255, 255, 255))

    # Book number badge
    f_n = load_font("calibrib.ttf", 20)
    ntext = "LIBRO 4 DE 5"
    nb = draw.textbbox((0, 0), ntext, font=f_n)
    nw, nh = nb[2]-nb[0], nb[3]-nb[1]
    nx, ny = (W-nw)//2, 125
    draw.rounded_rectangle([nx-18, ny-6, nx+nw+18, ny+nh+10], radius=12, fill=(220, 170, 40, 230))
    text_center(draw, ntext, f_n, ny+1, (35, 25, 10))

    # Title
    f_t = load_font("calibrib.ttf", 60)
    y = 260
    for line in ["INGENIERIA DE", "DATOS MODERNA"]:
        text_center(draw, line, f_t, y, (230, 230, 255))
        y += 68
    line_y = y + 10
    draw.line([(350, line_y), (1250, line_y)], fill=(80, 200, 255), width=4)
    draw.line([(350, line_y+4), (1250, line_y+4)], fill=(30, 100, 180, 80), width=6)

    # Subtitle
    f_sub = load_font("calibrib.ttf", 28)
    text_center(draw, "Domina el data engineering moderno", f_sub, line_y+50, (165, 185, 220))
    text_center(draw, "con Python, Airflow y dbt", f_sub, line_y+85, (165, 185, 220))

    # Tool icons
    icons = [("Python", "#3776AB"), ("Airflow", "#017CEE"), ("dbt", "#FF694B")]
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
        ("@dag(schedule='@daily')", (1, 124, 238)),
        ("def extract_orders():", (55, 118, 171)),
        ("dbt run --select marts", (255, 105, 75)),
        ("DockerOperator(task_id='dbt')", (1, 124, 238)),
        ("s3.upload_file('data.parquet')", (227, 170, 50)),
        ("airflow dags trigger techstore", (1, 124, 238)),
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
        "Data Lakes con MinIO y Parquet",
        "dbt: transformaciones, testing y documentación",
        "Apache Airflow: orquestación y monitoreo",
        "Docker: contenedores para pipelines",
        "CI/CD para datos con GitHub Actions",
    ]
    for i, item in enumerate(items):
        iy = lry + 50 + i * 38
        draw.ellipse([430, iy+2, 438, iy+10], fill=(80, 200, 255))
        text_xy(draw, item, f_l, 455, iy, (200, 210, 230))

    # Author + collection
    draw.line([(300, 2100), (1300, 2100)], fill=(60, 100, 160, 100), width=1)
    f_a = load_font("calibrib.ttf", 28)
    text_center(draw, "Alex Goyzueta Delgado", f_a, 2140, (200, 210, 230))
    f_inf = load_font("calibri.ttf", 19)
    text_center(draw, "Colección Data & Analytics Mastery", f_inf, 2210, (130, 150, 180))
    text_center(draw, "5 libros para dominar el análisis de datos", f_inf, 2250, (120, 140, 170))
    text_center(draw, "Python · dbt · Airflow · Docker · CI/CD", f_inf, 2290, (110, 130, 160))
    f_isbn = load_font("calibri.ttf", 15)
    text_center(draw, "ISBN: Pendiente  |  © 2026 Alex Goyzueta Delgado", f_isbn, 2420, (70, 90, 120))

    out = os.path.join(BASE, "cover.jpg")
    img.save(out, quality=95)
    print(f"Portada generada: {out}")

if __name__ == "__main__":
    generar_portada()
