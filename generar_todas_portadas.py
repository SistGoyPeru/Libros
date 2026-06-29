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
if __name__ == "__main__":
    cover_codigo_asesino()
    cover_codigo_de_olas()
    cover_motor_cuantitativo()
    cover_raices_nuevas()
    cover_estadistica_mortal()
    cover_sql_letal()
    print("\nTodas las portadas generadas.")
