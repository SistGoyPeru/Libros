from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# Colors
DARK_BG = "#0D1117"
ACCENT_BLUE = "#58A6FF"
ACCENT_GREEN = "#3FB950"
ACCENT_PURPLE = "#BC8CFF"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#8B949E"
CARD_BG = "#161B22"

width, height = 1600, 2560
img = Image.new("RGB", (width, height), DARK_BG)
draw = ImageDraw.Draw(img)

# Background gradient with subtle grid pattern
for y in range(height):
    progress = y / height
    r = int(13 * (1 - progress) + 22 * progress)
    g = int(17 * (1 - progress) + 27 * progress)
    b = int(23 * (1 - progress) + 34 * progress)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# Grid lines
for x in range(0, width, 40):
    draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 3), width=1)
for y in range(0, height, 40):
    draw.line([(0, y), (width, y)], fill=(255, 255, 255, 3), width=1)

# Decorative top bar
for i in range(3):
    bar_y = 40 + i * 8
    draw.rectangle([(0, bar_y), (width, bar_y + 4)], fill=ACCENT_BLUE, width=0)

# Decorative accent circles
draw.ellipse([(1400, 180), (1500, 280)], fill=ACCENT_PURPLE, outline=None)
draw.ellipse([(1350, 130), (1420, 200)], fill=ACCENT_GREEN, outline=None)

# Collection badge
try:
    font_badge = ImageFont.truetype("arial.ttf", 28)
except:
    font_badge = ImageFont.load_default()
draw.text((80, 80), "COLECCIÓN DATA & ANALYTICS MASTERY", fill=ACCENT_BLUE, font=font_badge)

# Book number badge
badge_x, badge_y = 80, 140
draw.rounded_rectangle([(badge_x, badge_y), (badge_x + 160, badge_y + 50)], radius=25, fill=ACCENT_PURPLE, outline=None)
try:
    font_badge_num = ImageFont.truetype("arial.ttf", 24)
except:
    font_badge_num = ImageFont.load_default()
draw.text((badge_x + 18, badge_y + 12), "LIBRO 5 DE 5", fill=WHITE, font=font_badge_num)

# Main title
try:
    font_title = ImageFont.truetype("arialbd.ttf", 92)
except:
    font_title = ImageFont.load_default()
title = "Big Data, ML e IA"
title_x = 80
title_y = 280
draw.text((title_x, title_y), title, fill=WHITE, font=font_title)

# Title underline accent
draw.rectangle([(80, title_y + 110), (550, title_y + 118)], fill=ACCENT_BLUE, width=0)

# Subtitle
try:
    font_subtitle = ImageFont.truetype("arial.ttf", 36)
except:
    font_subtitle = ImageFont.load_default()
subtitle = "Domina el big data, machine learning"
subtitle2 = "e inteligencia artificial con proyectos prácticos"
draw.text((80, title_y + 150), subtitle, fill=LIGHT_GRAY, font=font_subtitle)
draw.text((80, title_y + 195), subtitle2, fill=LIGHT_GRAY, font=font_subtitle)

# Tech stack tags
tags = ["PySpark", "Scikit-learn", "TensorFlow", "MLflow", "Vertex AI", "LLMs"]
tag_y = title_y + 290
try:
    font_tag = ImageFont.truetype("arial.ttf", 22)
except:
    font_tag = ImageFont.load_default()
tag_x = 80
for tag in tags:
    tw = draw.textlength(tag, font=font_tag) + 40
    draw.rounded_rectangle([(tag_x, tag_y), (tag_x + tw, tag_y + 40)], radius=20, fill=CARD_BG, outline=ACCENT_BLUE)
    draw.text((tag_x + 20, tag_y + 8), tag, fill=ACCENT_BLUE, font=font_tag)
    tag_x += tw + 15

# Decorative circuit-line paths
points = [(80, 700), (400, 700), (500, 800), (600, 750), (750, 850)]
for i in range(len(points) - 1):
    draw.line([points[i], points[i + 1]], fill=ACCENT_GREEN, width=3)
for pt in points:
    draw.ellipse([(pt[0] - 6, pt[1] - 6), (pt[0] + 6, pt[1] + 6)], fill=ACCENT_GREEN)

# Three project cards
projects = [
    ("Proyecto 1", "Big Data", "PySpark, Streaming, ETL escalable", ACCENT_BLUE),
    ("Proyecto 2", "ML", "Supervisado, No Supervisado, Tuning", ACCENT_GREEN),
    ("Proyecto 3", "DL & MLOps", "TensorFlow, NLP, MLflow, Vertex AI", ACCENT_PURPLE),
    ("Proyecto 4", "IA Generativa", "LLMs, RAG, BigQuery ML, LangChain", "#FF7B72"),
]
card_w = 340
card_h = 200
card_gap = 30
total_w = 4 * card_w + 3 * card_gap
start_x = (width - total_w) // 2
card_y = 900

for i, (proj, topic, desc, color) in enumerate(projects):
    cx = start_x + i * (card_w + card_gap)
    # Card background
    draw.rounded_rectangle([(cx, card_y), (cx + card_w, card_y + card_h)], radius=12, fill=CARD_BG, outline=color)
    # Number circle
    draw.ellipse([(cx + 20, card_y + 20), (cx + 50, card_y + 50)], fill=color, outline=None)
    try:
        font_num = ImageFont.truetype("arialbd.ttf", 24)
    except:
        font_num = ImageFont.load_default()
    draw.text((cx + 30, card_y + 25), str(i + 1), fill=DARK_BG, font=font_num)
    # Title
    try:
        font_proj = ImageFont.truetype("arialbd.ttf", 26)
    except:
        font_proj = ImageFont.load_default()
    draw.text((cx + 20, card_y + 70), proj, fill=WHITE, font=font_proj)
    # Topic
    try:
        font_topic = ImageFont.truetype("arial.ttf", 32)
    except:
        font_topic = ImageFont.load_default()
    draw.text((cx + 20, card_y + 105), topic, fill=color, font=font_topic)
    # Desc
    try:
        font_desc = ImageFont.truetype("arial.ttf", 18)
    except:
        font_desc = ImageFont.load_default()
    draw.text((cx + 20, card_y + 150), desc, fill=LIGHT_GRAY, font=font_desc)

# Large TechStore dataset section
ds_y = 1200
draw.rounded_rectangle([(80, ds_y), (width - 80, ds_y + 200)], radius=16, fill=CARD_BG, outline=ACCENT_GREEN)
try:
    font_ds_title = ImageFont.truetype("arialbd.ttf", 32)
except:
    font_ds_title = ImageFont.load_default()
draw.text((120, ds_y + 30), "DATASET CENTRAL: TECHSTORE", fill=ACCENT_GREEN, font=font_ds_title)
try:
    font_ds_desc = ImageFont.truetype("arial.ttf", 24)
except:
    font_ds_desc = ImageFont.load_default()
ds_texts = [
    "→ Evolución del dataset a lo largo de la colección completa",
    "→ ML predictions, segmentación de clientes, forecasting de ventas",
    "→ NLP sobre reseñas, RAG con documentación, recomendaciones",
]
for j, t in enumerate(ds_texts):
    draw.text((120, ds_y + 80 + j * 36), t, fill=LIGHT_GRAY, font=font_ds_desc)

# Author and footer
try:
    font_author = ImageFont.truetype("arial.ttf", 28)
except:
    font_author = ImageFont.load_default()
draw.text((80, 2200), "Alex Goyzueta Delgado", fill=WHITE, font=font_author)
draw.text((80, 2240), "Data & Analytics Mastery", fill=LIGHT_GRAY, font=font_author)

# Bottom accent bar
draw.rectangle([(0, height - 80), (width, height - 70)], fill=ACCENT_BLUE, width=0)

# Save
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cover.jpg")
img.save(output_path, "JPEG", quality=95)
print(f"Portada generada: {output_path}")
