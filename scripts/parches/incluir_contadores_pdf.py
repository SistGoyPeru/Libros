import re

path = r"c:\Users\alexg\OneDrive\Alex_2026\libros epub\generar_excel_pdf.py"
with open(path, encoding="utf-8") as f:
    content = f.read()

old = '            "16_apendice_soluciones.md", "17_sobre_el_autor.md",\n        ],\n    },\n]\n\n\nclass ExcelBookPDF(FPDF):'

new_book = '''            "16_apendice_soluciones.md", "17_sobre_el_autor.md",
        ],
    },
    {
        "folder": "excel_contadores",
        "pdf_filename": "Excel_Para_Contadores.pdf",
        "title": "Excel para Contadores",
        "subtitle": "Domina Excel en el mundo contable y financiero",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_configuracion_excel_contabilidad.md",
            "06_catalogo_cuentas.md", "07_libro_diario_mayor.md",
            "08_funciones_financieras.md", "09_funciones_condicionales.md",
            "10_tablas_dinamicas.md", "11_consolidacion.md",
            "12_auditoria_validacion.md", "13_dashboard_kpis.md",
            "14_macros_vba.md", "15_epilogo.md",
            "16_enigmas_finales.md", "17_soluciones.md",
        ],
    },
]


class ExcelBookPDF(FPDF):'''

if old not in content:
    print("NOT FOUND")
else:
    content = content.replace(old, new_book, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("OK - PDF script updated")
