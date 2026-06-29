import os, shutil, sys

BASE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(BASE, 'distribucion')

BOOKS = [
    ('codigo_asesino',     'Codigo_Asesino',              'Codigo_Asesino.epub',                 'Codigo_Asesino.pdf',                 'cover.jpg'),
    ('codigo_de_olas',     'Codigo_De_Olas',              'Codigo_De_Olas.epub',                 'Codigo_De_Olas.pdf',                 'cover.jpg'),
    ('estadistica_mortal', 'Estadistica_Mortal',          'Estadistica_Mortal.epub',             'Estadistica_Mortal.pdf',             'cover.jpg'),
    ('motor_cuantitativo', 'El_Motor_Cuantitativo',       'El_Motor_Cuantitativo.epub',          'El_Motor_Cuantitativo.pdf',          'cover.jpg'),
    ('raices_nuevas',      'Raices_Nuevas',               'Raices_Nuevas.epub',                  'Raices_Nuevas.pdf',                  'cover.jpg'),
    ('print_Sigo_Aqui',    'print_Sigo_Aqui',             'print_Sigo_Aqui.epub',               'print_Sigo_Aqui.pdf',               'cover_pretty.jpg'),
    ('sql_letal',          'SQL_Letal',                   'SQL_Letal_Misterio_Base_Datos.epub',  'SQL_Letal_Misterio_Base_Datos.pdf',  'cover.jpg'),
    ('excel_basico',       'Excel_Basico',                'Excel_Basico.epub',                   'Excel_Basico.pdf',                   'cover.jpg'),
    ('excel_intermedio',   'Excel_Intermedio',            'Excel_Intermedio.epub',               'Excel_Intermedio.pdf',               'cover.jpg'),
    ('excel_avanzado',     'Excel_Avanzado',              'Excel_Avanzado.epub',                 'Excel_Avanzado.pdf',                 'cover.jpg'),
    ('excel_contadores',   'Excel_Para_Contadores',       'Excel_Para_Contadores.epub',          'Excel_Para_Contadores.pdf',           'cover.jpg'),
]

os.makedirs(DIST, exist_ok=True)

ok, fail = 0, 0
for folder, out_name, epub_name, pdf_name, cover_name in BOOKS:
    src = os.path.join(BASE, folder)
    dst = os.path.join(DIST, folder)
    os.makedirs(dst, exist_ok=True)

    pairs = [
        (os.path.join(src, epub_name), os.path.join(dst, f'{out_name}.epub')),
        (os.path.join(src, pdf_name),  os.path.join(dst, f'{out_name}.pdf')),
        (os.path.join(src, cover_name), os.path.join(dst, 'cover.jpg')),
    ]

    for s, d in pairs:
        if os.path.exists(s):
            shutil.copy2(s, d)
        else:
            print(f'  [FALTA] {os.path.basename(s)}')

    codigos_src = os.path.join(src, 'codigos')
    codigos_dst = os.path.join(dst, 'codigos')
    if os.path.isdir(codigos_src):
        if os.path.isdir(codigos_dst):
            shutil.rmtree(codigos_dst)
        shutil.copytree(codigos_src, codigos_dst)

    print(f'[OK] {folder}')
    ok += 1

print(f'\nHecho. {ok} libros copiados a {DIST}')
