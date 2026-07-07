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
        "category": "Excel",
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
        "category": "Excel",
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
        "category": "Excel",
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
        "category": "Excel",
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
        "category": "Excel",
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
    {
        "folder": "excel_copilot",
        "category": "Excel",
        "id": "excel-copilot-asistente-inteligente",
        "title": "Excel con Copilot: Tu Asistente Inteligente",
        "subtitle": "Una Novela para Dominar Excel con Inteligencia Artificial",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Excel_con_Copilot.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_primeros_pasos.md", "Cap\u00edtulo 1: El Primer Encuentro"),
            ("06_capitulo2_conversando_datos.md", "Cap\u00edtulo 2: Conversando con los Datos"),
            ("07_capitulo3_formulas_sin_esfuerzo.md", "Cap\u00edtulo 3: F\u00f3rmulas sin Esfuerzo"),
            ("08_capitulo4_analisis_instantaneo.md", "Cap\u00edtulo 4: An\u00e1lisis al Instante"),
            ("09_capitulo5_visualizaciones_magicas.md", "Cap\u00edtulo 5: Visualizaciones M\u00e1gicas"),
            ("10_capitulo6_limpieza_datos.md", "Cap\u00edtulo 6: Limpieza de Datos Automatizada"),
            ("11_capitulo7_power_query_copilot.md", "Cap\u00edtulo 7: Power Query y Copilot"),
            ("12_capitulo8_automatizacion_inteligente.md", "Cap\u00edtulo 8: Automatizaci\u00f3n Inteligente"),
            ("13_capitulo9_dashboard_inteligente.md", "Cap\u00edtulo 9: Dashboard Inteligente"),
            ("14_capitulo10_proyecto_final.md", "Cap\u00edtulo 10: El Proyecto Final"),
            ("15_conclusion.md", "Conclusi\u00f3n"),
            ("16_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "html_basico",
        "category": "Web",
        "id": "html-basico-codigo-web",
        "title": "HTML B\u00e1sico: El C\u00f3digo de la Web",
        "subtitle": "Una Novela para Aprender HTML Desde Cero",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "HTML_Basico.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_el_desafio_de_la_web.md", "Cap\u00edtulo 1: El Desaf\u00edo de la Web"),
            ("06_capitulo2_las_primeras_palabras.md", "Cap\u00edtulo 2: Las Primeras Palabras"),
            ("07_capitulo3_el_mapa_del_sitio.md", "Cap\u00edtulo 3: El Mapa del Sitio"),
            ("08_capitulo4_organizando_la_informacion.md", "Cap\u00edtulo 4: Organizando la Informaci\u00f3n"),
            ("09_capitulo5_la_voz_del_barrio.md", "Cap\u00edtulo 5: La Voz del Barrio"),
            ("10_capitulo6_el_significado_de_las_cosas.md", "Cap\u00edtulo 6: El Significado de las Cosas"),
            ("11_capitulo7_mas_alla_del_texto.md", "Cap\u00edtulo 7: M\u00e1s All\u00e1 del Texto"),
            ("12_capitulo8_el_codigo_invisible.md", "Cap\u00edtulo 8: El C\u00f3digo Invisible"),
            ("13_capitulo9_para_todos.md", "Cap\u00edtulo 9: Para Todos"),
            ("14_capitulo10_la_gran_publicacion.md", "Cap\u00edtulo 10: La Gran Publicaci\u00f3n"),
            ("15_conclusion.md", "Conclusi\u00f3n"),
            ("16_apendice_soluciones.md", "Ap\u00e9ndice: Soluciones"),
            ("17_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "css_basico",
        "category": "Web",
        "id": "css-basico-diseno-web",
        "title": "CSS B\u00e1sico: El Dise\u00f1o que Transforma la Web",
        "subtitle": "Una Novela para Aprender CSS Desde Cero",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "CSS_Basico.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_el_primer_estilo.md", "Cap\u00edtulo 1: El Primer Estilo"),
            ("06_capitulo2_la_paleta_de_colores.md", "Cap\u00edtulo 2: La Paleta de Colores"),
            ("07_capitulo3_el_espacio_entre_lineas.md", "Cap\u00edtulo 3: El Espacio entre L\u00edneas"),
            ("08_capitulo4_poniendo_orden.md", "Cap\u00edtulo 4: Poniendo Orden"),
            ("09_capitulo5_flexibilidad.md", "Cap\u00edtulo 5: Flexibilidad"),
            ("10_capitulo6_la_grilla_perfecta.md", "Cap\u00edtulo 6: La Grilla Perfecta"),
            ("11_capitulo7_adaptandose_al_mundo.md", "Cap\u00edtulo 7: Adapt\u00e1ndose al Mundo"),
            ("12_capitulo8_el_toque_magico.md", "Cap\u00edtulo 8: El Toque M\u00e1gico"),
            ("13_capitulo9_detalles_que_importan.md", "Cap\u00edtulo 9: Detalles que Importan"),
            ("14_capitulo10_el_lanzamiento.md", "Cap\u00edtulo 10: El Lanzamiento"),
            ("15_conclusion.md", "Conclusi\u00f3n"),
            ("16_apendice_soluciones.md", "Ap\u00e9ndice: Soluciones"),
            ("17_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "js_basico",
        "category": "Web",
        "id": "js-basico-poder-interactividad",
        "title": "JavaScript B\u00e1sico: El Poder de la Interactividad",
        "subtitle": "Una Novela para Aprender JavaScript Desde Cero",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "JS_Basico.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_el_primer_script.md", "Cap\u00edtulo 1: El Primer Script"),
            ("06_capitulo2_tomando_decisiones.md", "Cap\u00edtulo 2: Tomando Decisiones"),
            ("07_capitulo3_las_funciones_del_conocimiento.md", "Cap\u00edtulo 3: Las Funciones del Conocimiento"),
            ("08_capitulo4_listas_y_colecciones.md", "Cap\u00edtulo 4: Listas y Colecciones"),
            ("09_capitulo5_la_vida_en_la_pagina.md", "Cap\u00edtulo 5: La Vida en la P\u00e1gina"),
            ("10_capitulo6_transformando_la_interfaz.md", "Cap\u00edtulo 6: Transformando la Interfaz"),
            ("11_capitulo7_formularios_inteligentes.md", "Cap\u00edtulo 7: Formularios Inteligentes"),
            ("12_capitulo8_guardando_el_progreso.md", "Cap\u00edtulo 8: Guardando el Progreso"),
            ("13_capitulo9_conectando_con_el_mundo.md", "Cap\u00edtulo 9: Conectando con el Mundo"),
            ("14_capitulo10_la_gran_demo.md", "Cap\u00edtulo 10: La Gran Demo"),
            ("15_conclusion.md", "Conclusi\u00f3n"),
            ("16_apendice_soluciones.md", "Ap\u00e9ndice: Soluciones"),
            ("17_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "fundamentos_analista_datos",
        "category": "Datos_IA",
        "id": "fundamentos-analista-datos",
        "title": "Los Fundamentos del Analista de Datos",
        "subtitle": "Domina SQL, Excel y Python desde cero",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Fundamentos_Analista_Datos.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_ecosistema_analista.md", "Cap\u00edtulo 1: El Ecosistema del Analista de Datos"),
            ("06_capitulo2_sql_select_basico.md", "Cap\u00edtulo 2: SQL \u2014 SELECT y tus Primeros Datos"),
            ("07_capitulo3_sql_where_filtros.md", "Cap\u00edtulo 3: SQL \u2014 Filtrando con Precisi\u00f3n"),
            ("08_capitulo4_excel_importar_formato.md", "Cap\u00edtulo 4: Excel \u2014 Importar y Transformar Datos"),
            ("09_capitulo5_python_variables_tipos.md", "Cap\u00edtulo 5: Python \u2014 Variables y Tipos de Datos"),
            ("10_checkpoint_1_analizando_ventas_basicas.md", "Checkpoint 1: Analizando Ventas B\u00e1sicas"),
            ("11_capitulo6_sql_agregacion.md", "Cap\u00edtulo 6: SQL \u2014 Agrupando y Resumiendo Datos"),
            ("12_capitulo7_sql_joins.md", "Cap\u00edtulo 7: SQL \u2014 Conectando Tablas con JOINs"),
            ("13_capitulo8_excel_tablas_dinamicas.md", "Cap\u00edtulo 8: Excel \u2014 Tablas Din\u00e1micas"),
            ("14_capitulo9_python_estructuras_datos.md", "Cap\u00edtulo 9: Python \u2014 Estructuras de Datos y Control de Flujo"),
            ("15_capitulo10_excel_graficos.md", "Cap\u00edtulo 10: Excel \u2014 Visualizaci\u00f3n con Gr\u00e1ficos"),
            ("16_checkpoint_2_top_productos.md", "Checkpoint 2: Top 10 Productos M\u00e1s Vendidos"),
            ("17_capitulo11_sql_subconsultas_cte.md", "Cap\u00edtulo 11: SQL \u2014 Subconsultas y CTEs"),
            ("18_capitulo12_sql_window_functions.md", "Cap\u00edtulo 12: SQL \u2014 Funciones de Ventana"),
            ("19_capitulo13_excel_power_query.md", "Cap\u00edtulo 13: Excel \u2014 Power Query"),
            ("20_capitulo14_python_funciones.md", "Cap\u00edtulo 14: Python \u2014 Funciones y M\u00f3dulos"),
            ("21_capitulo15_excel_dax_basico.md", "Cap\u00edtulo 15: Excel \u2014 DAX y Power Pivot"),
            ("22_checkpoint_3_cohortes.md", "Checkpoint 3: An\u00e1lisis de Cohorte de Ventas"),
            ("23_capitulo16_python_sql_excel.md", "Cap\u00edtulo 16: Python + SQL + Excel \u2014 La Integraci\u00f3n Total"),
            ("24_capitulo17_modelo_datos_dashboard.md", "Cap\u00edtulo 17: Modelo de Datos y Dashboard Profesional"),
            ("25_capitulo18_proyecto_final.md", "Cap\u00edtulo 18: Proyecto Integrador Final"),
            ("26_checkpoint_4_pipeline_automatizado.md", "Checkpoint 4: Pipeline de An\u00e1lisis Automatizado"),
            ("27_conclusion.md", "Conclusi\u00f3n"),
            ("28_apendice_a_soluciones.md", "Ap\u00e9ndice A: Soluciones a los Ejercicios"),
            ("29_apendice_b_cheatsheets.md", "Ap\u00e9ndice B: Cheatsheets"),
            ("30_apendice_c_instalacion.md", "Ap\u00e9ndice C: Instalaci\u00f3n y Configuraci\u00f3n"),
            ("31_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "python_data_cloud",
        "category": "Datos_IA",
        "id": "python-data-cloud-pandas-bigquery",
        "title": "Python para Datos y tu Primer Data Warehouse Cloud",
        "subtitle": "De Pandas a BigQuery: an\u00e1lisis profesional en la nube",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Python_Data_Cloud.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_reposo_python_pandas.md", "Cap\u00edtulo 1: Repaso R\u00e1pido \u2014 Python y pandas"),
            ("06_capitulo2_pandas_avanzado.md", "Cap\u00edtulo 2: pandas Avanzado"),
            ("07_capitulo3_limpieza_datos.md", "Cap\u00edtulo 3: Limpieza de Datos Reales"),
            ("08_capitulo4_visualizacion.md", "Cap\u00edtulo 4: Visualizaci\u00f3n"),
            ("09_capitulo5_eda_completo.md", "Cap\u00edtulo 5: EDA Completo"),
            ("checkpoint1_eda_techstore.md", "Checkpoint 1: EDA Completo de TechStore"),
            ("10_capitulo6_cloud_computing.md", "Cap\u00edtulo 6: Cloud Computing"),
            ("11_capitulo7_gcp_configuracion.md", "Cap\u00edtulo 7: GCP Configuraci\u00f3n"),
            ("12_capitulo8_bigquery_intro.md", "Cap\u00edtulo 8: BigQuery Intro"),
            ("13_capitulo9_bigquery_avanzado.md", "Cap\u00edtulo 9: BigQuery Avanzado"),
            ("14_capitulo10_python_bigquery.md", "Cap\u00edtulo 10: Python + BigQuery"),
            ("15_checkpoint2_migrar_techstore.md", "Checkpoint 2: Migrar TechStore a BigQuery"),
            ("16_capitulo11_bigquery_sql_analitico.md", "Cap\u00edtulo 11: SQL Anal\u00edtico y Nested Fields"),
            ("17_capitulo12_data_pipelines.md", "Cap\u00edtulo 12: Data Pipelines"),
            ("18_capitulo13_looker_studio_intro.md", "Cap\u00edtulo 13: Looker Studio"),
            ("19_capitulo14_looker_avanzado.md", "Cap\u00edtulo 14: Looker Studio Avanzado"),
            ("20_checkpoint3_dashboard_cloud.md", "Checkpoint 3: Dashboard Cloud"),
            ("21_capitulo15_cloud_functions.md", "Cap\u00edtulo 15: Cloud Functions"),
            ("22_capitulo16_schedule_queries.md", "Cap\u00edtulo 16: Schedule Queries"),
            ("23_capitulo17_proyecto_final.md", "Cap\u00edtulo 17: Proyecto Final"),
            ("24_checkpoint4_pipeline_automatizado.md", "Checkpoint 4: Pipeline Automatizado"),
            ("25_conclusion.md", "Conclusi\u00f3n"),
            ("26_apendice_a_soluciones.md", "Ap\u00e9ndice A: Soluciones"),
            ("27_apendice_b_cheatsheets.md", "Ap\u00e9ndice B: Cheatsheets"),
            ("28_apendice_c_gcp_costes.md", "Ap\u00e9ndice C: GCP y Costes"),
            ("29_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "business_intelligence_bi",
        "category": "Datos_IA",
        "id": "business-intelligence-powerbi",
        "title": "Business Intelligence y Modelado de Datos",
        "subtitle": "Dise\u00f1a dashboards profesionales y modela datos como un experto",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Business_Intelligence_BI.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_intro_bi.md", "Cap\u00edtulo 1: Introducci\u00f3n al BI"),
            ("06_capitulo2_arquitectura_datos.md", "Cap\u00edtulo 2: Arquitectura de Datos"),
            ("07_capitulo3_modelado_dimensional.md", "Cap\u00edtulo 3: Modelado Dimensional"),
            ("08_capitulo4_kpis_metricas.md", "Cap\u00edtulo 4: KPIs y M\u00e9tricas"),
            ("09_checkpoint1_modelo_dimensional.md", "Checkpoint 1: Modelo Dimensional"),
            ("10_capitulo5_powerbi_primeros_pasos.md", "Cap\u00edtulo 5: Power BI \u2014 Primeros Pasos"),
            ("11_capitulo6_powerbi_modelado.md", "Cap\u00edtulo 6: Modelado en Power BI"),
            ("12_capitulo7_powerbi_visualizaciones.md", "Cap\u00edtulo 7: Visualizaciones"),
            ("13_capitulo8_dax_basico.md", "Cap\u00edtulo 8: DAX B\u00e1sico"),
            ("14_checkpoint2_dashboard_powerbi.md", "Checkpoint 2: Dashboard Power BI"),
            ("15_capitulo9_dax_avanzado.md", "Cap\u00edtulo 9: DAX Avanzado"),
            ("16_capitulo10_power_query_etl.md", "Cap\u00edtulo 10: Power Query ETL"),
            ("17_capitulo11_data_warehousing.md", "Cap\u00edtulo 11: Data Warehousing"),
            ("18_capitulo12_medidas_avanzadas.md", "Cap\u00edtulo 12: Medidas Avanzadas"),
            ("19_checkpoint3_modelo_semantico.md", "Checkpoint 3: Modelo Sem\u00e1ntico"),
            ("20_capitulo13_powerbi_service.md", "Cap\u00edtulo 13: Power BI Service"),
            ("21_capitulo14_seguridad_rls.md", "Cap\u00edtulo 14: Seguridad RLS"),
            ("22_capitulo15_proyecto_final.md", "Cap\u00edtulo 15: Proyecto Final"),
            ("23_checkpoint4_portal_bi.md", "Checkpoint 4: Portal BI Corporativo"),
            ("24_conclusion.md", "Conclusi\u00f3n"),
            ("25_apendice_a_soluciones.md", "Ap\u00e9ndice A: Soluciones"),
            ("26_apendice_b_cheatsheets.md", "Ap\u00e9ndice B: Cheatsheets"),
            ("27_apendice_c_costes_powerbi.md", "Ap\u00e9ndice C: Costes y Licencias"),
            ("28_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "ingenieria_datos_moderna",
        "category": "Datos_IA",
        "id": "ingenieria-datos-moderna",
        "title": "Ingenier\u00eda de Datos Moderna",
        "subtitle": "Domina el data engineering moderno con Python, Airflow y dbt",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Ingenieria_Datos_Moderna.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_intro_data_engineering.md", "Cap\u00edtulo 1: Introducci\u00f3n al Data Engineering"),
            ("06_capitulo2_python_data_engineering.md", "Cap\u00edtulo 2: Python para Data Engineering"),
            ("07_capitulo3_formatos_datos.md", "Cap\u00edtulo 3: Formatos de Datos"),
            ("08_capitulo4_data_lakes_minio.md", "Cap\u00edtulo 4: Data Lakes y MinIO"),
            ("09_checkpoint1_data_lake_techstore.md", "Checkpoint 1: Data Lake TechStore"),
            ("10_capitulo5_intro_dbt.md", "Cap\u00edtulo 5: Introducci\u00f3n a dbt"),
            ("11_capitulo6_modelado_dbt.md", "Cap\u00edtulo 6: Modelado en dbt"),
            ("12_capitulo7_testing_documentacion_dbt.md", "Cap\u00edtulo 7: Testing y Documentaci\u00f3n"),
            ("13_capitulo8_dbt_avanzado.md", "Cap\u00edtulo 8: dbt Avanzado"),
            ("14_checkpoint2_pipeline_dbt.md", "Checkpoint 2: Pipeline dbt"),
            ("15_capitulo9_intro_airflow.md", "Cap\u00edtulo 9: Introducci\u00f3n a Airflow"),
            ("16_capitulo10_airflow_avanzado.md", "Cap\u00edtulo 10: Airflow Avanzado"),
            ("17_capitulo11_airflow_dbt.md", "Cap\u00edtulo 11: Airflow + dbt"),
            ("18_capitulo12_monitoreo_alertas.md", "Cap\u00edtulo 12: Monitoreo y Alertas"),
            ("19_checkpoint3_orquestacion_completa.md", "Checkpoint 3: Orquestaci\u00f3n Completa"),
            ("20_capitulo13_docker_data.md", "Cap\u00edtulo 13: Docker para DE"),
            ("21_capitulo14_cicd_datos.md", "Cap\u00edtulo 14: CI/CD para Datos"),
            ("22_capitulo15_proyecto_final.md", "Cap\u00edtulo 15: Proyecto Final"),
            ("23_checkpoint4_data_platform.md", "Checkpoint 4: Data Platform"),
            ("24_conclusion.md", "Conclusi\u00f3n"),
            ("25_apendice_a_soluciones.md", "Ap\u00e9ndice A: Soluciones"),
            ("26_apendice_b_cheatsheets.md", "Ap\u00e9ndice B: Cheatsheets"),
            ("27_apendice_c_instalacion.md", "Ap\u00e9ndice C: Instalaci\u00f3n"),
            ("28_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "big_data_ml_ia",
        "category": "Datos_IA",
        "id": "big-data-ml-ia",
        "title": "Big Data, ML e IA",
        "subtitle": "Domina el big data, machine learning e inteligencia artificial con proyectos pr\u00e1cticos",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Big_Data_ML_IA.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_intro_big_data.md", "Cap\u00edtulo 1: Introducci\u00f3n al Big Data"),
            ("06_capitulo2_pyspark_fundamentos.md", "Cap\u00edtulo 2: PySpark - Procesamiento Distribuido"),
            ("07_capitulo3_procesamiento_datos.md", "Cap\u00edtulo 3: Procesamiento de Datos a Escala"),
            ("08_capitulo4_streaming_datos.md", "Cap\u00edtulo 4: Datos en Streaming"),
            ("09_checkpoint1_pipeline_big_data.md", "Checkpoint 1: Pipeline Big Data"),
            ("10_capitulo5_intro_ml.md", "Cap\u00edtulo 5: Introducci\u00f3n al ML"),
            ("11_capitulo6_aprendizaje_supervisado.md", "Cap\u00edtulo 6: Aprendizaje Supervisado"),
            ("12_capitulo7_aprendizaje_no_supervisado.md", "Cap\u00edtulo 7: Aprendizaje No Supervisado"),
            ("13_capitulo8_evaluacion_modelos.md", "Cap\u00edtulo 8: Evaluaci\u00f3n de Modelos"),
            ("14_checkpoint2_modelo_techstore.md", "Checkpoint 2: Modelo TechStore"),
            ("15_capitulo9_deep_learning.md", "Cap\u00edtulo 9: Deep Learning"),
            ("16_capitulo10_nlp_texto.md", "Cap\u00edtulo 10: NLP"),
            ("17_capitulo11_series_temporales.md", "Cap\u00edtulo 11: Series Temporales"),
            ("18_capitulo12_mlops_mlflow.md", "Cap\u00edtulo 12: MLOps"),
            ("19_checkpoint3_pipeline_ml.md", "Checkpoint 3: Pipeline ML"),
            ("20_capitulo13_llms_ia_generativa.md", "Cap\u00edtulo 13: LLMs e IA Generativa"),
            ("21_capitulo14_ml_cloud.md", "Cap\u00edtulo 14: ML en la Nube"),
            ("22_capitulo15_proyecto_final.md", "Cap\u00edtulo 15: Proyecto Final"),
            ("23_checkpoint4_plataforma_ia.md", "Checkpoint 4: Plataforma IA"),
            ("24_conclusion.md", "Conclusi\u00f3n"),
            ("25_apendice_a_soluciones.md", "Ap\u00e9ndice A: Soluciones"),
            ("26_apendice_b_cheatsheets.md", "Ap\u00e9ndice B: Cheatsheets"),
            ("27_apendice_c_instalacion.md", "Ap\u00e9ndice C: Instalaci\u00f3n"),
            ("28_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "freelancer_datos",
        "category": "Datos_IA",
        "id": "freelancer-datos",
        "title": "Freelancer de Datos",
        "subtitle": "Gu\u00eda para convertirte en un analista freelance exitoso",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Freelancer_Datos.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_mercado_freelance.md", "Cap\u00edtulo 1: El Mercado Freelance en Datos"),
            ("06_capitulo2_habilidades_pricing.md", "Cap\u00edtulo 2: Habilidades y Pricing"),
            ("07_capitulo3_conseguir_clientes.md", "Cap\u00edtulo 3: C\u00f3mo Conseguir Clientes"),
            ("08_capitulo4_marca_personal.md", "Cap\u00edtulo 4: Marca Personal y Reputaci\u00f3n"),
            ("09_capitulo5_stack_tecnico.md", "Cap\u00edtulo 5: Stack T\u00e9cnico del Freelancer"),
            ("10_capitulo6_ia_asistente.md", "Cap\u00edtulo 6: IA como Asistente de Datos"),
            ("11_capitulo7_automatizacion.md", "Cap\u00edtulo 7: Automatizaci\u00f3n de Informes"),
            ("12_capitulo8_recursos_web.md", "Cap\u00edtulo 8: Recursos Web y Plataformas"),
            ("13_capitulo9_storytelling.md", "Cap\u00edtulo 9: Storytelling con Datos"),
            ("14_capitulo10_visualizaciones.md", "Cap\u00edtulo 10: Visualizaciones que Impactan"),
            ("15_capitulo11_entregables.md", "Cap\u00edtulo 11: Entregables Profesionales"),
            ("16_capitulo12_presentacion.md", "Cap\u00edtulo 12: Presentaci\u00f3n de Resultados"),
            ("17_capitulo13_pricing.md", "Cap\u00edtulo 13: C\u00f3mo Poner Precio a tu Trabajo"),
            ("18_capitulo14_marca_personal.md", "Cap\u00edtulo 14: Construye tu Marca Personal"),
            ("19_capitulo15_dia_a_dia.md", "Cap\u00edtulo 15: El D\u00eda a D\u00eda del Freelancer"),
            ("20_conclusion.md", "Conclusi\u00f3n"),
            ("21_apendice_a_herramientas.md", "Ap\u00e9ndice A: Herramientas Recomendadas"),
            ("22_apendice_b_plantillas.md", "Ap\u00e9ndice B: Plantillas y Recursos"),
            ("23_apendice_c_recursos.md", "Ap\u00e9ndice C: Lecturas Recomendadas"),
            ("24_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "agentes_ia_negocios",
        "category": "Datos_IA",
        "id": "agentes-ia-negocios",
        "title": "Agentes de IA para Peque\u00f1as Empresas",
        "subtitle": "Gu\u00eda pr\u00e1ctica para transformar tu negocio con inteligencia artificial sin ser t\u00e9cnico",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Agentes_IA_Negocios.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_que_es_agente_ia.md", "Cap\u00edtulo 1: Qu\u00e9 es un Agente de IA"),
            ("06_capitulo2_herramientas_gratuitas.md", "Cap\u00edtulo 2: Herramientas Gratuitas que ya Tienes"),
            ("07_capitulo3_donde_no_usar_ia.md", "Cap\u00edtulo 3: D\u00f3nde NO Usar IA"),
            ("08_capitulo4_atencion_cliente.md", "Cap\u00edtulo 4: Atenci\u00f3n al Cliente Automatizada"),
            ("09_capitulo5_marketing_redes.md", "Cap\u00edtulo 5: Marketing y Redes Sociales"),
            ("10_capitulo6_administracion.md", "Cap\u00edtulo 6: Administraci\u00f3n y Finanzas"),
            ("11_capitulo7_organizacion_productividad.md", "Cap\u00edtulo 7: Organizaci\u00f3n y Productividad"),
            ("12_capitulo8_primer_agente.md", "Cap\u00edtulo 8: C\u00f3mo Montar tu Primer Agente en 30 Minutos"),
            ("13_capitulo9_casos_estudio.md", "Cap\u00edtulo 9: 5 Casos de Estudio Reales"),
            ("14_capitulo10_futuro.md", "Cap\u00edtulo 10: El Futuro \u2014 Qu\u00e9 Esperar en 2027"),
            ("15_conclusion.md", "Conclusi\u00f3n"),
            ("16_recursos.md", "Recursos y Referencias"),
            ("17_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "codigo_asesino",
        "category": "Programacion",
        "id": "codigo-asesino-enigma-qhapaq-nan",
        "title": "C\u00f3digo Asesino: El Enigma de Qhapaq \u00d1an",
        "subtitle": "Una Saga de Misterio, Tecnolog\u00eda y Memoria Ancestral",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Codigo_Asesino.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_el_asesinato.md", "Cap\u00edtulo 1: El Asesinato"),
            ("06_capitulo2_los_nudos_del_quipu.md", "Cap\u00edtulo 2: Los Nudos del Quipu"),
            ("07_capitulo3_la_lista_de_sospechosos.md", "Cap\u00edtulo 3: La Lista de Sospechosos"),
            ("08_capitulo4_el_diccionario_de_inti.md", "Cap\u00edtulo 4: El Diccionario de Inti"),
            ("09_capitulo5_el_interrogatorio.md", "Cap\u00edtulo 5: El Interrogatorio"),
            ("10_capitulo6_la_ruta_del_inca.md", "Cap\u00edtulo 6: La Ruta del Inca"),
            ("11_capitulo7_las_funciones_del_saber.md", "Cap\u00edtulo 7: Las Funciones del Saber"),
            ("12_capitulo8_los_archivos_del_laboratorio.md", "Cap\u00edtulo 8: Los Archivos del Laboratorio"),
            ("13_capitulo9_el_circulo_del_sol.md", "Cap\u00edtulo 9: El C\u00edrculo del Sol"),
            ("14_capitulo10_los_modulos_del_heredero.md", "Cap\u00edtulo 10: Los M\u00f3dulos del Heredero"),
            ("15_capitulo11_la_clase_del_misterio.md", "Cap\u00edtulo 11: La Clase del Misterio"),
            ("16_capitulo12_la_herencia_de_los_incas.md", "Cap\u00edtulo 12: La Herencia de los Incas"),
            ("17_capitulo13_el_codigo_asesino_parte1.md", "Cap\u00edtulo 13: El C\u00f3digo Asesino (Parte 1)"),
            ("18_capitulo14_el_codigo_asesino_parte2.md", "Cap\u00edtulo 14: El C\u00f3digo Asesino (Parte 2)"),
            ("19_capitulo15_el_epilogo.md", "Cap\u00edtulo 15: El Ep\u00edlogo"),
            ("20_conclusion.md", "Conclusi\u00f3n"),
            ("21_apendice_soluciones.md", "Ap\u00e9ndice: Soluciones"),
            ("22_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "codigo_de_olas",
        "category": "Programacion",
        "id": "codigo-de-olas-misterio-ancon",
        "title": "C\u00f3digo de Olas: El Misterio del Puerto de Anc\u00f3n",
        "subtitle": "Una Historia de Surf, Tecnolog\u00eda y el Secreto del Mar",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Codigo_De_Olas.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_el_secreto_de_la_playa.md", "Cap\u00edtulo 1: El Secreto de la Playa"),
            ("06_capitulo2_el_lenguaje_del_mar.md", "Cap\u00edtulo 2: El Lenguaje del Mar"),
            ("07_capitulo3_la_lista_de_implicados.md", "Cap\u00edtulo 3: La Lista de Implicados"),
            ("08_capitulo4_el_diccionario_del_pescador.md", "Cap\u00edtulo 4: El Diccionario del Pescador"),
            ("09_capitulo5_la_decision_de_la_ola.md", "Cap\u00edtulo 5: La Decisi\u00f3n de la Ola"),
            ("10_capitulo6_el_viaje_de_mateo.md", "Cap\u00edtulo 6: El Viaje de Mateo"),
            ("11_capitulo7_las_funciones_del_mar.md", "Cap\u00edtulo 7: Las Funciones del Mar"),
            ("12_capitulo8_los_archivos_del_puerto.md", "Cap\u00edtulo 8: Los Archivos del Puerto"),
            ("13_capitulo9_el_error_en_la_red.md", "Cap\u00edtulo 9: El Error en la Red"),
            ("14_capitulo10_los_modulos_del_puerto.md", "Cap\u00edtulo 10: Los M\u00f3dulos del Puerto"),
            ("15_capitulo11_la_clase_del_surfista.md", "Cap\u00edtulo 11: La Clase del Surfista"),
            ("16_capitulo12_la_herencia_del_mar.md", "Cap\u00edtulo 12: La Herencia del Mar"),
            ("17_capitulo13_el_proyecto_integrador.md", "Cap\u00edtulo 13: El Proyecto Integrador"),
            ("18_capitulo14_revelacion_en_el_muelle.md", "Cap\u00edtulo 14: Revelaci\u00f3n en el Muelle"),
            ("19_capitulo15_epilogo_ola_libre.md", "Cap\u00edtulo 15: Ep\u00edlogo — Ola Libre"),
            ("20_conclusion.md", "Conclusi\u00f3n"),
            ("21_apendice_soluciones.md", "Ap\u00e9ndice: Soluciones"),
            ("22_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "estadistica_mortal",
        "category": "Programacion",
        "id": "estadistica-mortal-conjunto-vacio",
        "title": "Estad\u00edstica Mortal: El Enigma del Conjunto Vac\u00edo",
        "subtitle": "Una Novela de Misterio, Datos y Probabilidades",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Estadistica_Mortal.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_el_conjunto_vacio.md", "Cap\u00edtulo 1: El Conjunto Vac\u00edo"),
            ("06_capitulo2_la_probabilidad_del_crimen.md", "Cap\u00edtulo 2: La Probabilidad del Crimen"),
            ("07_capitulo3_el_teorema_del_sospechoso.md", "Cap\u00edtulo 3: El Teorema del Sospechoso"),
            ("08_capitulo4_la_distribucion_del_engano.md", "Cap\u00edtulo 4: La Distribuci\u00f3n del Enga\u00f1o"),
            ("09_capitulo5_la_muestra_que_miente.md", "Cap\u00edtulo 5: La Muestra que Miente"),
            ("10_capitulo6_la_hipotesis_asesina.md", "Cap\u00edtulo 6: La Hip\u00f3tesis Asesina"),
            ("11_capitulo7_la_correlacion_del_secreto.md", "Cap\u00edtulo 7: La Correlaci\u00f3n del Secreto"),
            ("12_capitulo8_la_regresion_del_pasado.md", "Cap\u00edtulo 8: La Regresi\u00f3n del Pasado"),
            ("13_capitulo9_el_intervalo_de_confianza.md", "Cap\u00edtulo 9: El Intervalo de Confianza"),
            ("14_capitulo10_la_varianza_del_silencio.md", "Cap\u00edtulo 10: La Varianza del Silencio"),
            ("15_capitulo11_la_prueba_del_chi_cuadrado.md", "Cap\u00edtulo 11: La Prueba del Chi\u2011Cuadrado"),
            ("16_capitulo12_la_serie_del_tiempo_perdido.md", "Cap\u00edtulo 12: La Serie del Tiempo Perdido"),
            ("17_capitulo13_el_ultimo_conjunto_parte1.md", "Cap\u00edtulo 13: El \u00daltimo Conjunto (Parte 1)"),
            ("18_capitulo14_el_ultimo_conjunto_parte2.md", "Cap\u00edtulo 14: El \u00daltimo Conjunto (Parte 2)"),
            ("19_capitulo15_el_epilogo.md", "Cap\u00edtulo 15: El Ep\u00edlogo"),
            ("20_conclusion.md", "Conclusi\u00f3n"),
            ("21_apendice_soluciones.md", "Ap\u00e9ndice: Soluciones"),
            ("22_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "sql_letal",
        "category": "Programacion",
        "id": "sql-letal-misterio-base-datos",
        "title": "SQL Letal: El Misterio de la Base de Datos",
        "subtitle": "Una Novela de Misterio, Datos y Consultas",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "SQL_Letal_Misterio_Base_Datos.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_cap1_select.md", "Cap\u00edtulo 1: SELECT — Los Primeros Datos"),
            ("06_cap2_where.md", "Cap\u00edtulo 2: WHERE — Filtrando Pistas"),
            ("07_cap3_joins.md", "Cap\u00edtulo 3: JOINs — Conectando los Puntos"),
            ("08_cap4_groupby.md", "Cap\u00edtulo 4: GROUP BY — Agrupando Sospechosos"),
            ("09_cap5_fechas.md", "Cap\u00edtulo 5: Fechas — La L\u00ednea del Tiempo"),
            ("10_cap6_subconsultas.md", "Cap\u00edtulo 6: Subconsultas — El Caso Interno"),
            ("11_cap7_indices.md", "Cap\u00edtulo 7: \u00cdndices — Accelerando la B\u00fasqueda"),
            ("12_cap8_vistas.md", "Cap\u00edtulo 8: Vistas — La Perspectiva Correcta"),
            ("13_cap9_transacciones.md", "Cap\u00edtulo 9: Transacciones — Todo o Nada"),
            ("14_cap10_funciones.md", "Cap\u00edtulo 10: Funciones — El Poder de la Base"),
            ("15_cap11_triggers.md", "Cap\u00edtulo 11: Triggers — El \u00daltimo Guardi\u00e1n"),
            ("16_cap12_normalizacion.md", "Cap\u00edtulo 12: Normalizaci\u00f3n — El Orden Perfecto"),
            ("17_cap13_ctes.md", "Cap\u00edtulo 13: CTEs — La Consulta que lo Cambia Todo"),
            ("18_cap14_window.md", "Cap\u00edtulo 14: Window Functions — Viendo M\u00e1s All\u00e1"),
            ("19_cap15_epilogo.md", "Cap\u00edtulo 15: Ep\u00edlogo"),
            ("20_conclusion.md", "Conclusi\u00f3n"),
            ("21_apendice_soluciones.md", "Ap\u00e9ndice: Soluciones"),
            ("22_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "motor_cuantitativo",
        "category": "Matematicas",
        "id": "motor-cuantitativo",
        "title": "El Motor Cuantitativo",
        "subtitle": "Fundamentos Matem\u00e1ticos y Estad\u00edsticos con Python para el An\u00e1lisis de Datos",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "El_Motor_Cuantitativo.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_modulo1_1_ecosistema.md", "M\u00f3dulo 1.1: El Ecosistema del An\u00e1lisis"),
            ("06_modulo1_2_algebra_lineal.md", "M\u00f3dulo 1.2: \u00c1lgebra Lineal"),
            ("07_modulo1_3_calculo_diferencial.md", "M\u00f3dulo 1.3: C\u00e1lculo Diferencial"),
            ("08_modulo2_1_medidas_descriptivas.md", "M\u00f3dulo 2.1: Medidas Descriptivas"),
            ("09_modulo2_2_probabilidad.md", "M\u00f3dulo 2.2: Probabilidad"),
            ("10_modulo2_3_distribuciones.md", "M\u00f3dulo 2.3: Distribuciones"),
            ("11_modulo2_4_tlc.md", "M\u00f3dulo 2.4: Teorema del L\u00edmite Central"),
            ("12_modulo3_1_poblacion_muestra.md", "M\u00f3dulo 3.1: Poblaci\u00f3n y Muestra"),
            ("13_modulo3_2_intervalos_confianza.md", "M\u00f3dulo 3.2: Intervalos de Confianza"),
            ("14_modulo3_3_pruebas_hipotesis.md", "M\u00f3dulo 3.3: Pruebas de Hip\u00f3tesis"),
            ("15_modulo3_4_tests_python.md", "M\u00f3dulo 3.4: Tests Estad\u00edsticos en Python"),
            ("16_modulo4_1_fundamentos_experimentales.md", "M\u00f3dulo 4.1: Fundamentos Experimentales"),
            ("17_modulo4_2_ab_testing_python.md", "M\u00f3dulo 4.2: A/B Testing en Python"),
            ("18_modulo4_3_errores_comunes.md", "M\u00f3dulo 4.3: Errores Comunes en Experimentos"),
            ("19_modulo5_1_correlacion_causalidad.md", "M\u00f3dulo 5.1: Correlaci\u00f3n y Causalidad"),
            ("20_modulo5_2_regresion_lineal.md", "M\u00f3dulo 5.2: Regresi\u00f3n Lineal"),
            ("21_modulo5_3_evaluacion_modelos.md", "M\u00f3dulo 5.3: Evaluaci\u00f3n de Modelos"),
            ("22_modulo5_4_regresion_logistica.md", "M\u00f3dulo 5.4: Regresi\u00f3n Log\u00edstica"),
            ("23_modulo6_1_pca.md", "M\u00f3dulo 6.1: PCA — Componentes Principales"),
            ("24_modulo6_2_kmeans.md", "M\u00f3dulo 6.2: K\u2011Means — Clustering"),
            ("25_modulo6_3_series_temporales.md", "M\u00f3dulo 6.3: Series Temporales"),
            ("26_modulo7_1_flujo_trabajo.md", "M\u00f3dulo 7.1: Flujo de Trabajo en la Pr\u00e1ctica"),
            ("27_modulo7_2_datos_faltantes.md", "M\u00f3dulo 7.2: Manejo de Datos Faltantes"),
            ("28_modulo7_3_comunicacion.md", "M\u00f3dulo 7.3: Comunicaci\u00f3n de Resultados"),
            ("29_conclusion.md", "Conclusi\u00f3n"),
            ("30_apendice_a.md", "Ap\u00e9ndice A: Referencia R\u00e1pida"),
            ("31_apendice_b.md", "Ap\u00e9ndice B: Tablas Estad\u00edsticas"),
            ("32_referencias.md", "Referencias"),
            ("33_sobre_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "print_Sigo_Aqui",
        "category": "Crecimiento_Personal",
        "id": "print-sigo-aqui",
        "title": "print(\"Sigo Aqu\u00ed\")",
        "subtitle": "El viaje de un inform\u00e1tico sin papeles",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "print_Sigo_Aqui.epub",
        "chapter_map": [
            ("00_prologo.md", "Pr\u00f3logo"),
            ("01_capitulo1_llegada_madrid.md", "Cap\u00edtulo 1: La Llegada a Madrid"),
            ("02_capitulo2_naranjas_amargas.md", "Cap\u00edtulo 2: Naranjas Amargas"),
            ("03_capitulo3_polvo_y_cemento.md", "Cap\u00edtulo 3: Polvo y Cemento"),
            ("04_capitulo4_fibra_en_el_norte.md", "Cap\u00edtulo 4: Fibra en el Norte"),
            ("05_capitulo5_si_reclamas_me_consigo_a_otro.md", "Cap\u00edtulo 5: Si Reclamas me Consigo a Otro"),
            ("06_capitulo6_codigo_en_la_madrugada.md", "Cap\u00edtulo 6: C\u00f3digo en la Madrugada"),
            ("07_capitulo7_la_entrevista.md", "Cap\u00edtulo 7: La Entrevista"),
            ("08_capitulo8_los_papeles.md", "Cap\u00edtulo 8: Los Papeles"),
            ("09_capitulo9_data_analyst.md", "Cap\u00edtulo 9: Data Analyst"),
            ("10_epilogo.md", "Ep\u00edlogo"),
            ("11_apendice_recursos.md", "Ap\u00e9ndice: Recursos"),
            ("12_sobre_el_autor.md", "Sobre el Autor"),
        ],
    },
    {
        "folder": "raices_nuevas",
        "category": "Crecimiento_Personal",
        "id": "raices-nuevas",
        "title": "Ra\u00edces Nuevas",
        "subtitle": "Gu\u00eda Pr\u00e1ctica para Combatir la Ansiedad del Inmigrante",
        "author": "Alex Goyzueta Delgado",
        "epub_filename": "Raices_Nuevas.epub",
        "chapter_map": [
            ("00_portada.md", "Portada"),
            ("01_creditos.md", "Cr\u00e9ditos"),
            ("02_dedicatoria.md", "Dedicatoria"),
            ("03_prefacio.md", "Prefacio"),
            ("04_introduccion.md", "Introducci\u00f3n"),
            ("05_capitulo1_lo_que_nadie_te_dice.md", "Cap\u00edtulo 1: Lo Que Nadie Te Dice"),
            ("06_capitulo2_la_ansiedad.md", "Cap\u00edtulo 2: La Ansiedad"),
            ("07_capitulo3_el_duelo_migratorio.md", "Cap\u00edtulo 3: El Duelo Migratorio"),
            ("08_capitulo4_respirar_y_ancorarte.md", "Cap\u00edtulo 4: Respirar y Ancorarte"),
            ("09_capitulo5_el_poder_de_las_rutinas.md", "Cap\u00edtulo 5: El Poder de las Rutinas"),
            ("10_capitulo6_conectar_sin_forzar.md", "Cap\u00edtulo 6: Conectar sin Forzar"),
            ("11_capitulo7_el_idioma.md", "Cap\u00edtulo 7: El Idioma"),
            ("12_capitulo8_mover_el_cuerpo.md", "Cap\u00edtulo 8: Mover el Cuerpo"),
            ("13_capitulo9_limites_sanos.md", "Cap\u00edtulo 9: L\u00edmites Sanos"),
            ("14_capitulo10_cuando_buscar_ayuda.md", "Cap\u00edtulo 10: Cu\u00e1ndo Buscar Ayuda"),
            ("15_capitulo11_tu_identidad.md", "Cap\u00edtulo 11: Tu Identidad"),
            ("16_capitulo12_celebrar_lo_pequeno.md", "Cap\u00edtulo 12: Celebrar lo Peque\u00f1o"),
            ("17_conclusion.md", "Conclusi\u00f3n"),
            ("18_apendice_recursos.md", "Ap\u00e9ndice: Recursos"),
            ("19_sobre_el_autor.md", "Sobre el Autor"),
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

    book_dir = os.path.join(BASE, "libros", book_config.get("category", ""), book_config["folder"])

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
