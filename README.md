# Tienda de libros Django

Proyecto Django para una tienda virtual de libros electrónicos basada en `epub_visor`.

## Estructura del repositorio

- `.gitignore`: archivos y carpetas excluidas del control de versiones.
- `actualizar_distribucion.py`: script para construir `distribucion/` a partir de `libros/`.
- `distribucion/`: carpeta con ebooks y recursos de distribución.
- `epub_visor/`: proyecto Django, configuración y app principal.
- `libros/`: biblioteca original de ebooks y códigos fuente.
- `promociones/`: contenidos de marketing y anuncios.
- `scripts/`: utilidades para generar portadas, ejemplos y promociones.
- `venv_epub/`: entorno virtual local (no versionado gracias a `.gitignore`).

## Ejecutar el proyecto

1. Activar el entorno virtual:
   ```powershell
   .\venv_epub\Scripts\Activate.ps1
   ```
2. Ir al proyecto Django:
   ```powershell
   cd .\epub_visor
   ```
3. Ejecutar el servidor:
   ```powershell
   py -3 manage.py runserver
   ```
4. Abrir en el navegador:
   - Tienda: `http://127.0.0.1:8000/`

## Desarrollo y despliegue

- `epub_visor/requirements.txt`: dependencias Python.
- `epub_visor/README.md`: documentación específica del proyecto Django.
- `epub_visor/build.sh`: script de compilación para Render.
- `render.yaml`: configuración de despliegue en Render.

## Notas

- `distribucion/` está ignorado por Git para evitar subir archivos binarios y paquetes epub/pdf pesados.
- Usa el admin de Django para crear y editar libros, luego marca `publicado`.
- El campo `payhip_url` permite enlazar cada libro a Payhip.
