# Apéndice C: Instalación y Configuración

## 1. DB Browser for SQLite

Descarga: https://sqlitebrowser.org/dl/

### Instalación
1. Descarga el instalador para Windows (portable o installer)
2. Ejecuta el instalador
3. Sigue los pasos del asistente
4. Abre DB Browser y selecciona "Open Database"
5. Navega a `codigos/techstore.db`

### Verificación
- Ejecuta `SELECT COUNT(*) FROM products;` → debe devolver 509

## 2. Python 3.12+

Descarga: https://www.python.org/downloads/

### Instalación
1. Descarga Python 3.12 o superior
2. **IMPORTANTE**: marca "Add Python to PATH"
3. Haz clic en "Install Now"
4. Espera a que termine la instalación

### Verificación
Abre una terminal (cmd) y escribe:
```bash
python --version
pip --version
```

### Instalar paquetes
```bash
pip install pandas openpyxl
```

## 3. Visual Studio Code

Descarga: https://code.visualstudio.com/

### Instalación
1. Descarga el instalador
2. Ejecuta y sigue los pasos
3. Abre VS Code

### Extensiones recomendadas
- **Python** (Microsoft) — Soporte para Python
- **SQLite Viewer** — Ver bases de datos SQLite
- **Excel Viewer** — Vista previa de CSV
- **Spanish Language Pack** — Interfaz en español (opcional)
- **Markdown Preview** — Vista previa de markdown

### Configurar VS Code para Python
1. Abre VS Code
2. Ctrl+Shift+P > "Python: Select Interpreter"
3. Selecciona la versión de Python instalada
4. Crea un archivo `.py` y escribe `print("Hola")`
5. Haz clic en "Run" (triángulo en esquina superior derecha)

## 4. Microsoft Excel

### Si no tienes Excel
Opciones gratuitas compatibles:
- **LibreOffice Calc**: https://www.libreoffice.org/
- **Google Sheets**: sheets.google.com (gratuito con cuenta Google)
- **OnlyOffice**: https://www.onlyoffice.com/

### Power Pivot (solo Excel)
1. Archivo > Opciones > Complementos
2. En "Administrar", selecciona "Complementos COM"
3. Marca "Microsoft Power Pivot for Excel"
4. Aparecerá la pestaña "Power Pivot" en la cinta

### Power Query (Excel 2016+)
Ya viene incluido en "Datos" > "Obtener y transformar datos"

## 5. Estructura de archivos del libro

```
fundamentos_analista_datos/
├── codigos/
│   ├── techstore.db         # Base de datos SQLite
│   ├── datos_ventas.csv     # 6000 pedidos
│   ├── datos_clientes.csv   # 250 clientes
│   ├── datos_productos.csv  # 509 productos
│   ├── datos_detalles_ventas.csv  # 21118 líneas
│   ├── ejemplo_1.sql        # SQL de ejemplo
│   ├── ejemplo_2.sql
│   ├── ejemplo_3.sql
│   └── generar_db_techstore.py   # Script para regenerar la BD
├── *.md                     # Capítulos del libro
├── metadata.yaml            # Metadatos del libro
├── cover.jpg                # Portada
├── descripcion.txt          # Descripción
└── toc.md                   # Tabla de contenidos
```

## 6. Solución de problemas comunes

### Python no se reconoce como comando
- Solución: reinstala Python marcando "Add Python to PATH"
- O: usa la ruta completa: `C:\Users\tu_usuario\AppData\Local\Programs\Python\Python312\python.exe`

### pandas no encontrado
- Abre terminal y ejecuta: `pip install pandas`

### SQLite no abre la base de datos
- Verifica que `techstore.db` existe en la carpeta correcta
- Si no existe, ejecuta: `python codigos/generar_db_techstore.py`

### Excel no abre CSV correctamente
- Usa "Datos" > "Desde archivo" > "Desde CSV" en lugar de doble clic
- Selecciona el separador correcto (coma) y codificación UTF-8

### Power Query no aparece
- Solo disponible en Excel 2016 o superior
- Verifica que no estás en modo de compatibilidad (.xls en lugar de .xlsx)

## 7. Recursos online

- Repositorio GitHub del libro: [URL]
- Códigos y soluciones: carpeta `codigos/soluciones/`
- Comunidad Data & Analytics Mastery: [URL]
- Canal de YouTube con videotutoriales: [URL]
