from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, random, math

# Amazon Kindle eBook: 2560 height x 1600 width (portrait)
W, H = 1600, 2560
CX, CY = W // 2, H // 2  # center: 800, 1280
FONT_DIR = "C:\\Windows\\Fonts"
BASE = r"C:\Users\alexg\OneDrive\Alex_2026\libros epub"


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
    return x, tw, bbox[3] - bbox[1]


def shadow_text(draw, text, font, y, fill, dx=4, dy=4):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (W - tw) // 2
    for sx, sy in [(dx, dy), (dx + 1, dy + 1)]:
        draw.text((x + sx, y + sy), text, fill=(0, 0, 0, 180), font=font)
    draw.text((x, y), text, fill=fill, font=font)
    return x, tw, th


# --------------------------------------------------------------------
# 1. CÓDIGO ASESINO — Mystery / Inca / Code
# --------------------------------------------------------------------
def cover_codigo_asesino():
    out = os.path.join(BASE, "codigo_asesino", "cover.jpg")
    img = Image.new("RGB", (W, H), (10, 5, 15))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        r = int(30 + (y / H) * 40)
        g = int(5 + (y / H) * 10)
        b = int(15 + (y / H) * 5)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Quipu vertical lines
    random.seed(123)
    for i in range(30):
        x = random.randint(50, W - 50)
        y0 = random.randint(200, H - 400)
        y1 = y0 + random.randint(200, 800)
        col = (random.randint(120, 180), random.randint(40, 80), random.randint(20, 40))
        draw.line([(x, y0), (x, y1)], fill=col, width=random.randint(2, 5))
        for ky in range(y0, y1, random.randint(40, 100)):
            r2 = random.randint(4, 8)
            draw.ellipse([x - r2, ky - r2, x + r2, ky + r2], fill=col)

    # Code lines
    f_code = load_font("consola.ttf", 18)
    code_snippets = [
        "quipu = {nudo: valor for nudo, valor in enumerate(misterio)}",
        "if 'Qhapaq Nan' in ruta_inca: print('Descifrado')",
        "def descifrar(codigo, clave_inka):",
        "   return [c ^ k for c, k in zip(codigo, clave_inka)]",
        "sospechosos = [Inti, Qori, Tupac, el_arqueologo]",
        "with open('codigo_asesino.txt', 'rb') as f: evidencia = f.read()",
        "clave = sum([ord(c) for c in palabra_secreta]) % 256",
    ]
    random.seed(456)
    for line in code_snippets:
        x = random.randint(40, W - 400)
        y = random.randint(100, H - 100)
        draw.text((x, y), line, fill=(60, 40, 50), font=f_code)

    f_tit = load_font("consolab.ttf", 100)
    f_sub1 = load_font("calibri.ttf", 42)
    f_sub2 = load_font("calibri.ttf", 30)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "CÓDIGO ASESINO", f_tit, CY - 340, (200, 60, 50))
    text_center(draw, "El Enigma de Qhapaq Ñan", f_sub1, CY - 180, (200, 180, 150))
    text_center(draw, "Una Saga de Misterio, Tecnología", f_sub2, CY - 120, (150, 140, 130))
    text_center(draw, "y Memoria Ancestral", f_sub2, CY - 85, (150, 140, 130))

    draw.rectangle([CX - 120, CY - 40, CX + 120, CY - 36], fill=(200, 60, 50))

    quote = '"En los nudos del quipu se esconde la verdad."'
    text_center(draw, quote, f_sub2, CY + 10, (160, 130, 120))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (170, 170, 170))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] Código Asesino -> {out}")


# --------------------------------------------------------------------
# 2. CÓDIGO DE OLAS — Ocean / Surf / Tech
# --------------------------------------------------------------------
def cover_codigo_de_olas():
    out = os.path.join(BASE, "codigo_de_olas", "cover.jpg")
    img = Image.new("RGB", (W, H), (0, 20, 50))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        r = int(0 + (y / H) * 10)
        g = int(40 + (y / H) * 60)
        b = int(80 + (y / H) * 40)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    for wave in range(10):
        y_base = 300 + wave * 200
        amp = 30 + wave * 6
        freq = 0.005 + wave * 0.0008
        pts = []
        for x in range(0, W, 3):
            y = y_base + int(amp * math.sin(x * freq + wave * 1.5))
            pts.append((x, y))
        col = (60, 140 + wave * 8, 180 - wave * 4)
        draw.line(pts, fill=col, width=3)

    f_code = load_font("consola.ttf", 16)
    code_lines = [
        "ola = Ola(altura=2.5, direccion='noroeste', velocidad=12)",
        "surfista = Surfista('Mateo', nivel='intermedio')",
        "while ola.rompe(): surfista.remar(); surfista.tomar_ola()",
        "datos_puerto = pd.read_csv('embarcaciones.csv')",
        "if marea == 'alta' and viento < 15: print('Buen surfing!')",
        "secreto = descifrar_mensaje(ola.lleva_mensaje())",
    ]
    random.seed(789)
    for line in code_lines:
        x = random.randint(40, W - 400)
        y = random.randint(80, H - 80)
        draw.text((x, y), line, fill=(40, 80, 120), font=f_code)

    f_tit = load_font("consolab.ttf", 100)
    f_sub1 = load_font("calibri.ttf", 42)
    f_sub2 = load_font("calibri.ttf", 30)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "CÓDIGO DE OLAS", f_tit, CY - 340, (60, 190, 220))
    text_center(draw, "El Misterio del Puerto de Ancón", f_sub1, CY - 180, (180, 210, 230))
    text_center(draw, "Una Historia de Surf, Tecnología", f_sub2, CY - 120, (140, 170, 190))
    text_center(draw, "y el Secreto del Mar", f_sub2, CY - 85, (140, 170, 190))

    draw.rectangle([CX - 120, CY - 40, CX + 120, CY - 36], fill=(60, 190, 220))

    quote = '"Las olas tienen su propio lenguaje."'
    text_center(draw, quote, f_sub2, CY + 10, (150, 180, 200))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (160, 180, 190))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] Código de Olas -> {out}")


# --------------------------------------------------------------------
# 3. EL MOTOR CUANTITATIVO — Math / Data Science
# --------------------------------------------------------------------
def cover_motor_cuantitativo():
    out = os.path.join(BASE, "motor_cuantitativo", "cover.jpg")
    img = Image.new("RGB", (W, H), (5, 10, 25))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        r = int(8 + (y / H) * 15)
        g = int(15 + (y / H) * 25)
        b = int(35 + (y / H) * 20)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    for x in range(0, W, 50):
        draw.line([(x, 0), (x, H)], fill=(20, 30, 50), width=1)
    for y in range(0, H, 50):
        draw.line([(0, y), (W, y)], fill=(20, 30, 50), width=1)

    f_code = load_font("consola.ttf", 18)
    formulas = [
        "y = mx + b", "sum( (xi - mu)**2 ) / n",
        "P(A|B) = P(B|A)*P(A)/P(B)", "lim (x->inf) f(x)",
        "X_bar ~ N(mu, sigma/sqrt(n))", "R^2 = 1 - SS_res/SS_tot",
        "y_hat = sigmoid(X @ w + b)", "PCA: X = U * S * V^T",
        "K-means: min sum ||xi - cj||^2", "MSE = (1/n) * sum(yi - y_hati)^2",
        "t = (x1_bar - x2_bar) / sqrt(s1^2/n1 + s2^2/n2)",
        "p_value < 0.05 -> reject H0", "log(p/(1-p)) = X*beta",
    ]
    random.seed(111)
    for line in formulas:
        x = random.randint(30, W - 300)
        y = random.randint(60, H - 60)
        col = (random.randint(30, 60), random.randint(60, 100), random.randint(80, 140))
        draw.text((x, y), line, fill=col, font=f_code)

    # Bell curve
    curve_pts = []
    cx2, cy2 = W // 2, H - 350
    for x in range(-200, 201, 2):
        y = cy2 - int(150 * math.exp(-(x ** 2) / (2 * 70 ** 2)))
        curve_pts.append((cx2 + x, y))
    draw.line(curve_pts, fill=(80, 160, 220), width=3)

    f_tit = load_font("consolab.ttf", 90)
    f_sub1 = load_font("calibri.ttf", 36)
    f_sub2 = load_font("calibri.ttf", 28)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "El Motor Cuantitativo", f_tit, CY - 340, (80, 180, 240))
    text_center(draw, "Fundamentos Matemáticos y Estadísticos", f_sub1, CY - 200, (170, 200, 220))
    text_center(draw, "con Python para el Análisis de Datos", f_sub1, CY - 155, (170, 200, 220))

    draw.rectangle([CX - 120, CY - 110, CX + 120, CY - 106], fill=(80, 180, 240))

    text_center(draw, "Alex Goyzueta Delgado", f_aut, CY - 50, (170, 200, 220))
    text_center(draw, "Analista de Datos Senior & Instructor", f_sub2, CY - 10, (130, 160, 180))
    text_center(draw, "2026", f_sub2, H - 100, (120, 140, 160))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] Motor Cuantitativo -> {out}")


# --------------------------------------------------------------------
# 4. RAÍCES NUEVAS — Self-help / Roots / Growth
# --------------------------------------------------------------------
def cover_raices_nuevas():
    out = os.path.join(BASE, "raices_nuevas", "cover.jpg")
    img = Image.new("RGB", (W, H), (15, 30, 15))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        r = int(20 + (y / H) * 30)
        g = int(45 + (y / H) * 50)
        b = int(25 + (y / H) * 20)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Roots growing from bottom
    random.seed(222)
    for i in range(50):
        x = random.randint(50, W - 50)
        y_start = H - random.randint(100, 300)
        y_end = random.randint(100, H - 500)
        curve_w = random.randint(15, 60)
        col = (random.randint(40, 80), random.randint(80, 140), random.randint(30, 60))
        pts = []
        for t in range(101):
            p = t / 100
            px = x + int(curve_w * math.sin(p * math.pi * (2 + i % 3)))
            py = int(y_start + (y_end - y_start) * p)
            pts.append((px, py))
        draw.line(pts, fill=col, width=random.randint(2, 5))
        if random.random() < 0.3:
            lx, ly = pts[-1]
            for _ in range(3):
                lx2 = lx + random.randint(-15, 15)
                ly2 = ly + random.randint(-15, 0)
                draw.ellipse([lx2 - 3, ly2 - 3, lx2 + 3, ly2 + 3], fill=(60, 140, 50))

    # Warm sun circle
    for r in range(350, 0, -3):
        ratio = r / 350
        alpha = int(12 * (1 - ratio))
        if alpha <= 0:
            continue
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        cr = int(200 + 55 * (1 - ratio))
        cg = int(160 + 40 * (1 - ratio))
        cb = int(60 + 20 * (1 - ratio))
        od.ellipse([CX - r, 300 - r, CX + r, 300 + r], fill=(cr, cg, cb, alpha))
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        draw = ImageDraw.Draw(img)

    # Leaves
    for x, y, s in [(200, 300, 6), (W - 200, 250, 5), (250, 380, 4)]:
        draw.ellipse([x - s * 2, y - s, x + s * 2, y + s], fill=(80, 160, 60))
        draw.line([(x, y), (x - s * 2, y - s * 3)], fill=(60, 120, 40), width=2)

    f_tit = load_font("consolab.ttf", 100)
    f_sub1 = load_font("calibri.ttf", 40)
    f_sub2 = load_font("calibri.ttf", 32)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "RAÍCES NUEVAS", f_tit, CY - 300, (160, 210, 100))
    text_center(draw, "Guía Práctica para Combatir", f_sub1, CY - 160, (210, 220, 180))
    text_center(draw, "la Ansiedad del Inmigrante", f_sub1, CY - 120, (210, 220, 180))
    text_center(draw, "Lo que me hubiera gustado saber cuando llegué", f_sub2, CY - 60, (180, 190, 150))

    draw.rectangle([CX - 120, CY - 20, CX + 120, CY - 16], fill=(160, 210, 100))

    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (200, 210, 180))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] Raíces Nuevas -> {out}")


# --------------------------------------------------------------------
# 5. ESTADÍSTICA MORTAL — Stats / Probability / Crime
# --------------------------------------------------------------------
def cover_estadistica_mortal():
    out = os.path.join(BASE, "estadistica_mortal", "cover.jpg")
    img = Image.new("RGB", (W, H), (10, 15, 30))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        r = int(15 + (y / H) * 20)
        g = int(20 + (y / H) * 30)
        b = int(45 + (y / H) * 25)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Grid background (data science feel)
    for x in range(0, W, 40):
        draw.line([(x, 0), (x, H)], fill=(20, 30, 50), width=1)
    for y in range(0, H, 40):
        draw.line([(0, y), (W, y)], fill=(20, 30, 50), width=1)

    # Bell curve
    curve_pts = []
    cx2, cy2 = W // 2, H - 450
    for x in range(-300, 301, 3):
        y = cy2 - int(200 * math.exp(-(x ** 2) / (2 * 90 ** 2)))
        curve_pts.append((cx2 + x, y))
    draw.line(curve_pts, fill=(220, 180, 60), width=4)

    # Shaded area under curve (tail)
    shade_pts = [(cx2 + 180, cy2)]
    for x in range(180, 301, 3):
        y = cy2 - int(200 * math.exp(-(x ** 2) / (2 * 90 ** 2)))
        shade_pts.append((cx2 + x, y))
    shade_pts.append((cx2 + 300, cy2))
    draw.polygon(shade_pts, fill=(220, 180, 60, 40))

    # Code snippets
    f_code = load_font("consola.ttf", 17)
    formulas = [
        "datos = []", "mean = sum(x) / len(x)",
        "P(A|B) = P(B|A)*P(A)/P(B)", "z = (x - mu) / sigma",
        "H0: mu == 0, H1: mu != 0", "r = cov(X,Y) / (sx * sy)",
        "chi2 = sum((O-E)**2 / E)", "Y = mX + b",
    ]
    import random as rnd
    rnd.seed(333)
    for line in formulas:
        x = rnd.randint(30, W - 300)
        y = rnd.randint(70, H - 70)
        col = (rnd.randint(40, 70), rnd.randint(60, 100), rnd.randint(90, 150))
        draw.text((x, y), line, fill=col, font=f_code)

    f_tit = load_font("consolab.ttf", 90)
    f_sub1 = load_font("calibri.ttf", 38)
    f_sub2 = load_font("calibri.ttf", 30)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "ESTADÍSTICA MORTAL", f_tit, CY - 340, (220, 180, 60))
    text_center(draw, "El Enigma del Conjunto Vacío", f_sub1, CY - 200, (200, 200, 220))
    text_center(draw, "Una Novela de Misterio, Datos", f_sub2, CY - 145, (160, 170, 190))
    text_center(draw, "y Probabilidades", f_sub2, CY - 110, (160, 170, 190))

    draw.rectangle([CX - 120, CY - 65, CX + 120, CY - 61], fill=(220, 180, 60))

    quote = '"Los números no mienten. Las personas, sí."'
    text_center(draw, quote, f_sub2, CY - 15, (180, 180, 200))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (180, 180, 190))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] Estadística Mortal -> {out}")


# --------------------------------------------------------------------
# 6. SQL LETAL — SQL / Database / Crime
# --------------------------------------------------------------------
def cover_sql_letal():
    out = os.path.join(BASE, "sql_letal", "cover.jpg")
    img = Image.new("RGB", (W, H), (5, 20, 30))
    draw = ImageDraw.Draw(img)

    # Dark terminal-style background
    for y in range(H):
        r = int(8 + (y / H) * 10)
        g = int(25 + (y / H) * 20)
        b = int(35 + (y / H) * 25)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Grid lines (database schema feel)
    for x in range(0, W, 30):
        draw.line([(x, 0), (x, H)], fill=(10, 35, 50), width=1)
    for y in range(0, H, 30):
        draw.line([(0, y), (W, y)], fill=(10, 35, 50), width=1)

    # SQL code snippets scattered in background
    f_code = load_font("consola.ttf", 16)
    snippets = [
        "SELECT * FROM crimenes;",
        "JOIN sospechosos ON id = caso_id",
        "WHERE fecha > '2026-07-14'",
        "GROUP BY usuario HAVING COUNT(*) > 5",
        "ORDER BY monto DESC LIMIT 1",
        "CREATE TABLE evidencias (...);",
        "INSERT INTO auditoria VALUES (...)",
        "WITH RECURSIVE organigrama AS (...)",
        "ROW_NUMBER() OVER (PARTITION BY...)",
        "LAG(fecha) OVER (ORDER BY fecha)",
    ]
    import random as rnd
    rnd.seed(444)
    for line in snippets:
        x = rnd.randint(30, W - 350)
        y = rnd.randint(60, H - 60)
        col = (rnd.randint(15, 40), rnd.randint(45, 80), rnd.randint(60, 100))
        draw.text((x, y), line, fill=col, font=f_code)

    # Database icon (simplified cylinder)
    cx_db, cy_db = W // 2, H - 400
    # Cylinder top ellipse
    draw.ellipse([cx_db - 120, cy_db - 30, cx_db + 120, cy_db + 5], fill=(0, 60, 80), outline=(30, 120, 160), width=2)
    # Cylinder body
    draw.rectangle([cx_db - 120, cy_db + 5, cx_db + 120, cy_db + 120], fill=(0, 50, 70), outline=(30, 120, 160), width=2)
    # Cylinder bottom ellipse
    draw.ellipse([cx_db - 120, cy_db + 95, cx_db + 120, cy_db + 130], fill=(0, 60, 80), outline=(30, 120, 160), width=2)

    # Key icon inside cylinder (unlocking data)
    draw.rectangle([cx_db - 15, cy_db + 20, cx_db - 5, cy_db + 60], fill=(200, 180, 60), width=0)
    draw.ellipse([cx_db - 25, cy_db + 50, cx_db + 5, cy_db + 80], fill=(200, 180, 60), width=0)
    draw.rectangle([cx_db + 10, cy_db + 40, cx_db + 35, cy_db + 48], fill=(200, 180, 60), width=0)
    draw.rectangle([cx_db + 10, cy_db + 48, cx_db + 18, cy_db + 56], fill=(200, 180, 60), width=0)

    f_tit = load_font("consolab.ttf", 85)
    f_sub1 = load_font("calibri.ttf", 36)
    f_sub2 = load_font("calibri.ttf", 30)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "SQL LETAL", f_tit, CY - 340, (30, 180, 220))
    text_center(draw, "El Misterio de la Base de Datos", f_sub1, CY - 200, (200, 210, 220))
    text_center(draw, "Una Novela de Misterio, Datos", f_sub2, CY - 145, (140, 170, 190))
    text_center(draw, "y Consultas", f_sub2, CY - 110, (140, 170, 190))

    draw.rectangle([CX - 120, CY - 65, CX + 120, CY - 61], fill=(30, 180, 220))

    quote = '"SELECT la verdad FROM los datos"'
    text_center(draw, quote, f_sub2, CY - 15, (160, 190, 210))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (160, 180, 190))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] SQL Letal -> {out}")


# --------------------------------------------------------------------
# 7. EXCEL BÁSICO — Spreadsheet / Green / Foundation
# --------------------------------------------------------------------
def cover_excel_basico():
    out = os.path.join(BASE, "excel_basico", "cover.jpg")
    img = Image.new("RGB", (W, H), (10, 30, 15))
    draw = ImageDraw.Draw(img)

    # Green gradient background
    for y in range(H):
        r = int(12 + (y / H) * 25)
        g = int(45 + (y / H) * 50)
        b = int(20 + (y / H) * 20)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Spreadsheet grid pattern
    for x in range(0, W, 60):
        draw.line([(x, 0), (x, H)], fill=(20, 55, 30), width=1)
    for y in range(0, H, 40):
        draw.line([(0, y), (W, y)], fill=(20, 55, 30), width=1)

    # Highlight some cells like a spreadsheet selection
    random.seed(101)
    for _ in range(15):
        cell_x = random.randint(0, 25) * 60
        cell_y = random.randint(0, 60) * 40
        col = (random.randint(40, 80), random.randint(140, 200), random.randint(40, 80))
        draw.rectangle([cell_x, cell_y, cell_x + 58, cell_y + 38], fill=col, outline=(60, 180, 80))

    # Code snippets
    f_code = load_font("consola.ttf", 16)
    snippets = [
        "=SUMA(A1:A10)", "=PROMEDIO(B1:B20)",
        "=A1*B1", "=SI(C2>100,\"OK\",\"Revisar\")",
        "Cédula activa: A1", "Tabla: Inventario_Taller",
        "=CONTAR(D1:D50)", "Ordenar por Cantidad",
        "Filtro: Producto > Madera", "Gráfico de barras",
    ]
    random.seed(202)
    for line in snippets:
        x = random.randint(30, W - 350)
        y = random.randint(70, H - 70)
        col = (random.randint(30, 60), random.randint(60, 100), random.randint(30, 50))
        draw.text((x, y), line, fill=col, font=f_code)

    # Formula bar visual
    bar_y = H - 250
    draw.rectangle([200, bar_y, W - 200, bar_y + 40], fill=(20, 50, 30), outline=(50, 140, 70), width=2)
    f_fx = load_font("consola.ttf", 22)
    draw.text((220, bar_y + 8), "fx  =SUMA(Inventario[Precio])", fill=(100, 220, 120), font=f_fx)

    f_tit = load_font("consolab.ttf", 100)
    f_sub1 = load_font("calibri.ttf", 40)
    f_sub2 = load_font("calibri.ttf", 30)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "EXCEL BÁSICO", f_tit, CY - 340, (80, 220, 100))
    text_center(draw, "El Legado de las Fórmulas", f_sub1, CY - 190, (180, 230, 190))
    text_center(draw, "Una Novela para Aprender", f_sub2, CY - 130, (150, 200, 165))
    text_center(draw, "Excel Desde Cero", f_sub2, CY - 95, (150, 200, 165))

    draw.rectangle([CX - 120, CY - 50, CX + 120, CY - 46], fill=(80, 220, 100))

    quote = '"Aprende Excel, salva el taller."'
    text_center(draw, quote, f_sub2, CY + 5, (160, 210, 175))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (160, 200, 170))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] Excel Básico -> {out}")


# --------------------------------------------------------------------
# 8. EXCEL INTERMEDIO — Spreadsheet / Blue / Analysis
# --------------------------------------------------------------------
def cover_excel_intermedio():
    out = os.path.join(BASE, "excel_intermedio", "cover.jpg")
    img = Image.new("RGB", (W, H), (10, 15, 40))
    draw = ImageDraw.Draw(img)

    # Blue gradient background
    for y in range(H):
        r = int(10 + (y / H) * 15)
        g = int(20 + (y / H) * 30)
        b = int(50 + (y / H) * 45)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Pivot table grid
    for x in range(0, W, 50):
        draw.line([(x, 0), (x, H)], fill=(15, 30, 55), width=1)
    for y in range(0, H, 50):
        draw.line([(0, y), (W, y)], fill=(15, 30, 55), width=1)

    # Pivot table style blocks
    random.seed(303)
    for row in range(8):
        for col in range(5):
            x = 100 + col * 140
            y = 300 + row * 60
            if random.random() < 0.6:
                col_bright = random.randint(30, 80)
                draw.rectangle([x, y, x + 135, y + 55], fill=(col_bright, col_bright + 20, col_bright + 60), outline=(50, 80, 140))

    # Chart visualization
    chart_x, chart_y = W // 2, H - 380
    bar_colors = [(80, 140, 220), (60, 180, 220), (100, 200, 180), (120, 160, 240), (70, 190, 200)]
    bar_w = 30
    for i, h in enumerate([80, 140, 100, 180, 120]):
        x = chart_x - 100 + i * 45
        draw.rectangle([x, chart_y - h, x + bar_w, chart_y], fill=bar_colors[i], outline=(150, 200, 255), width=1)

    f_code = load_font("consola.ttf", 16)
    snippets = [
        "=BUSCARV(A2,Tabla,2,FALSO)", "=BUSCARX(A2,Tabla[ID],Tabla[Valor])",
        "TABLA DINÁMICA: Suma de Ventas", "=INDICE(B:B,COINCIDIR(D2,A:A,0))",
        "Filtro: Fecha > 01/01/2024", "Segmentador de datos: Producto",
    ]
    random.seed(404)
    for line in snippets:
        x = random.randint(30, W - 400)
        y = random.randint(80, H - 80)
        col = (random.randint(30, 60), random.randint(50, 90), random.randint(90, 140))
        draw.text((x, y), line, fill=col, font=f_code)

    f_tit = load_font("consolab.ttf", 90)
    f_sub1 = load_font("calibri.ttf", 38)
    f_sub2 = load_font("calibri.ttf", 28)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "EXCEL INTERMEDIO", f_tit, CY - 340, (60, 180, 240))
    text_center(draw, "Los Secretos de la Hoja", f_sub1, CY - 200, (180, 210, 230))
    text_center(draw, "Una Novela para Dominar", f_sub2, CY - 145, (140, 170, 200))
    text_center(draw, "el Análisis de Datos en Excel", f_sub2, CY - 110, (140, 170, 200))

    draw.rectangle([CX - 120, CY - 65, CX + 120, CY - 61], fill=(60, 180, 240))

    quote = '"Los datos guardan secretos. Las fórmulas los revelan."'
    text_center(draw, quote, f_sub2, CY - 15, (150, 190, 220))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (150, 180, 200))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] Excel Intermedio -> {out}")


# --------------------------------------------------------------------
# 9. EXCEL AVANZADO — Dark / Gold / Power
# --------------------------------------------------------------------
def cover_excel_avanzado():
    out = os.path.join(BASE, "excel_avanzado", "cover.jpg")
    img = Image.new("RGB", (W, H), (15, 10, 25))
    draw = ImageDraw.Draw(img)

    # Dark gradient background
    for y in range(H):
        r = int(15 + (y / H) * 20)
        g = int(10 + (y / H) * 15)
        b = int(30 + (y / H) * 30)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Power Query flow lines
    random.seed(505)
    for i in range(20):
        x_start = random.randint(50, W - 50)
        x_end = random.randint(50, W - 50)
        y_pos = random.randint(300, H - 200)
        col = (random.randint(40, 70), random.randint(80, 130), random.randint(140, 200))
        draw.line([(x_start, y_pos), (x_start + 50, y_pos - 20), (x_end - 50, y_pos + 20), (x_end, y_pos)], fill=col, width=2)
        draw.ellipse([x_end - 5, y_pos - 5, x_end + 5, y_pos + 5], fill=col)

    # DAX / VBA code blocks
    f_code = load_font("consola.ttf", 16)
    snippets = [
        "CALCULATE(SUM(Ventas[Monto]), FILTER(...))",
        "Sub ProcesarDatos()", "For Each celda In Range(\"A1:A100\")",
        "=LET(x, FILTER(Tabla, Tabla[Year]=2024), SORT(x))",
        "Power Query: M language", "=LAMBDA(x, x*2)(5)",
        "VAR Total = SUMX(Ventas, Ventas[Cant]*Ventas[Precio])",
        "Solver: Max Z = 3x + 5y",
    ]
    random.seed(606)
    for line in snippets:
        x = random.randint(30, W - 450)
        y = random.randint(60, H - 60)
        col = (random.randint(40, 70), random.randint(50, 90), random.randint(80, 130))
        draw.text((x, y), line, fill=col, font=f_code)

    # VBA window visual
    vba_x, vba_y = 200, H - 350
    draw.rectangle([vba_x, vba_y, vba_x + 500, vba_y + 180], fill=(5, 5, 20), outline=(100, 100, 180), width=2)
    draw.rectangle([vba_x, vba_y, vba_x + 500, vba_y + 25], fill=(30, 30, 60), outline=(100, 100, 180), width=1)
    f_vba = load_font("consola.ttf", 14)
    vba_lines = [
        "Sub AnalizarDatos()",
        "  Dim ws As Worksheet",
        "  Set ws = ThisWorkbook.Sheets(1)",
        "  ws.Range(\"A1\").Value = \"Completado\"",
        "End Sub",
    ]
    for i, line in enumerate(vba_lines):
        draw.text((vba_x + 10, vba_y + 30 + i * 25), line, fill=(130, 200, 130), font=f_vba)

    f_tit = load_font("consolab.ttf", 90)
    f_sub1 = load_font("calibri.ttf", 38)
    f_sub2 = load_font("calibri.ttf", 28)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "EXCEL AVANZADO", f_tit, CY - 340, (200, 180, 60))
    text_center(draw, "El Poder del Análisis", f_sub1, CY - 200, (210, 200, 150))
    text_center(draw, "Una Novela para Convertirte", f_sub2, CY - 145, (170, 170, 140))
    text_center(draw, "en un Experto en Análisis de Datos", f_sub2, CY - 110, (170, 170, 140))

    draw.rectangle([CX - 120, CY - 65, CX + 120, CY - 61], fill=(200, 180, 60))

    quote = '"El conocimiento es poder. El análisis es libertad."'
    text_center(draw, quote, f_sub2, CY - 15, (180, 175, 130))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (170, 165, 140))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] Excel Avanzado -> {out}")


# --------------------------------------------------------------------
# 10. EXCEL CON COPILOT — AI / Purple / Futuristic
# --------------------------------------------------------------------
def cover_excel_copilot():
    out = os.path.join(BASE, "excel_copilot", "cover.jpg")
    img = Image.new("RGB", (W, H), (10, 5, 25))
    draw = ImageDraw.Draw(img)

    # Purple-blue gradient background
    for y in range(H):
        r = int(15 + (y / H) * 40)
        g = int(5 + (y / H) * 20)
        b = int(40 + (y / H) * 60)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Neural network / circuit patterns
    random.seed(707)
    for i in range(25):
        x1 = random.randint(50, W - 50)
        y1 = random.randint(50, H - 50)
        x2 = random.randint(50, W - 50)
        y2 = random.randint(50, H - 50)
        col = (random.randint(40, 80), random.randint(20, 60), random.randint(80, 140))
        draw.line([(x1, y1), (x2, y2)], fill=col, width=1)
        draw.ellipse([x1 - 4, y1 - 4, x1 + 4, y1 + 4], fill=(80, 60, 180))
        draw.ellipse([x2 - 2, y2 - 2, x2 + 2, y2 + 2], fill=(100, 80, 200))

    # Glowing circle (AI / Copilot icon representation)
    for r in range(200, 0, -2):
        ratio = r / 200
        alpha = int(8 * (1 - ratio))
        if alpha <= 0:
            continue
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(overlay)
        cr = int(120 + 60 * (1 - ratio))
        cg = int(60 + 40 * (1 - ratio))
        cb = int(200 + 55 * (1 - ratio))
        od.ellipse([CX - r, H - 500 - r, CX + r, H - 500 + r], fill=(cr, cg, cb, alpha))
        img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
        draw = ImageDraw.Draw(img)

    # Code / prompt snippets
    f_code = load_font("consola.ttf", 16)
    snippets = [
        "Hola, Copilot: analiza estos datos",
        "¿Cuáles son las tendencias?",
        "Genera un gráfico de ventas",
        "Copilot: limpia esta tabla",
        "=SUMAPRODUCTO((A:A)*(B:B))",
        "Segmentar por región y mes",
        "Dashboard interactivo con IA",
        "Power Query + Copilot = magia",
        "Prompt: mejora este reporte",
    ]
    random.seed(808)
    for line in snippets:
        x = random.randint(30, W - 400)
        y = random.randint(80, H - 80)
        col = (random.randint(60, 100), random.randint(40, 80), random.randint(100, 160))
        draw.text((x, y), line, fill=col, font=f_code)

    # Chat input bar visual
    bar_y = H - 300
    draw.rectangle([250, bar_y, W - 250, bar_y + 45], fill=(15, 10, 40), outline=(100, 80, 200), width=2)
    f_chat = load_font("consola.ttf", 20)
    draw.text((270, bar_y + 10), "> Copilot: ¿En qué puedo ayudarte?", fill=(140, 120, 240), font=f_chat)

    f_tit = load_font("consolab.ttf", 90)
    f_sub1 = load_font("calibri.ttf", 40)
    f_sub2 = load_font("calibri.ttf", 30)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "EXCEL CON COPILOT", f_tit, CY - 340, (140, 100, 240))
    text_center(draw, "Tu Asistente Inteligente", f_sub1, CY - 200, (200, 180, 240))
    text_center(draw, "Una Novela para Dominar Excel", f_sub2, CY - 140, (170, 150, 210))
    text_center(draw, "con Inteligencia Artificial", f_sub2, CY - 105, (170, 150, 210))

    draw.rectangle([CX - 120, CY - 60, CX + 120, CY - 56], fill=(140, 100, 240))

    quote = '"La mejor pregunta es la que nunca te atreviste a hacer."'
    text_center(draw, quote, f_sub2, CY - 5, (180, 160, 220))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (170, 160, 200))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] Excel con Copilot -> {out}")


# --------------------------------------------------------------------
# 11. HTML BÁSICO — Orange / Code Editor / Web
# --------------------------------------------------------------------
def cover_html_basico():
    out = os.path.join(BASE, "html_basico", "cover.jpg")
    img = Image.new("RGB", (W, H), (25, 15, 10))
    draw = ImageDraw.Draw(img)

    # Warm orange gradient
    for y in range(H):
        r = int(40 + (y / H) * 50)
        g = int(20 + (y / H) * 30)
        b = int(10 + (y / H) * 15)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Code editor line numbers (left margin)
    f_lnum = load_font("consola.ttf", 14)
    for i in range(0, H // 30):
        draw.text((20, 10 + i * 30), f"{i+1:>3}", fill=(100, 60, 40), font=f_lnum)

    # Angle bracket decorations scattered
    f_code = load_font("consola.ttf", 18)
    tags = [
        "<html>", "<head>", "<title>La Voz del Barrio</title>",
        "<body>", "<h1>Bienvenidos</h1>", "<p class=\"noticia\">",
        "<a href=\"index.html\">Inicio</a>", "<img src=\"foto.jpg\" alt=\"\">",
        "<table>", "<tr><td>Edición</td><td>2026</td></tr>",
        "<form action=\"/suscripcion\" method=\"post\">",
        "<input type=\"email\" name=\"correo\">",
        "<footer>© 2026 La Voz del Barrio</footer>",
        "</body>", "</html>",
    ]
    random.seed(909)
    for line in tags:
        x = random.randint(80, W - 400)
        y = random.randint(80, H - 80)
        col = (random.randint(120, 180), random.randint(60, 100), random.randint(30, 60))
        draw.text((x, y), line, fill=col, font=f_code)

    # Large angle brackets as decorative element
    f_bracket = load_font("consolab.ttf", 300)
    draw.text((60, 1800), "< / >", fill=(180, 100, 40, 40), font=f_bracket)

    # Web browser mockup bar
    bar_y = H - 280
    draw.rectangle([150, bar_y, W - 150, bar_y + 35], fill=(35, 25, 20), outline=(160, 100, 50), width=2)
    f_url = load_font("consola.ttf", 18)
    draw.text((170, bar_y + 7), "https://lavozdelbarrio.net", fill=(180, 160, 120), font=f_url)

    f_tit = load_font("consolab.ttf", 100)
    f_sub1 = load_font("calibri.ttf", 42)
    f_sub2 = load_font("calibri.ttf", 30)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "HTML BÁSICO", f_tit, CY - 340, (220, 140, 50))
    text_center(draw, "El Código de la Web", f_sub1, CY - 190, (230, 200, 150))
    text_center(draw, "Una Novela para Aprender", f_sub2, CY - 130, (200, 170, 130))
    text_center(draw, "HTML Desde Cero", f_sub2, CY - 95, (200, 170, 130))

    draw.rectangle([CX - 120, CY - 50, CX + 120, CY - 46], fill=(220, 140, 50))

    quote = '"Cada etiqueta es un ladrillo en la web."'
    text_center(draw, quote, f_sub2, CY + 5, (210, 180, 140))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (200, 180, 150))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] HTML Básico -> {out}")


# --------------------------------------------------------------------
# 12. CSS BÁSICO — Teal / Design / Style
# --------------------------------------------------------------------
def cover_css_basico():
    out = os.path.join(BASE, "css_basico", "cover.jpg")
    img = Image.new("RGB", (W, H), (10, 25, 30))
    draw = ImageDraw.Draw(img)

    # Teal gradient background
    for y in range(H):
        r = int(10 + (y / H) * 20)
        g = int(35 + (y / H) * 50)
        b = int(45 + (y / H) * 40)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # Color swatches as decorative boxes
    swatch_colors = [
        (220, 80, 60), (60, 180, 220), (80, 200, 100),
        (220, 180, 50), (180, 100, 220), (60, 200, 180),
        (240, 140, 60), (100, 140, 240), (200, 80, 140),
    ]
    random.seed(1111)
    for _ in range(20):
        sx = random.randint(50, W - 100)
        sy = random.randint(50, H - 100)
        sw = random.randint(30, 80)
        sh = random.randint(30, 80)
        col = random.choice(swatch_colors)
        alpha_col = (col[0], col[1], col[2])
        draw.rectangle([sx, sy, sx + sw, sy + sh], fill=alpha_col, outline=(255, 255, 255, 80), width=1)

    # CSS code snippets
    f_code = load_font("consola.ttf", 18)
    snippets = [
        "body { font-family: Georgia; }",
        ".noticia { color: #333; }",
        "#portada { background: #f0f0f0; }",
        "h1 { font-size: 2em; font-weight: bold; }",
        ".menu { display: flex; gap: 1rem; }",
        "@media (max-width: 768px) { ... }",
        ".grid { display: grid; grid-template-columns: 1fr 1fr; }",
        "a:hover { color: #c00; transition: 0.3s; }",
        ".card { box-shadow: 0 2px 8px rgba(0,0,0,0.1); }",
        "::before { content: \"<3\"; }",
    ]
    random.seed(1212)
    for line in snippets:
        x = random.randint(80, W - 400)
        y = random.randint(80, H - 80)
        col = (random.randint(40, 80), random.randint(80, 140), random.randint(100, 180))
        draw.text((x, y), line, fill=col, font=f_code)

    # CSS braces decorative
    f_brace = load_font("consolab.ttf", 280)
    draw.text((W - 300, 1800), "{ }", fill=(40, 140, 160, 40), font=f_brace)

    # Color picker wheel visual
    cw_x, cw_y = CX, H - 350
    for angle in range(0, 360, 30):
        import math as m
        rad = m.radians(angle)
        r = int(128 + 127 * m.sin(rad))
        g = int(128 + 127 * m.sin(rad + 2.094))
        b = int(128 + 127 * m.sin(rad + 4.188))
        for radd in range(50, 80, 3):
            px = cw_x + int(radd * m.cos(rad))
            py = cw_y + int(radd * m.sin(rad))
            draw.ellipse([px - 4, py - 4, px + 4, py + 4], fill=(r, g, b))

    f_tit = load_font("consolab.ttf", 95)
    f_sub1 = load_font("calibri.ttf", 40)
    f_sub2 = load_font("calibri.ttf", 30)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "CSS BÁSICO", f_tit, CY - 340, (60, 200, 220))
    text_center(draw, "El Diseño que Transforma la Web", f_sub1, CY - 190, (200, 220, 230))
    text_center(draw, "Una Novela para Aprender", f_sub2, CY - 130, (160, 200, 210))
    text_center(draw, "CSS Desde Cero", f_sub2, CY - 95, (160, 200, 210))

    draw.rectangle([CX - 120, CY - 50, CX + 120, CY - 46], fill=(60, 200, 220))

    quote = '"El diseño no es solo cómo se ve, sino cómo funciona."'
    text_center(draw, quote, f_sub2, CY + 5, (170, 210, 220))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (170, 200, 210))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] CSS Básico -> {out}")


# --------------------------------------------------------------------
# 13. JAVASCRIPT BÁSICO — Yellow / Gold / Interactive
# --------------------------------------------------------------------
def cover_js_basico():
    out = os.path.join(BASE, "js_basico", "cover.jpg")
    img = Image.new("RGB", (W, H), (25, 20, 5))
    draw = ImageDraw.Draw(img)

    # Warm gold gradient
    for y in range(H):
        r = int(35 + (y / H) * 45)
        g = int(25 + (y / H) * 35)
        b = int(8 + (y / H) * 15)
        draw.line([(0, y), (W, y)], fill=(r, g, b))

    # JavaScript code snippets
    f_code = load_font("consola.ttf", 17)
    snippets = [
        "let cursos = [];",
        "const API_URL = 'https://api.aprendeya.com';",
        "function calcularProgreso(usuario) {",
        "  return usuario.lecciones / usuario.total * 100;",
        "}",
        "document.querySelector('.btn').addEventListener('click', ...);",
        "fetch(API_URL + '/cursos').then(r => r.json());",
        "localStorage.setItem('progreso', JSON.stringify(datos));",
        "if (usuario.autenticado) { mostrarDashboard(); }",
        "const sumar = (a, b) => a + b;",
        "console.log('¡Hola, mundo!');",
    ]
    random.seed(1313)
    for line in snippets:
        x = random.randint(80, W - 450)
        y = random.randint(80, H - 80)
        col = (random.randint(120, 180), random.randint(100, 160), random.randint(40, 80))
        draw.text((x, y), line, fill=col, font=f_code)

    # Curly braces decoration
    f_brace = load_font("consolab.ttf", 260)
    draw.text((80, 1850), "{ }", fill=(180, 160, 50, 40), font=f_brace)

    # Function-like visual: console output lines
    console_y = H - 320
    draw.rectangle([180, console_y, W - 180, console_y + 120], fill=(15, 12, 5), outline=(180, 160, 60), width=2)
    draw.rectangle([180, console_y, W - 180, console_y + 25], fill=(40, 35, 20), outline=(180, 160, 60), width=1)
    f_cons = load_font("consola.ttf", 16)
    draw.text((195, console_y + 5), "Console — AprendeYa Platform", fill=(180, 180, 160), font=f_cons)
    draw.text((195, console_y + 35), "> Usuarios activos: 1,247", fill=(120, 220, 120), font=f_cons)
    draw.text((195, console_y + 60), "> Progreso promedio: 67%", fill=(120, 220, 120), font=f_cons)
    draw.text((195, console_y + 88), "> ¡Demo lista para inversores!", fill=(120, 220, 120), font=f_cons)

    f_tit = load_font("consolab.ttf", 90)
    f_sub1 = load_font("calibri.ttf", 40)
    f_sub2 = load_font("calibri.ttf", 30)
    f_aut = load_font("calibri.ttf", 28)

    shadow_text(draw, "JAVASCRIPT BÁSICO", f_tit, CY - 340, (220, 190, 50))
    text_center(draw, "El Poder de la Interactividad", f_sub1, CY - 190, (230, 220, 150))
    text_center(draw, "Una Novela para Aprender", f_sub2, CY - 130, (200, 190, 120))
    text_center(draw, "JavaScript Desde Cero", f_sub2, CY - 95, (200, 190, 120))

    draw.rectangle([CX - 120, CY - 50, CX + 120, CY - 46], fill=(220, 190, 50))

    quote = '"La web cobra vida cuando aprendes su idioma."'
    text_center(draw, quote, f_sub2, CY + 5, (210, 200, 130))
    text_center(draw, "Alex Goyzueta Delgado", f_aut, H - 120, (200, 190, 140))

    img.save(out, "JPEG", quality=94)
    print(f"[OK] JavaScript Básico -> {out}")


# --------------------------------------------------------------------
if __name__ == "__main__":
    cover_codigo_asesino()
    cover_codigo_de_olas()
    cover_motor_cuantitativo()
    cover_raices_nuevas()
    cover_estadistica_mortal()
    cover_sql_letal()
    cover_excel_basico()
    cover_excel_intermedio()
    cover_excel_avanzado()
    cover_excel_copilot()
    cover_html_basico()
    cover_css_basico()
    cover_js_basico()
    print("\nTodas las portadas generadas.")
