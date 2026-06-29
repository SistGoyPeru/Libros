import os, re
from fpdf import FPDF

BASE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = "C:\\Windows\\Fonts"

BOOKS = [
    {
        "folder": "excel_basico",
        "pdf_filename": "Excel_Basico.pdf",
        "title": "Excel B\u00e1sico: El Legado de las F\u00f3rmulas",
        "subtitle": "Una Novela para Aprender Excel Desde Cero",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_el_taller_heredado.md",
            "06_capitulo2_el_primer_inventario.md", "07_capitulo3_las_formulas_del_abuelo.md",
            "08_capitulo4_el_misterio_de_las_referencias.md", "09_capitulo5_dando_forma_a_los_numeros.md",
            "10_capitulo6_el_pedido_especial.md", "11_capitulo7_un_vistazo_al_progreso.md",
            "12_capitulo8_la_feria_de_la_madera.md", "13_capitulo9_el_presupuesto_final.md",
            "14_capitulo10_la_gran_apertura.md", "15_conclusion.md",
            "16_apendice_soluciones.md", "17_sobre_el_autor.md",
        ],
    },
    {
        "folder": "excel_intermedio",
        "pdf_filename": "Excel_Intermedio.pdf",
        "title": "Excel Intermedio: Los Secretos de la Hoja",
        "subtitle": "Una Novela para Dominar el An\u00e1lisis de Datos en Excel",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_el_archivo_secreto.md",
            "06_capitulo2_pistas_ocultas.md", "07_capitulo3_la_busqueda_del_tesoro.md",
            "08_capitulo4_el_rompecabezas_financiero.md", "09_capitulo5_revelaciones.md",
            "10_capitulo6_el_codigo_del_abuelo.md", "11_capitulo7_nombres_con_significado.md",
            "12_capitulo8_que_pasaria_si.md", "13_capitulo9_el_mapa_del_tesoro.md",
            "14_capitulo10_la_verdad_emerge.md", "15_conclusion.md",
            "16_apendice_soluciones.md", "17_sobre_el_autor.md",
        ],
    },
    {
        "folder": "excel_avanzado",
        "pdf_filename": "Excel_Avanzado.pdf",
        "title": "Excel Avanzado: El Poder del An\u00e1lisis",
        "subtitle": "Una Novela para Convertirte en un Experto en An\u00e1lisis de Datos con Excel",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_el_descubrimiento.md",
            "06_capitulo2_conexiones_peligrosas.md", "07_capitulo3_el_lenguaje_de_los_datos.md",
            "08_capitulo4_automatizacion_necesaria.md", "09_capitulo5_formulas_que_piensan.md",
            "10_capitulo6_la_estrategia_optima.md", "11_capitulo7_el_panel_de_control.md",
            "12_capitulo8_la_presentacion_final.md", "13_capitulo9_el_juicio.md",
            "14_capitulo10_justicia_y_nuevos_comienzos.md", "15_conclusion.md",
            "16_apendice_soluciones.md", "17_sobre_el_autor.md",
        ],
    },
]


class ExcelBookPDF(FPDF):
    BODY_SIZE = 10.5
    CODE_SIZE = 8
    CHAP_SIZE = 22
    SEC_SIZE = 14
    SUB_SIZE = 11
    LEADING_MM = 5.6

    def __init__(self, title, subtitle, author):
        super().__init__()
        self._chapter_started = False
        self._title = title
        self._subtitle = subtitle
        self._author = author

        self.add_font("Georgia", "", os.path.join(FONT_DIR, "georgia.ttf"))
        self.add_font("Georgia", "B", os.path.join(FONT_DIR, "georgiab.ttf"))
        self.add_font("Georgia", "I", os.path.join(FONT_DIR, "georgiai.ttf"))
        self.add_font("Georgia", "BI", os.path.join(FONT_DIR, "georgiaz.ttf"))
        self.add_font("Consolas", "", os.path.join(FONT_DIR, "consola.ttf"))
        self.add_font("Consolas", "B", os.path.join(FONT_DIR, "consolab.ttf"))

        self.set_margins(25, 20, 20)
        self.set_auto_page_break(auto=True, margin=22)

    def header(self):
        pass

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-18)
            self.set_font("Georgia", "", 9)
            self.cell(0, 10, str(self.page_no()), align="C")

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

    def add_title_page(self):
        self.add_page()
        self.ln(55)
        cx = self.w / 2
        self.set_draw_color(50, 140, 70)
        self.set_line_width(0.5)
        self.line(cx - 40, self.get_y(), cx + 40, self.get_y())
        self.ln(15)
        self.set_font("Georgia", "B", 30)
        self.multi_cell(0, 14, self._title, align="C")
        self.ln(6)
        self.set_font("Georgia", "I", 13)
        for sub_line in self._subtitle.split("\n"):
            self.cell(0, 8, sub_line, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(8)
        self.set_draw_color(50, 140, 70)
        self.line(cx - 40, self.get_y(), cx + 40, self.get_y())
        self.ln(30)
        self.set_font("Georgia", "", 12)
        self.cell(0, 8, self._author, align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 8, "alexgoyzueta2018@gmail.com", align="C", new_x="LMARGIN", new_y="NEXT")

    def add_chapter_heading(self, text):
        if self._chapter_started:
            self.add_page()
        self._chapter_started = True
        self.ln(15)
        cx = self.w / 2
        self.set_draw_color(50, 140, 70)
        self.set_line_width(0.4)
        self.line(cx - 35, self.get_y(), cx + 35, self.get_y())
        self.ln(10)
        self.set_font("Georgia", "B", self.CHAP_SIZE)
        self.multi_cell(0, 12, text, align="C")
        self.ln(4)
        self.line(cx - 35, self.get_y(), cx + 35, self.get_y())
        self.ln(12)

    def add_section_heading(self, text):
        self.ln(3)
        self.set_font("Georgia", "B", self.SEC_SIZE)
        self.multi_cell(0, 8, text, align="L")
        self.set_x(self.l_margin)
        self.ln(2)

    def add_sub_heading(self, text):
        self.ln(2)
        self.set_font("Georgia", "B", self.SUB_SIZE)
        self.multi_cell(0, 6, text, align="L")
        self.set_x(self.l_margin)
        self.ln(1)

    def add_body_text(self, text):
        if self._has_formatting(text):
            self._write_formatted(text)
            self.set_x(self.l_margin)
            return
        self.set_font("Georgia", "", self.BODY_SIZE)
        self.multi_cell(0, self.LEADING_MM, "     " + text, align="J")
        self.set_x(self.l_margin)

    def _write_formatted(self, text):
        segments = self._parse_segments(text)
        segments.insert(0, ("", "     "))
        for style, seg_text in segments:
            self.set_font("Georgia", style, self.BODY_SIZE)
            self.write(self.LEADING_MM * 1.15, seg_text)
        self.set_x(self.l_margin)
        self.ln(self.LEADING_MM * 1.25)

    def add_horizontal_rule(self):
        self.ln(3)
        y = self.get_y()
        self.set_draw_color(170, 170, 170)
        self.set_line_width(0.3)
        self.line(self.l_margin + 10, y, self.w - self.r_margin - 10, y)
        self.ln(4)

    def add_list_item(self, text):
        if self._has_formatting(text):
            segments = self._parse_segments(text)
            self.set_x(self.l_margin + 10)
            self.set_font("Georgia", "", self.BODY_SIZE)
            self.write(self.LEADING_MM, "  \u2022 ")
            for style, seg_text in segments:
                self.set_font("Georgia", style, self.BODY_SIZE)
                self.write(self.LEADING_MM, seg_text)
            self.set_x(self.l_margin)
            self.ln(self.LEADING_MM * 1.3)
        else:
            self.set_font("Georgia", "", self.BODY_SIZE)
            self.multi_cell(0, self.LEADING_MM, "      \u2022 " + text, align="J")
            self.set_x(self.l_margin)
            self.ln(1)

    def add_code_block(self, code):
        self.ln(2)
        self.set_fill_color(242, 242, 245)
        self.set_draw_color(200, 200, 200)
        self.set_font("Consolas", "", self.CODE_SIZE)
        lines = code.split("\n")
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

    def add_table(self, rows):
        self.ln(2)
        col_count = max(len(r) for r in rows) if rows else 0
        if col_count == 0:
            return
        col_w = (self.w - self.l_margin - self.r_margin) / col_count
        self.set_font("Consolas", "", 7.5)
        for i, row in enumerate(rows):
            if self.get_y() > self.h - 30:
                self.add_page()
            for j, cell in enumerate(row):
                x = self.l_margin + j * col_w
                self.set_xy(x, self.get_y())
                if i == 0:
                    fill = True
                else:
                    fill = i % 2 == 0
                self.cell(col_w, 5.5, cell, border=1, fill=fill, align="C")
            self.ln()
        self.ln(3)


def parse_md_for_pdf(pdf, content):
    in_code = False
    code_buffer = []
    in_table = False
    table_rows = []

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
            if in_table:
                pdf.add_table(table_rows)
                table_rows = []
                in_table = False
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            is_separator = all(set(c) <= set("-: ") for c in cells)
            if is_separator:
                continue
            if not in_table:
                table_rows = []
                in_table = True
            table_rows.append(cells)
            continue
        else:
            if in_table:
                pdf.add_table(table_rows)
                table_rows = []
                in_table = False

        if "|" in stripped and not stripped.startswith("|"):
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

    if in_table:
        pdf.add_table(table_rows)


def create_pdf_for_book(book_config):
    print(f"\n--- Generando PDF: {book_config['title']} ---")

    pdf = ExcelBookPDF(book_config["title"], book_config["subtitle"], book_config["author"])
    pdf.add_title_page()

    book_dir = os.path.join(BASE, book_config["folder"])
    for filename in book_config["chapter_map"]:
        filepath = os.path.join(book_dir, filename)
        if not os.path.exists(filepath):
            print(f"  [FALTA] {filename}")
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        parse_md_for_pdf(pdf, content)

    output_path = os.path.join(book_dir, book_config["pdf_filename"])
    pdf.output(output_path)
    size_kb = os.path.getsize(output_path) // 1024
    print(f"  PDF creado: {output_path} ({size_kb} KB)")
    return output_path


def main():
    print("Generando libros PDF de Excel...")
    print("=" * 50)
    for book_config in BOOKS:
        try:
            create_pdf_for_book(book_config)
        except Exception as e:
            print(f"  ERROR: {e}")
    print("\n" + "=" * 50)
    print("Proceso completado.")


if __name__ == "__main__":
    main()
