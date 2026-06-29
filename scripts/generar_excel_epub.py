import os
import re
from ebooklib import epub

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CSS = """
body { font-family: Georgia, 'Times New Roman', serif; line-height: 1.6; color: #333; margin: 0; padding: 0; }
h1 { font-family: Georgia, 'Times New Roman', serif; font-size: 2.2em; font-weight: bold; text-align: center; page-break-before: always; margin-top: 3em; margin-bottom: 0.5em; color: #1a1a1a; }
h2 { font-family: Georgia, 'Times New Roman', serif; font-size: 1.6em; font-weight: bold; text-align: left; margin-top: 2em; margin-bottom: 0.3em; color: #2a2a2a; }
h3 { font-family: Georgia, 'Times New Roman', serif; font-size: 1.3em; font-weight: bold; margin-top: 1.5em; margin-bottom: 0.3em; color: #2a2a2a; }
p { text-align: justify; text-indent: 1.5em; margin: 0.3em 0; orphans: 3; widows: 3; }
h1 + p, h2 + p, h3 + p { text-indent: 0; }
pre { font-family: Consolas, 'Courier New', monospace; font-size: 0.85em; background-color: #f5f5f5; border: 1px solid #ddd; border-radius: 4px; padding: 1em; margin: 1em 0; white-space: pre-wrap; word-wrap: break-word; line-height: 1.4; }
code { font-family: Consolas, 'Courier New', monospace; font-size: 0.9em; background-color: #f0f0f0; padding: 0.1em 0.3em; border-radius: 3px; }
pre code { background-color: transparent; padding: 0; border-radius: 0; }
blockquote { font-style: italic; color: #555; border-left: 4px solid #ccc; margin: 1em 0; padding: 0.5em 1em; background-color: #fafafa; }
table { border-collapse: collapse; margin: 1em auto; font-size: 0.9em; width: 100%; }
th, td { border: 1px solid #ccc; padding: 0.4em 0.8em; text-align: left; }
th { background-color: #f0f0f0; font-weight: bold; }
img { max-width: 100%; height: auto; }
hr { border: 0; border-top: 1px solid #ccc; margin: 1.5em 0; }
.cover-page { page-break-after: always; text-align: center; padding-top: 30%; }
.dedication { text-align: center; font-style: italic; margin-top: 5em; }
"""

BOOKS = [
    {
        "folder": "excel_basico",
        "id": "excel-basico-legado-formulas",
        "title": "Excel B\u00e1sico: El Legado de las F\u00f3rmulas",
        "subtitle": "Una Novela para Aprender Excel Desde Cero",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Excel_Basico.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_el_taller_heredado.md", "Cap\u00edtulo 1: El Taller Heredado"),
            ("06_capitulo2_el_primer_inventario.md", "Cap\u00edtulo 2: El Primer Inventario"),
            ("07_capitulo3_las_formulas_del_abuelo.md", "Cap\u00edtulo 3: Las F\u00f3rmulas del Abuelo"),
            ("08_capitulo4_el_misterio_de_las_referencias.md", "Cap\u00edtulo 4: El Misterio de las Referencias"),
            ("09_capitulo5_dando_forma_a_los_numeros.md", "Cap\u00edtulo 5: Dando Forma a los N\u00fameros"),
            ("10_capitulo6_el_pedido_especial.md", "Cap\u00edtulo 6: El Pedido Especial"),
            ("11_capitulo7_un_vistazo_al_progreso.md", "Cap\u00edtulo 7: Un Vistazo al Progreso"),
            ("12_capitulo8_la_feria_de_la_madera.md", "Cap\u00edtulo 8: La Feria de la Madera"),
            ("13_capitulo9_el_presupuesto_final.md", "Cap\u00edtulo 9: El Presupuesto Final"),
            ("14_capitulo10_la_gran_apertura.md", "Cap\u00edtulo 10: La Gran Apertura"),
            ("15_conclusion.md", "Conclusi\u00f3n"),
            ("16_apendice_soluciones.md", "Ap\u00e9ndice: Soluciones"),
            ("17_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "excel_intermedio",
        "id": "excel-intermedio-secretos-hoja",
        "title": "Excel Intermedio: Los Secretos de la Hoja",
        "subtitle": "Una Novela para Dominar el An\u00e1lisis de Datos en Excel",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Excel_Intermedio.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_el_archivo_secreto.md", "Cap\u00edtulo 1: El Archivo Secreto"),
            ("06_capitulo2_pistas_ocultas.md", "Cap\u00edtulo 2: Pistas Ocultas"),
            ("07_capitulo3_la_busqueda_del_tesoro.md", "Cap\u00edtulo 3: La B\u00fasqueda del Tesoro"),
            ("08_capitulo4_el_rompecabezas_financiero.md", "Cap\u00edtulo 4: El Rompecabezas Financiero"),
            ("09_capitulo5_revelaciones.md", "Cap\u00edtulo 5: Revelaciones"),
            ("10_capitulo6_el_codigo_del_abuelo.md", "Cap\u00edtulo 6: El C\u00f3digo del Abuelo"),
            ("11_capitulo7_nombres_con_significado.md", "Cap\u00edtulo 7: Nombres con Significado"),
            ("12_capitulo8_que_pasaria_si.md", "Cap\u00edtulo 8: \u00bfQu\u00e9 Pasar\u00eda Si...?"),
            ("13_capitulo9_el_mapa_del_tesoro.md", "Cap\u00edtulo 9: El Mapa del Tesoro"),
            ("14_capitulo10_la_verdad_emerge.md", "Cap\u00edtulo 10: La Verdad Emerge"),
            ("15_conclusion.md", "Conclusi\u00f3n"),
            ("16_apendice_soluciones.md", "Ap\u00e9ndice: Soluciones"),
            ("17_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "excel_avanzado",
        "id": "excel-avanzado-poder-analisis",
        "title": "Excel Avanzado: El Poder del An\u00e1lisis",
        "subtitle": "Una Novela para Convertirte en un Experto en An\u00e1lisis de Datos con Excel",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Excel_Avanzado.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_el_descubrimiento.md", "Cap\u00edtulo 1: El Descubrimiento"),
            ("06_capitulo2_conexiones_peligrosas.md", "Cap\u00edtulo 2: Conexiones Peligrosas"),
            ("07_capitulo3_el_lenguaje_de_los_datos.md", "Cap\u00edtulo 3: El Lenguaje de los Datos"),
            ("08_capitulo4_automatizacion_necesaria.md", "Cap\u00edtulo 4: Automatizaci\u00f3n Necesaria"),
            ("09_capitulo5_formulas_que_piensan.md", "Cap\u00edtulo 5: F\u00f3rmulas que Piensan"),
            ("10_capitulo6_la_estrategia_optima.md", "Cap\u00edtulo 6: La Estrategia \u00d3ptima"),
            ("11_capitulo7_el_panel_de_control.md", "Cap\u00edtulo 7: El Panel de Control"),
            ("12_capitulo8_la_presentacion_final.md", "Cap\u00edtulo 8: La Presentaci\u00f3n Final"),
            ("13_capitulo9_el_juicio.md", "Cap\u00edtulo 9: El Juicio"),
            ("14_capitulo10_justicia_y_nuevos_comienzos.md", "Cap\u00edtulo 10: Justicia y Nuevos Comienzos"),
            ("15_conclusion.md", "Conclusi\u00f3n"),
            ("16_apendice_soluciones.md", "Ap\u00e9ndice: Soluciones"),
            ("17_sobre_el_autor.md", "Sobre el Autor"),
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
            ("01_creditos.md", "Créditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducción"),
            ("05_configuracion_excel_contabilidad.md", "Capítulo 1: Configuración para Contabilidad"),
            ("06_catalogo_cuentas.md", "Capítulo 2: Catálogo de Cuentas"),
            ("07_libro_diario_mayor.md", "Capítulo 3: Libro Diario y Mayor"),
            ("08_funciones_financieras.md", "Capítulo 4: Funciones Financieras"),
            ("09_funciones_condicionales.md", "Capítulo 5: Funciones Condicionales"),
            ("10_tablas_dinamicas.md", "Capítulo 6: Tablas Dinámicas"),
            ("11_consolidacion.md", "Capítulo 7: Consolidación"),
            ("12_auditoria_validacion.md", "Capítulo 8: Auditoría"),
            ("13_dashboard_kpis.md", "Capítulo 9: Dashboard y KPIs"),
            ("14_macros_vba.md", "Capítulo 10: Macros VBA"),
            ("15_epilogo.md", "Epílogo"),
            ("16_enigmas_finales.md", "Enigmas Finales"),
            ("17_soluciones.md", "Soluciones"),
        ],
    },
    {
        "folder": "excel_analisis_datos",
        "id": "excel-analisis-datos",
        "title": "Excel para An\u00e1lisis de Datos",
        "subtitle": "De los datos crudos a las decisiones inteligentes",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Excel_Analisis_Datos.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Créditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducción"),
            ("05_proceso_analisis_datos.md", "Capítulo 1: El Proceso del Análisis de Datos"),
            ("06_limpieza_datos.md", "Capítulo 2: Limpieza y Preparación de Datos"),
            ("07_eda.md", "Capítulo 3: Análisis Exploratorio de Datos (EDA)"),
            ("08_funciones_analisis.md", "Capítulo 4: Funciones de Análisis Esenciales"),
            ("09_tendencias.md", "Capítulo 5: Análisis de Tendencias y Patrones"),
            ("10_tablas_dinamicas.md", "Capítulo 6: Tablas Dinámicas para Análisis"),
            ("11_visualizacion.md", "Capítulo 7: Visualización de Datos"),
            ("12_escenarios.md", "Capítulo 8: Análisis de Escenarios y Sensibilidad"),
            ("13_powerquery.md", "Capítulo 9: Power Query para Análisis de Datos"),
            ("14_proyecto_final.md", "Capítulo 10: Proyecto Final — Pipeline de Análisis"),
        ],
    },
]



def md_to_html(md_text):
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

    lines = html.split("\n")
    result = []
    in_table = False
    in_code = False
    for line in lines:
        if line.startswith("<pre>"):
            in_code = True
            result.append(line)
            continue
        if line.startswith("</pre>"):
            in_code = False
            result.append(line)
            continue
        if in_code:
            result.append(line)
            continue
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|") and stripped.count("|") > 2:
            if not in_table:
                result.append("<table>")
                in_table = True
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            header_below = False
            result.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
        else:
            if in_table:
                result.append("</table>")
                in_table = False
            result.append(line)
    if in_table:
        result.append("</table>")

    html = "\n".join(result)
    html = re.sub(r'^(.+?)$', r'<p>\1</p>', html, flags=re.MULTILINE)

    return f"<html><body>{html}</body></html>"


def create_epub_for_book(book_config):
    print(f"\n--- Generando EPUB: {book_config['title']} ---")

    book = epub.EpubBook()
    book.set_identifier(book_config["id"])
    book.set_title(book_config["title"])
    book.set_language("es")
    book.add_author(book_config["author"])
    book.add_metadata("DC", "description", book_config["subtitle"])

    nav_css = epub.EpubItem(uid="style", file_name="style.css", media_type="text/css", content=CSS)
    book.add_item(nav_css)

    book_dir = os.path.join(BASE, book_config["folder"])

    # Add cover image
    cover_path = os.path.join(book_dir, "cover.jpg")
    if os.path.exists(cover_path):
        with open(cover_path, "rb") as f:
            cover_data = f.read()
        book.set_cover("cover.jpg", cover_data)

    chapters_epub = []
    spine = ["nav"]

    for filename, chap_title in book_config["chapter_map"]:
        filepath = os.path.join(book_dir, filename)
        if not os.path.exists(filepath):
            print(f"  [FALTA] {filename}")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        html_content = md_to_html(content)
        chap = epub.EpubHtml(title=chap_title, file_name=f"chap_{filename.replace('.md', '.xhtml')}", lang="es")
        chap.content = f'<html><head><link rel="stylesheet" type="text/css" href="style.css"/></head><body>{html_content}</body></html>'
        chap.add_item(nav_css)
        book.add_item(chap)
        chapters_epub.append(chap)
        spine.append(chap)

    book.toc = chapters_epub
    book.spine = spine
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    output_path = os.path.join(book_dir, book_config["epub_filename"])
    epub.write_epub(output_path, book, {})
    print(f"  EPUB creado: {output_path}")
    size_kb = os.path.getsize(output_path) // 1024
    print(f"  Tamaño: {size_kb} KB")

    return output_path


def main():
    print("Generando libros EPUB de Excel...")
    print("=" * 50)

    for book_config in BOOKS:
        try:
            create_epub_for_book(book_config)
        except Exception as e:
            print(f"  ERROR: {e}")

    print("\n" + "=" * 50)
    print("Proceso completado.")


if __name__ == "__main__":
    main()
