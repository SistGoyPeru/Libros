import re
from fpdf import FPDF

class MarkdownPDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)

    def write_markdown(self, md_text):
        in_code = False
        code_block = []
        for line in md_text.split('\n'):
            stripped = line.strip()
            if stripped.startswith('```'):
                if in_code:
                    self._render_code('\n'.join(code_block))
                    code_block = []
                in_code = not in_code
                continue
            if in_code:
                code_block.append(line)
                continue
            if not stripped or stripped.startswith('<'):
                continue
            if re.match(r'^-{3,}$', stripped) or re.match(r'^\*{3,}$', stripped):
                self.ln(3)
                continue
            if stripped.startswith('# '):
                self.set_font('Arial', 'B', 20)
                self.multi_cell(0, 10, stripped[2:], align='C')
                self.ln(3)
                continue
            if stripped.startswith('## '):
                self.set_font('Arial', 'B', 16)
                self.multi_cell(0, 8, stripped[3:], align='L')
                self.ln(2)
                continue
            if stripped.startswith('### '):
                self.set_font('Arial', 'B', 13)
                self.multi_cell(0, 7, stripped[4:])
                self.ln(2)
                continue
            text = stripped.replace('**', '').replace('*', '').replace('$$', '')
            if stripped.startswith('> '):
                self.set_font('Arial', '', 10)
                self.set_text_color(100, 100, 100)
                self.multi_cell(0, 5, stripped[2:])
                self.set_text_color(0, 0, 0)
                self.ln(1)
                continue
            self.set_font('Arial', '', 11)
            self.multi_cell(0, 5.5, text)
            self.ln(1)

    def _render_code(self, code_text):
        self.set_fill_color(240, 240, 240)
        self.set_font('Consolas', '', 7.5)
        for line in code_text.split('\n'):
            if line.strip():
                try:
                    self.cell(0, 4, line[:120], fill=True)
                except:
                    self.cell(0, 4, line.encode('ascii', 'ignore').decode()[:120], fill=True)
                self.ln()
        self.ln(2)


base = r'C:\Users\alexg\OneDrive\Alex_2026\libros epub\sql_letal'
md_path = base + r'\libro_completo.md'
pdf_path = base + r'\SQL_Letal_Misterio_Base_Datos.pdf'

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

pdf = MarkdownPDF()
pdf.add_font('Arial', '', r'C:\Windows\Fonts\arial.ttf')
pdf.add_font('Arial', 'B', r'C:\Windows\Fonts\arialbd.ttf')
pdf.add_font('Consolas', '', r'C:\Windows\Fonts\consola.ttf')
pdf.add_page()
pdf.write_markdown(text)
pdf.output(pdf_path)
print(f'PDF generado: {pdf_path}')
print(f'Paginas: {pdf.pages_count}')
