import os, re
from fpdf import FPDF

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONT_DIR = "C:\\Windows\\Fonts"

BOOKS = [
    {
        "folder": "excel_basico",
        "category": "Excel",
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
        "category": "Excel",
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
        "category": "Excel",
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
    {
        "folder": "excel_contadores",
        "category": "Excel",
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
    {
        "folder": "excel_analisis_datos",
        "category": "Excel",
        "pdf_filename": "Excel_Analisis_Datos.pdf",
        "title": "Excel para An\u00e1lisis de Datos",
        "subtitle": "De los datos crudos a las decisiones inteligentes",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_proceso_analisis_datos.md",
            "06_limpieza_datos.md", "07_eda.md",
            "08_funciones_analisis.md", "09_tendencias.md",
            "10_tablas_dinamicas.md", "11_visualizacion.md",
            "12_escenarios.md", "13_powerquery.md",
            "14_proyecto_final.md",
        ],
    },
    {
        "folder": "excel_copilot",
        "category": "Excel",
        "pdf_filename": "Excel_con_Copilot.pdf",
        "title": "Excel con Copilot: Tu Asistente Inteligente",
        "subtitle": "Una Novela para Dominar Excel con Inteligencia Artificial",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_primeros_pasos.md",
            "06_capitulo2_conversando_datos.md", "07_capitulo3_formulas_sin_esfuerzo.md",
            "08_capitulo4_analisis_instantaneo.md", "09_capitulo5_visualizaciones_magicas.md",
            "10_capitulo6_limpieza_datos.md", "11_capitulo7_power_query_copilot.md",
            "12_capitulo8_automatizacion_inteligente.md", "13_capitulo9_dashboard_inteligente.md",
            "14_capitulo10_proyecto_final.md", "15_conclusion.md",
            "16_sobre_el_autor.md",
        ],
    },
    {
        "folder": "html_basico",
        "category": "Web",
        "pdf_filename": "HTML_Basico.pdf",
        "title": "HTML B\u00e1sico: El C\u00f3digo de la Web",
        "subtitle": "Una Novela para Aprender HTML Desde Cero",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_el_desafio_de_la_web.md",
            "06_capitulo2_las_primeras_palabras.md", "07_capitulo3_el_mapa_del_sitio.md",
            "08_capitulo4_organizando_la_informacion.md", "09_capitulo5_la_voz_del_barrio.md",
            "10_capitulo6_el_significado_de_las_cosas.md", "11_capitulo7_mas_alla_del_texto.md",
            "12_capitulo8_el_codigo_invisible.md", "13_capitulo9_para_todos.md",
            "14_capitulo10_la_gran_publicacion.md", "15_conclusion.md",
            "16_apendice_soluciones.md", "17_sobre_el_autor.md",
        ],
    },
    {
        "folder": "css_basico",
        "category": "Web",
        "pdf_filename": "CSS_Basico.pdf",
        "title": "CSS B\u00e1sico: El Dise\u00f1o que Transforma la Web",
        "subtitle": "Una Novela para Aprender CSS Desde Cero",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_el_primer_estilo.md",
            "06_capitulo2_la_paleta_de_colores.md", "07_capitulo3_el_espacio_entre_lineas.md",
            "08_capitulo4_poniendo_orden.md", "09_capitulo5_flexibilidad.md",
            "10_capitulo6_la_grilla_perfecta.md", "11_capitulo7_adaptandose_al_mundo.md",
            "12_capitulo8_el_toque_magico.md", "13_capitulo9_detalles_que_importan.md",
            "14_capitulo10_el_lanzamiento.md", "15_conclusion.md",
            "16_apendice_soluciones.md", "17_sobre_el_autor.md",
        ],
    },
    {
        "folder": "js_basico",
        "category": "Web",
        "pdf_filename": "JS_Basico.pdf",
        "title": "JavaScript B\u00e1sico: El Poder de la Interactividad",
        "subtitle": "Una Novela para Aprender JavaScript Desde Cero",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_el_primer_script.md",
            "06_capitulo2_tomando_decisiones.md", "07_capitulo3_las_funciones_del_conocimiento.md",
            "08_capitulo4_listas_y_colecciones.md", "09_capitulo5_la_vida_en_la_pagina.md",
            "10_capitulo6_transformando_la_interfaz.md", "11_capitulo7_formularios_inteligentes.md",
            "12_capitulo8_guardando_el_progreso.md", "13_capitulo9_conectando_con_el_mundo.md",
            "14_capitulo10_la_gran_demo.md", "15_conclusion.md",
            "16_apendice_soluciones.md", "17_sobre_el_autor.md",
        ],
    },
    {
        "folder": "fundamentos_analista_datos",
        "category": "Datos_IA",
        "pdf_filename": "Fundamentos_Analista_Datos.pdf",
        "title": "Los Fundamentos del Analista de Datos",
        "subtitle": "Domina SQL, Excel y Python desde cero",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_ecosistema_analista.md",
            "06_capitulo2_sql_select_basico.md", "07_capitulo3_sql_where_filtros.md",
            "08_capitulo4_excel_importar_formato.md", "09_capitulo5_python_variables_tipos.md",
            "10_checkpoint_1_analizando_ventas_basicas.md",
            "11_capitulo6_sql_agregacion.md", "12_capitulo7_sql_joins.md",
            "13_capitulo8_excel_tablas_dinamicas.md", "14_capitulo9_python_estructuras_datos.md",
            "15_capitulo10_excel_graficos.md", "16_checkpoint_2_top_productos.md",
            "17_capitulo11_sql_subconsultas_cte.md", "18_capitulo12_sql_window_functions.md",
            "19_capitulo13_excel_power_query.md", "20_capitulo14_python_funciones.md",
            "21_capitulo15_excel_dax_basico.md", "22_checkpoint_3_cohortes.md",
            "23_capitulo16_python_sql_excel.md", "24_capitulo17_modelo_datos_dashboard.md",
            "25_capitulo18_proyecto_final.md", "26_checkpoint_4_pipeline_automatizado.md",
            "27_conclusion.md", "28_apendice_a_soluciones.md",
            "29_apendice_b_cheatsheets.md", "30_apendice_c_instalacion.md",
            "31_sobre_el_autor.md",
        ],
    },
    {
        "folder": "python_data_cloud",
        "category": "Datos_IA",
        "pdf_filename": "Python_Data_Cloud.pdf",
        "title": "Python para Datos y tu Primer Data Warehouse Cloud",
        "subtitle": "De Pandas a BigQuery: an\u00e1lisis profesional en la nube",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_reposo_python_pandas.md",
            "06_capitulo2_pandas_avanzado.md", "07_capitulo3_limpieza_datos.md",
            "08_capitulo4_visualizacion.md", "09_capitulo5_eda_completo.md",
            "checkpoint1_eda_techstore.md",
            "10_capitulo6_cloud_computing.md", "11_capitulo7_gcp_configuracion.md",
            "12_capitulo8_bigquery_intro.md", "13_capitulo9_bigquery_avanzado.md",
            "14_capitulo10_python_bigquery.md", "15_checkpoint2_migrar_techstore.md",
            "16_capitulo11_bigquery_sql_analitico.md", "17_capitulo12_data_pipelines.md",
            "18_capitulo13_looker_studio_intro.md", "19_capitulo14_looker_avanzado.md",
            "20_checkpoint3_dashboard_cloud.md",
            "21_capitulo15_cloud_functions.md", "22_capitulo16_schedule_queries.md",
            "23_capitulo17_proyecto_final.md", "24_checkpoint4_pipeline_automatizado.md",
            "25_conclusion.md", "26_apendice_a_soluciones.md",
            "27_apendice_b_cheatsheets.md", "28_apendice_c_gcp_costes.md",
            "29_sobre_el_autor.md",
        ],
    },
    {
        "folder": "business_intelligence_bi",
        "category": "Datos_IA",
        "pdf_filename": "Business_Intelligence_BI.pdf",
        "title": "Business Intelligence y Modelado de Datos",
        "subtitle": "Dise\u00f1a dashboards profesionales y modela datos como un experto",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_intro_bi.md",
            "06_capitulo2_arquitectura_datos.md", "07_capitulo3_modelado_dimensional.md",
            "08_capitulo4_kpis_metricas.md", "09_checkpoint1_modelo_dimensional.md",
            "10_capitulo5_powerbi_primeros_pasos.md", "11_capitulo6_powerbi_modelado.md",
            "12_capitulo7_powerbi_visualizaciones.md", "13_capitulo8_dax_basico.md",
            "14_checkpoint2_dashboard_powerbi.md", "15_capitulo9_dax_avanzado.md",
            "16_capitulo10_power_query_etl.md", "17_capitulo11_data_warehousing.md",
            "18_capitulo12_medidas_avanzadas.md", "19_checkpoint3_modelo_semantico.md",
            "20_capitulo13_powerbi_service.md", "21_capitulo14_seguridad_rls.md",
            "22_capitulo15_proyecto_final.md", "23_checkpoint4_portal_bi.md",
            "24_conclusion.md", "25_apendice_a_soluciones.md",
            "26_apendice_b_cheatsheets.md", "27_apendice_c_costes_powerbi.md",
            "28_sobre_el_autor.md",
        ],
    },
    {
        "folder": "ingenieria_datos_moderna",
        "category": "Datos_IA",
        "pdf_filename": "Ingenieria_Datos_Moderna.pdf",
        "title": "Ingenier\u00eda de Datos Moderna",
        "subtitle": "Domina el data engineering moderno con Python, Airflow y dbt",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_intro_data_engineering.md",
            "06_capitulo2_python_data_engineering.md", "07_capitulo3_formatos_datos.md",
            "08_capitulo4_data_lakes_minio.md", "09_checkpoint1_data_lake_techstore.md",
            "10_capitulo5_intro_dbt.md", "11_capitulo6_modelado_dbt.md",
            "12_capitulo7_testing_documentacion_dbt.md", "13_capitulo8_dbt_avanzado.md",
            "14_checkpoint2_pipeline_dbt.md", "15_capitulo9_intro_airflow.md",
            "16_capitulo10_airflow_avanzado.md", "17_capitulo11_airflow_dbt.md",
            "18_capitulo12_monitoreo_alertas.md", "19_checkpoint3_orquestacion_completa.md",
            "20_capitulo13_docker_data.md", "21_capitulo14_cicd_datos.md",
            "22_capitulo15_proyecto_final.md", "23_checkpoint4_data_platform.md",
            "24_conclusion.md", "25_apendice_a_soluciones.md",
            "26_apendice_b_cheatsheets.md", "27_apendice_c_instalacion.md",
            "28_sobre_el_autor.md",
        ],
    },
    {
        "folder": "big_data_ml_ia",
        "category": "Datos_IA",
        "pdf_filename": "Big_Data_ML_IA.pdf",
        "title": "Big Data, ML e IA",
        "subtitle": "Domina el big data, machine learning e inteligencia artificial con proyectos pr\u00e1cticos",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_intro_big_data.md",
            "06_capitulo2_pyspark_fundamentos.md", "07_capitulo3_procesamiento_datos.md",
            "08_capitulo4_streaming_datos.md", "09_checkpoint1_pipeline_big_data.md",
            "10_capitulo5_intro_ml.md", "11_capitulo6_aprendizaje_supervisado.md",
            "12_capitulo7_aprendizaje_no_supervisado.md", "13_capitulo8_evaluacion_modelos.md",
            "14_checkpoint2_modelo_techstore.md", "15_capitulo9_deep_learning.md",
            "16_capitulo10_nlp_texto.md", "17_capitulo11_series_temporales.md",
            "18_capitulo12_mlops_mlflow.md", "19_checkpoint3_pipeline_ml.md",
            "20_capitulo13_llms_ia_generativa.md", "21_capitulo14_ml_cloud.md",
            "22_capitulo15_proyecto_final.md", "23_checkpoint4_plataforma_ia.md",
            "24_conclusion.md", "25_apendice_a_soluciones.md",
            "26_apendice_b_cheatsheets.md", "27_apendice_c_instalacion.md",
            "28_sobre_el_autor.md",
        ],
    },
    {
        "folder": "freelancer_datos",
        "category": "Datos_IA",
        "pdf_filename": "Freelancer_Datos.pdf",
        "title": "Freelancer de Datos",
        "subtitle": "Gu\u00eda para convertirte en un analista freelance exitoso",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_mercado_freelance.md",
            "06_capitulo2_habilidades_pricing.md", "07_capitulo3_conseguir_clientes.md",
            "08_capitulo4_marca_personal.md", "09_capitulo5_stack_tecnico.md",
            "10_capitulo6_ia_asistente.md", "11_capitulo7_automatizacion.md",
            "12_capitulo8_recursos_web.md", "13_capitulo9_storytelling.md",
            "14_capitulo10_visualizaciones.md", "15_capitulo11_entregables.md",
            "16_capitulo12_presentacion.md", "17_capitulo13_pricing.md",
            "18_capitulo14_marca_personal.md", "19_capitulo15_dia_a_dia.md",
            "20_conclusion.md", "21_apendice_a_herramientas.md",
            "22_apendice_b_plantillas.md", "23_apendice_c_recursos.md",
            "24_sobre_el_autor.md",
        ],
    },
    {
        "folder": "agentes_ia_negocios",
        "category": "Datos_IA",
        "pdf_filename": "Agentes_IA_Negocios.pdf",
        "title": "Agentes de IA para Peque\u00f1as Empresas",
        "subtitle": "Gu\u00eda pr\u00e1ctica para transformar tu negocio con inteligencia artificial sin ser t\u00e9cnico",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_que_es_agente_ia.md",
            "06_capitulo2_herramientas_gratuitas.md", "07_capitulo3_donde_no_usar_ia.md",
            "08_capitulo4_atencion_cliente.md", "09_capitulo5_marketing_redes.md",
            "10_capitulo6_administracion.md", "11_capitulo7_organizacion_productividad.md",
            "12_capitulo8_primer_agente.md", "13_capitulo9_casos_estudio.md",
            "14_capitulo10_futuro.md", "15_conclusion.md",
            "16_recursos.md", "17_sobre_el_autor.md",
        ],
    },
    {
        "folder": "codigo_asesino",
        "category": "Programacion",
        "pdf_filename": "Codigo_Asesino.pdf",
        "title": "C\u00f3digo Asesino: El Enigma de Qhapaq \u00d1an",
        "subtitle": "Una Saga de Misterio, Tecnolog\u00eda y Memoria Ancestral",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_el_asesinato.md",
            "06_capitulo2_los_nudos_del_quipu.md", "07_capitulo3_la_lista_de_sospechosos.md",
            "08_capitulo4_el_diccionario_de_inti.md", "09_capitulo5_el_interrogatorio.md",
            "10_capitulo6_la_ruta_del_inca.md", "11_capitulo7_las_funciones_del_saber.md",
            "12_capitulo8_los_archivos_del_laboratorio.md", "13_capitulo9_el_circulo_del_sol.md",
            "14_capitulo10_los_modulos_del_heredero.md", "15_capitulo11_la_clase_del_misterio.md",
            "16_capitulo12_la_herencia_de_los_incas.md", "17_capitulo13_el_codigo_asesino_parte1.md",
            "18_capitulo14_el_codigo_asesino_parte2.md", "19_capitulo15_el_epilogo.md",
            "20_conclusion.md", "21_apendice_soluciones.md", "22_sobre_el_autor.md",
        ],
    },
    {
        "folder": "codigo_de_olas",
        "category": "Programacion",
        "pdf_filename": "Codigo_De_Olas.pdf",
        "title": "C\u00f3digo de Olas: El Misterio del Puerto de Anc\u00f3n",
        "subtitle": "Una Historia de Surf, Tecnolog\u00eda y el Secreto del Mar",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_el_secreto_de_la_playa.md",
            "06_capitulo2_el_lenguaje_del_mar.md", "07_capitulo3_la_lista_de_implicados.md",
            "08_capitulo4_el_diccionario_del_pescador.md", "09_capitulo5_la_decision_de_la_ola.md",
            "10_capitulo6_el_viaje_de_mateo.md", "11_capitulo7_las_funciones_del_mar.md",
            "12_capitulo8_los_archivos_del_puerto.md", "13_capitulo9_el_error_en_la_red.md",
            "14_capitulo10_los_modulos_del_puerto.md", "15_capitulo11_la_clase_del_surfista.md",
            "16_capitulo12_la_herencia_del_mar.md", "17_capitulo13_el_proyecto_integrador.md",
            "18_capitulo14_revelacion_en_el_muelle.md", "19_capitulo15_epilogo_ola_libre.md",
            "20_conclusion.md", "21_apendice_soluciones.md", "22_sobre_el_autor.md",
        ],
    },
    {
        "folder": "estadistica_mortal",
        "category": "Programacion",
        "pdf_filename": "Estadistica_Mortal.pdf",
        "title": "Estad\u00edstica Mortal: El Enigma del Conjunto Vac\u00edo",
        "subtitle": "Una Novela de Misterio, Datos y Probabilidades",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_el_conjunto_vacio.md",
            "06_capitulo2_la_probabilidad_del_crimen.md", "07_capitulo3_el_teorema_del_sospechoso.md",
            "08_capitulo4_la_distribucion_del_engano.md", "09_capitulo5_la_muestra_que_miente.md",
            "10_capitulo6_la_hipotesis_asesina.md", "11_capitulo7_la_correlacion_del_secreto.md",
            "12_capitulo8_la_regresion_del_pasado.md", "13_capitulo9_el_intervalo_de_confianza.md",
            "14_capitulo10_la_varianza_del_silencio.md", "15_capitulo11_la_prueba_del_chi_cuadrado.md",
            "16_capitulo12_la_serie_del_tiempo_perdido.md", "17_capitulo13_el_ultimo_conjunto_parte1.md",
            "18_capitulo14_el_ultimo_conjunto_parte2.md", "19_capitulo15_el_epilogo.md",
            "20_conclusion.md", "21_apendice_soluciones.md", "22_sobre_el_autor.md",
        ],
    },
    {
        "folder": "sql_letal",
        "category": "Programacion",
        "pdf_filename": "SQL_Letal_Misterio_Base_Datos.pdf",
        "title": "SQL Letal: El Misterio de la Base de Datos",
        "subtitle": "Una Novela de Misterio, Datos y Consultas",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_cap1_select.md",
            "06_cap2_where.md", "07_cap3_joins.md",
            "08_cap4_groupby.md", "09_cap5_fechas.md",
            "10_cap6_subconsultas.md", "11_cap7_indices.md",
            "12_cap8_vistas.md", "13_cap9_transacciones.md",
            "14_cap10_funciones.md", "15_cap11_triggers.md",
            "16_cap12_normalizacion.md", "17_cap13_ctes.md",
            "18_cap14_window.md", "19_cap15_epilogo.md",
            "20_conclusion.md", "21_apendice_soluciones.md", "22_sobre_el_autor.md",
        ],
    },
    {
        "folder": "motor_cuantitativo",
        "category": "Matematicas",
        "pdf_filename": "El_Motor_Cuantitativo.pdf",
        "title": "El Motor Cuantitativo",
        "subtitle": "Fundamentos Matem\u00e1ticos y Estad\u00edsticos con Python para el An\u00e1lisis de Datos",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_modulo1_1_ecosistema.md",
            "06_modulo1_2_algebra_lineal.md", "07_modulo1_3_calculo_diferencial.md",
            "08_modulo2_1_medidas_descriptivas.md", "09_modulo2_2_probabilidad.md",
            "10_modulo2_3_distribuciones.md", "11_modulo2_4_tlc.md",
            "12_modulo3_1_poblacion_muestra.md", "13_modulo3_2_intervalos_confianza.md",
            "14_modulo3_3_pruebas_hipotesis.md", "15_modulo3_4_tests_python.md",
            "16_modulo4_1_fundamentos_experimentales.md", "17_modulo4_2_ab_testing_python.md",
            "18_modulo4_3_errores_comunes.md", "19_modulo5_1_correlacion_causalidad.md",
            "20_modulo5_2_regresion_lineal.md", "21_modulo5_3_evaluacion_modelos.md",
            "22_modulo5_4_regresion_logistica.md", "23_modulo6_1_pca.md",
            "24_modulo6_2_kmeans.md", "25_modulo6_3_series_temporales.md",
            "26_modulo7_1_flujo_trabajo.md", "27_modulo7_2_datos_faltantes.md",
            "28_modulo7_3_comunicacion.md", "29_conclusion.md",
            "30_apendice_a.md", "31_apendice_b.md",
            "32_referencias.md", "33_sobre_autor.md",
        ],
    },
    {
        "folder": "print_Sigo_Aqui",
        "category": "Crecimiento_Personal",
        "pdf_filename": "print_Sigo_Aqui.pdf",
        "title": "print(\"Sigo Aqu\u00ed\")",
        "subtitle": "El viaje de un inform\u00e1tico sin papeles",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_prologo.md", "01_capitulo1_llegada_madrid.md",
            "02_capitulo2_naranjas_amargas.md", "03_capitulo3_polvo_y_cemento.md",
            "04_capitulo4_fibra_en_el_norte.md", "05_capitulo5_si_reclamas_me_consigo_a_otro.md",
            "06_capitulo6_codigo_en_la_madrugada.md", "07_capitulo7_la_entrevista.md",
            "08_capitulo8_los_papeles.md", "09_capitulo9_data_analyst.md",
            "10_epilogo.md", "11_apendice_recursos.md", "12_sobre_el_autor.md",
        ],
    },
    {
        "folder": "raices_nuevas",
        "category": "Crecimiento_Personal",
        "pdf_filename": "Raices_Nuevas.pdf",
        "title": "Ra\u00edces Nuevas",
        "subtitle": "Gu\u00eda Pr\u00e1ctica para Combatir la Ansiedad del Inmigrante",
        "author": "Alex Goyzueta Delgado",
        "chapter_map": [
            "00_portada.md", "01_creditos.md", "02_dedicatoria.md", "03_prefacio.md",
            "04_introduccion.md", "05_capitulo1_lo_que_nadie_te_dice.md",
            "06_capitulo2_la_ansiedad.md", "07_capitulo3_el_duelo_migratorio.md",
            "08_capitulo4_respirar_y_ancorarte.md", "09_capitulo5_el_poder_de_las_rutinas.md",
            "10_capitulo6_conectar_sin_forzar.md", "11_capitulo7_el_idioma.md",
            "12_capitulo8_mover_el_cuerpo.md", "13_capitulo9_limites_sanos.md",
            "14_capitulo10_cuando_buscar_ayuda.md", "15_capitulo11_tu_identidad.md",
            "16_capitulo12_celebrar_lo_pequeno.md", "17_conclusion.md",
            "18_apendice_recursos.md", "19_sobre_el_autor.md",
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
    _first_h1_skipped = False

    book_dir = os.path.join(BASE, "libros", book_config.get("category", ""), book_config["folder"])
    for filename in book_config["chapter_map"]:
        # Skip portada (already rendered as title page)
        if filename == "00_portada.md":
            continue
        filepath = os.path.join(book_dir, filename)
        if not os.path.exists(filepath):
            print(f"  [FALTA] {filename}")
            continue
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if not _first_h1_skipped:
            content = re.sub(r'^# .+(\n|$)', '', content, count=1)
            _first_h1_skipped = True
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

