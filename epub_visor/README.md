# Tienda de libros Django

Este proyecto es una tienda básica de libros creada con Django. Muestra libros publicados con portada, descripción, precio y enlace de Payhip.

## Estructura

- `manage.py`: script de administración de Django
- `requirements.txt`: dependencias Python
- `build.sh`: comando de compilación para Render
- `epub_visor/`: configuración del proyecto Django
- `store/`: app que contiene el modelo `Libro`, vistas y URLs
- `templates/store/home.html`: página principal de la tienda
- `static/`: archivos estáticos locales
- `staticfiles/`: archivos estáticos compilados
- `render.yaml`: configuración para desplegar en Render con base de datos PostgreSQL

## Ejecutar localmente

1. Abre PowerShell en `c:\Users\alexg\OneDrive\Alex_2026\libros epub\epub_visor`
2. Ejecuta:
   ```powershell
   py -3 manage.py runserver
   ```
3. Abre en el navegador:
   - Tienda: `http://127.0.0.1:8000/`
   - Admin: `http://127.0.0.1:8000/admin/`

## Crear superusuario

Para agregar libros desde el administrador de Django:

```powershell
py -3 manage.py createsuperuser
```

Sigue los pasos y luego inicia sesión en `/admin/`.

### Credenciales de admin de ejemplo

- Usuario: `admin`
- Email: `alexgoyzueta2018@gmail.com`
- Contraseña: `admin123`

> Usa estas credenciales solo para la copia local de desarrollo. En producción debes cambiar la contraseña por una más segura.

## Añadir libros

En el admin, crea nuevos objetos `Libro` con:

- `titulo`
- `descripcion`
- `portada_url` (URL de imagen de portada)
- `precio` (por defecto 1.00)
- `payhip_url` (enlace de compra)
- `publicado` (activa para mostrarlo en la tienda)

Si no pones todavía `payhip_url`, el botón aparecerá como "Agregar URL de Payhip".

## Despliegue en Render

Render ya tiene la configuración base en `render.yaml`:

- Usa `python` como runtime
- Construye con `build.sh`
- Arranca con `gunicorn epub_visor.wsgi:application --bind 0.0.0.0:$PORT --workers 4`
- Usa `DATABASE_URL` desde la base de datos de Render

### Variables de entorno en Render

- `DJANGO_SECRET_KEY` (generada automáticamente)
- `DJANGO_DEBUG` = `False`
- `DJANGO_ALLOWED_HOSTS` = `.onrender.com,localhost`
- `DJANGO_CSRF_TRUSTED_ORIGINS` = `https://*.onrender.com`
- `DATABASE_URL` desde la base de datos de Render

## Actualizar datos sin perder información

La app usa una base de datos administrada por Render. No borres el servicio de base de datos cuando actualices la app. Los datos de libros se mantienen mientras la base de datos siga activa.

## Cuando quieras agregar libros

Añade los libros al admin y marca `publicado`. Luego actualiza `payhip_url` cuando tengas el enlace definitivo.
