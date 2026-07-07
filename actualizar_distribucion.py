import os, shutil, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(BASE, 'distribucion')

BOOKS = [
    ('codigo_asesino',     'Codigo_Asesino',              'Codigo_Asesino.epub',                 'Codigo_Asesino.pdf',                 'cover.jpg', 'Programacion'),
    ('codigo_de_olas',     'Codigo_De_Olas',              'Codigo_De_Olas.epub',                 'Codigo_De_Olas.pdf',                 'cover.jpg', 'Programacion'),
    ('estadistica_mortal', 'Estadistica_Mortal',          'Estadistica_Mortal.epub',             'Estadistica_Mortal.pdf',             'cover.jpg', 'Programacion'),
    ('motor_cuantitativo', 'El_Motor_Cuantitativo',       'El_Motor_Cuantitativo.epub',          'El_Motor_Cuantitativo.pdf',          'cover.jpg', 'Matematicas'),
    ('raices_nuevas',      'Raices_Nuevas',               'Raices_Nuevas.epub',                  'Raices_Nuevas.pdf',                  'cover.jpg', 'Crecimiento_Personal'),
    ('print_Sigo_Aqui',    'print_Sigo_Aqui',             'print_Sigo_Aqui.epub',               'print_Sigo_Aqui.pdf',               'cover_pretty.jpg', 'Crecimiento_Personal'),
    ('sql_letal',          'SQL_Letal',                   'SQL_Letal_Misterio_Base_Datos.epub',  'SQL_Letal_Misterio_Base_Datos.pdf',  'cover.jpg', 'Programacion'),
    ('excel_basico',       'Excel_Basico',                'Excel_Basico.epub',                   'Excel_Basico.pdf',                   'cover.jpg', 'Excel'),
    ('excel_intermedio',   'Excel_Intermedio',            'Excel_Intermedio.epub',               'Excel_Intermedio.pdf',               'cover.jpg', 'Excel'),
    ('excel_avanzado',     'Excel_Avanzado',              'Excel_Avanzado.epub',                 'Excel_Avanzado.pdf',                 'cover.jpg', 'Excel'),
    ('excel_contadores',   'Excel_Para_Contadores',       'Excel_Para_Contadores.epub',          'Excel_Para_Contadores.pdf',           'cover.jpg', 'Excel'),
    ('excel_analisis_datos', 'Excel_Analisis_Datos',      'Excel_Analisis_Datos.epub',           'Excel_Analisis_Datos.pdf',            'cover.jpg', 'Excel'),
    ('excel_copilot',        'Excel_con_Copilot',         'Excel_con_Copilot.epub',              'Excel_con_Copilot.pdf',               'cover.jpg', 'Excel'),
    ('html_basico',          'HTML_Basico',               'HTML_Basico.epub',                    'HTML_Basico.pdf',                     'cover.jpg', 'Web'),
    ('css_basico',           'CSS_Basico',                'CSS_Basico.epub',                     'CSS_Basico.pdf',                      'cover.jpg', 'Web'),
    ('js_basico',            'JS_Basico',                 'JS_Basico.epub',                      'JS_Basico.pdf',                       'cover.jpg', 'Web'),
    ('fundamentos_analista_datos', 'Fundamentos_Analista_Datos', 'Fundamentos_Analista_Datos.epub',      'Fundamentos_Analista_Datos.pdf',       'cover.jpg', 'Datos_IA'),
    ('python_data_cloud',        'Python_Data_Cloud',          'Python_Data_Cloud.epub',              'Python_Data_Cloud.pdf',                'cover.jpg', 'Datos_IA'),
    ('business_intelligence_bi',  'Business_Intelligence_BI',  'Business_Intelligence_BI.epub',       'Business_Intelligence_BI.pdf',         'cover.jpg', 'Datos_IA'),
    ('ingenieria_datos_moderna',  'Ingenieria_Datos_Moderna', 'Ingenieria_Datos_Moderna.epub',      'Ingenieria_Datos_Moderna.pdf',         'cover.jpg', 'Datos_IA'),
    ('big_data_ml_ia',            'Big_Data_ML_IA',          'Big_Data_ML_IA.epub',                'Big_Data_ML_IA.pdf',                   'cover.jpg', 'Datos_IA'),
    ('freelancer_datos',         'Freelancer_Datos',        'Freelancer_Datos.epub',              'Freelancer_Datos.pdf',                 'cover.jpg', 'Datos_IA'),
    ('agentes_ia_negocios',      'Agentes_IA_Negocios',    'Agentes_IA_Negocios.epub',           'Agentes_IA_Negocios.pdf',              'cover.jpg', 'Datos_IA'),
]

os.makedirs(DIST, exist_ok=True)

ok, fail = 0, 0
for folder, out_name, epub_name, pdf_name, cover_name, category in BOOKS:
    src = os.path.join(BASE, "libros", category, folder)
    dst = os.path.join(DIST, folder)
    os.makedirs(dst, exist_ok=True)

    pairs = [
        (os.path.join(src, epub_name), os.path.join(dst, f'{out_name}.epub')),
        (os.path.join(src, pdf_name),  os.path.join(dst, f'{out_name}.pdf')),
        (os.path.join(src, cover_name), os.path.join(dst, 'cover.jpg')),
    ]

    for s, d in pairs:
        if s and os.path.exists(s):
            shutil.copy2(s, d)
        elif s:
            print(f'  [FALTA] {os.path.basename(s)}')

    codigos_src = os.path.join(src, 'codigos')
    codigos_dst = os.path.join(dst, 'codigos')
    if os.path.isdir(codigos_src):
        os.makedirs(codigos_dst, exist_ok=True)
        for item in os.listdir(codigos_src):
            if item == '__pycache__':
                continue
            s = os.path.join(codigos_src, item)
            d = os.path.join(codigos_dst, item)
            if os.path.isfile(s):
                shutil.copy2(s, d)
            elif os.path.isdir(s):
                if os.path.isdir(d):
                    shutil.rmtree(d, ignore_errors=True)
                shutil.copytree(s, d, dirs_exist_ok=True)

    desc_src = os.path.join(src, 'descripcion.txt')
    desc_dst = os.path.join(dst, 'descripcion.txt')
    if os.path.exists(desc_src):
        shutil.copy2(desc_src, desc_dst)

    print(f'[OK] {folder}')
    ok += 1

print(f'\nHecho. {ok} libros copiados a {DIST}')
