import os
import re
from fpdf import FPDF
from ebooklib import epub

BOOK_DIR = r"C:\Users\alexg\OneDrive\Alex_2026\libros epub\print_Sigo_Aqui"
OUTPUT_DIR = BOOK_DIR

FONT_DIR = "C:\\Windows\\Fonts"

CHAPTER_FILES = [
    ("00_prologo.md", "Prólogo"),
    ("01_capitulo1_llegada_madrid.md", "Capítulo 1: Madrid"),
    ("02_capitulo2_naranjas_amargas.md", "Capítulo 2: Naranjas Amargas"),
    ("03_capitulo3_polvo_y_cemento.md", "Capítulo 3: Polvo, Pintura y Promesas Rotas"),
    ("04_capitulo4_fibra_en_el_norte.md", "Capítulo 4: Fibra en el Paraíso Verde"),
    ("05_capitulo5_si_reclamas_me_consigo_a_otro.md", "Capítulo 5: Si Reclamas, Me Consigo a Otro"),
    ("06_capitulo6_codigo_en_la_madrugada.md", "Capítulo 6: Código en la Madrugada"),
    ("07_capitulo7_la_entrevista.md", "Capítulo 7: La Entrevista"),
    ("08_capitulo8_los_papeles.md", "Capítulo 8: El Sí"),
    ("09_capitulo9_data_analyst.md", "Capítulo 9: Data Analyst"),
    ("10_epilogo.md", "Epílogo: Las Naranjas Dulces"),
    ("11_apendice_recursos.md", "Apéndice: Recursos"),
    ("12_sobre_el_autor.md", "Sobre el Autor"),
]

TITLE = "print(\"Sigo Aquí\")"
SUBTITLE = "El viaje de un informático sin papeles que cruzó España\npara salvar a quien amaba"
AUTHOR = "Alex Goyzueta Delgado"


def md_to_html(md_text):
    """Convert simple markdown to HTML"""
    html = md_text

    html = html.replace("&", "&amp;")
    html = html.replace("<", "&lt;")
    html = html.replace(">", "&gt;")

    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)

    html = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', html)
    html = re.sub(r'\*(.+?)\*', r'<i>\1</i>', html)

    html = re.sub(r'^---$', r'<hr/>', html, flags=re.MULTILINE)

    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)

    html = re.sub(r'```(\w*)\n(.*?)```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)

    html = re.sub(r'^(.+?)$', r'<p>\1</p>', html, flags=re.MULTILINE)

    return f"<html><body>{html}</body></html>"


def create_epub():
    book = epub.EpubBook()
    book.set_identifier("naranjas-fibra-codigo")
    book.set_title(TITLE)
    book.set_language("es")
    book.add_author(AUTHOR)

    book.add_metadata("DC", "description", "El viaje de un informático sin papeles que cruzó España para salvar a quien amaba")

    css = """
    body { font-family: Georgia, serif; line-height: 1.6; }
    h1 { color: #2c3e50; }
    h2 { color: #34495e; }
    pre { background-color: #f4f4f4; padding: 10px; border-left: 3px solid #e67e22; font-size: 0.9em; white-space: pre-wrap; }
    code { font-family: Consolas, monospace; }
    hr { border: 0; border-top: 1px solid #ccc; margin: 20px 0; }
    p { text-align: justify; }
    li { margin-bottom: 5px; }
    """
    nav_css = epub.EpubItem(uid="style", file_name="style.css", media_type="text/css", content=css)
    book.add_item(nav_css)

    chapters_epub = []
    spine = ["nav"]

    for i, (filename, chap_title) in enumerate(CHAPTER_FILES):
        filepath = os.path.join(BOOK_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  Skipping {filename}")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        html_content = md_to_html(content)
        chap = epub.EpubHtml(title=chap_title, file_name=f"chap_{i:02d}.xhtml", lang="es")
        chap.content = f'<html><head><link rel="stylesheet" type="text/css" href="style.css"/></head><body>{html_content}</body></html>'
        chap.add_item(nav_css)
        book.add_item(chap)
        chapters_epub.append(chap)
        spine.append(chap)

    book.toc = chapters_epub
    book.spine = spine
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    output_path = os.path.join(OUTPUT_DIR, "print_Sigo_Aqui.epub")
    epub.write_epub(output_path, book, {})
    print(f"EPUB created: {output_path}")
    return output_path


class BookPDF(FPDF):
    """Professional book layout with serif body, justified text, first-line indent."""

    INDENT_MM = 6
    LEADING_MM = 5.6
    BODY_SIZE = 10.5
    CODE_SIZE = 8
    CHAP_SIZE = 22
    SEC_SIZE = 14
    SUB_SIZE = 11

    def __init__(self):
        super().__init__()
        self._chapter_started = False

        # --- Professional book fonts ---
        self.add_font("Georgia", "", os.path.join(FONT_DIR, "georgia.ttf"))
        self.add_font("Georgia", "B", os.path.join(FONT_DIR, "georgiab.ttf"))
        self.add_font("Georgia", "I", os.path.join(FONT_DIR, "georgiai.ttf"))
        self.add_font("Georgia", "BI", os.path.join(FONT_DIR, "georgiaz.ttf"))
        self.add_font("Consolas", "", os.path.join(FONT_DIR, "consola.ttf"))
        self.add_font("Consolas", "B", os.path.join(FONT_DIR, "consolab.ttf"))

        # Margins: left (binding) 25mm, top 20mm, right 20mm
        self.set_margins(25, 20, 20)
        self.set_auto_page_break(auto=True, margin=22)

    def header(self):
        pass  # clean book style – no running headers

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-18)
            self.set_font("Georgia", "", 9)
            self.cell(0, 10, str(self.page_no()), align="C")

    # ---- helper: parse inline **bold** and *italic* into segments ----
    @staticmethod
    def _parse_segments(text):
        segments = []
        pat = re.compile(r'\*\*(.+?)\*\*|\*(.+?)\*')
        pos = 0
        for m in pat.finditer(text):
            if m.start() > pos:
                segments.append(("", text[pos:m.start()]))
            if m.group(1) is not None:
                segments.append(("B", m.group(1)))
            else:
                segments.append(("I", m.group(2)))
            pos = m.end()
        if pos < len(text):
            segments.append(("", text[pos:]))
        return segments

    def _has_formatting(self, text):
        return bool(re.search(r'\*\*|\*', text))

    # ---- rendering methods ----
    def add_title_page(self):
        self.add_page()
        self.ln(55)
        # Decorative line
        self.set_draw_color(200, 160, 50)
        self.set_line_width(0.5)
        cx = self.w / 2
        self.line(cx - 40, self.get_y(), cx + 40, self.get_y())
        self.ln(15)

        # Title
        self.set_font("Georgia", "B", 30)
        self.multi_cell(0, 14, TITLE, align="C")
        self.ln(6)
        # Subtitle
        self.set_font("Georgia", "I", 13)
        for sub_line in SUBTITLE.split("\n"):
            self.cell(0, 8, sub_line, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(8)
        # Decorative line
        self.set_draw_color(200, 160, 50)
        self.line(cx - 40, self.get_y(), cx + 40, self.get_y())
        self.ln(30)
        # Author
        self.set_font("Georgia", "", 12)
        self.cell(0, 8, AUTHOR, align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "alexgoyzueta2018@gmail.com", align="C", new_x="LMARGIN", new_y="NEXT")

    def add_chapter_heading(self, text):
        if self._chapter_started:
            self.add_page()
        self._chapter_started = True
        self.ln(15)
        # Decorative line above
        self.set_draw_color(180, 150, 70)
        self.set_line_width(0.4)
        cx = self.w / 2
        self.line(cx - 35, self.get_y(), cx + 35, self.get_y())
        self.ln(10)
        # Chapter title
        self.set_font("Georgia", "B", BookPDF.CHAP_SIZE)
        self.multi_cell(0, 12, text, align="C")
        # Decorative line below
        self.ln(4)
        self.set_draw_color(180, 150, 70)
        self.line(cx - 35, self.get_y(), cx + 35, self.get_y())
        self.ln(12)

    def add_section_heading(self, text):
        self.ln(3)
        self.set_font("Georgia", "B", BookPDF.SEC_SIZE)
        self.multi_cell(0, 8, text, align="L")
        self.set_x(self.l_margin)
        self.ln(2)

    def add_sub_heading(self, text):
        self.ln(2)
        self.set_font("Georgia", "B", BookPDF.SUB_SIZE)
        self.multi_cell(0, 6, text, align="L")
        self.set_x(self.l_margin)
        self.ln(1)

    def add_body_text(self, text):
        if self._has_formatting(text):
            self._write_formatted(text)
            self.set_x(self.l_margin)
            return
        self.set_font("Georgia", "", BookPDF.BODY_SIZE)
        self.multi_cell(0, BookPDF.LEADING_MM, "     " + text, align="J")
        self.set_x(self.l_margin)

    def _write_formatted(self, text):
        segments = self._parse_segments(text)
        segments.insert(0, ("", "     "))
        for style, seg_text in segments:
            self.set_font("Georgia", style, BookPDF.BODY_SIZE)
            self.write(BookPDF.LEADING_MM * 1.15, seg_text)
        self.set_x(self.l_margin)
        self.ln(BookPDF.LEADING_MM * 1.25)

    def add_horizontal_rule(self):
        self.ln(3)
        y = self.get_y()
        self.set_draw_color(170, 170, 170)
        self.set_line_width(0.3)
        self.line(self.l_margin + 10, y, self.w - self.r_margin - 10, y)
        self.ln(4)

    def add_list_item(self, text):
        self.set_font("Georgia", "", BookPDF.BODY_SIZE)
        self.multi_cell(0, BookPDF.LEADING_MM, "      \u2022 " + text, align="J")
        self.set_x(self.l_margin)
        self.ln(1)

    def add_code_block(self, code):
        self.ln(2)
        self.set_fill_color(242, 242, 245)
        self.set_draw_color(200, 200, 200)
        self.set_font("Consolas", "", BookPDF.CODE_SIZE)
        lines = code.split("\n")
        # compute block width
        margin = 16
        blk_w = self.w - self.l_margin - self.r_margin - margin * 2
        x0 = self.l_margin + margin
        self.set_x(x0)
        for line in lines:
            if self.get_y() > self.h - 28:
                self.add_page()
                self.set_x(x0)
            display = line if line else " "
            self.cell(blk_w, 4.8, "  " + display, fill=True, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x0)
        self.ln(4)


# ---------------------------------------------------------------------------
# PARSER
# ---------------------------------------------------------------------------

def parse_for_pdf(pdf, content):
    in_code = False
    code_buffer = []

    for line in content.split("\n"):
        if line.startswith("```"):
            if in_code:
                in_code = False
                pdf.add_code_block("\n".join(code_buffer))
                code_buffer = []
            else:
                in_code = True
                code_buffer = []
            continue

        if in_code:
            code_buffer.append(line)
            continue

        stripped = line.strip()
        if not stripped:
            continue
        if "|" in line and "---" not in line:
            continue

        if line.startswith("# ") and not line.startswith("## "):
            pdf.add_chapter_heading(stripped[2:])
        elif line.startswith("## ") and not line.startswith("### "):
            pdf.add_section_heading(stripped[3:])
        elif line.startswith("### ") and not line.startswith("#### "):
            pdf.add_sub_heading(line[4:].strip())
        elif stripped == "---":
            pdf.add_horizontal_rule()
        elif stripped.startswith("- "):
            pdf.add_list_item(stripped[2:])
        else:
            pdf.add_body_text(stripped)


def create_pdf():
    pdf = BookPDF()
    pdf.add_title_page()
    pdf._chapter_started = False

    for filename, chap_title in CHAPTER_FILES:
        filepath = os.path.join(BOOK_DIR, filename)
        if not os.path.exists(filepath):
            print(f"  Skipping {filename}")
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        parse_for_pdf(pdf, content)

    output_path = os.path.join(OUTPUT_DIR, "print_Sigo_Aqui.pdf")
    pdf.output(output_path)
    print(f"PDF created: {output_path}")
    return output_path


def main():
    print("Creating EPUB...")
    epub_path = create_epub()
    print("Creating PDF...")
    pdf_path = create_pdf()
    print(f"\nDone! Files created:")
    print(f"  EPUB: {epub_path}")
    print(f"  PDF:  {pdf_path}")

    import os
    epub_size = os.path.getsize(epub_path) // 1024
    pdf_size = os.path.getsize(pdf_path) // 1024
    print(f"  EPUB size: {epub_size} KB")
    print(f"  PDF size: {pdf_size} KB")


if __name__ == "__main__":
    main()
