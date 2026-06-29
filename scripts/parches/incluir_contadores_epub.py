path = r"c:\Users\alexg\OneDrive\Alex_2026\libros epub\generar_excel_epub.py"
with open(path, encoding="utf-8") as f:
    content = f.read()

old = '            ("17_sobre_el_autor.md", "Sobre el Autor"),\n        ],\n    },\n]\n\n\ndef md_to_html(md_text):'

new_book = '''            ("17_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "excel_contadores",
        "id": "excel-contadores",
        "title": "Excel para Contadores",
        "subtitle": "Domina Excel en el mundo contable y financiero",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Excel_Para_Contadores.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_configuracion_excel_contabilidad.md", "Cap\u00edtulo 1: Configuraci\u00f3n para Contabilidad"),
            ("06_catalogo_cuentas.md", "Cap\u00edtulo 2: Cat\u00e1logo de Cuentas"),
            ("07_libro_diario_mayor.md", "Cap\u00edtulo 3: Libro Diario y Mayor"),
            ("08_funciones_financieras.md", "Cap\u00edtulo 4: Funciones Financieras"),
            ("09_funciones_condicionales.md", "Cap\u00edtulo 5: Funciones Condicionales"),
            ("10_tablas_dinamicas.md", "Cap\u00edtulo 6: Tablas Din\u00e1micas"),
            ("11_consolidacion.md", "Cap\u00edtulo 7: Consolidaci\u00f3n"),
            ("12_auditoria_validacion.md", "Cap\u00edtulo 8: Auditor\u00eda"),
            ("13_dashboard_kpis.md", "Cap\u00edtulo 9: Dashboard y KPIs"),
            ("14_macros_vba.md", "Cap\u00edtulo 10: Macros VBA"),
            ("15_epilogo.md", "Ep\u00edlogo"),
            ("16_enigmas_finales.md", "Enigmas Finales"),
            ("17_soluciones.md", "Soluciones"),
        ],
    },
]

def md_to_html(md_text):'''

if old not in content:
    print("NOT FOUND")
else:
    content = content.replace(old, new_book, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("OK - EPUB script updated")
