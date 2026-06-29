@echo off
cd /d "%~dp0"
echo ====================================
echo   EPUB VISOR - Kindle Reader
echo ====================================
echo.
echo Abre tu navegador en: http://localhost:8000
echo Admin: http://localhost:8000/admin/
echo Usuario: alex / Clave: admin123
echo.
"%CD%\..\venv_epub\Scripts\python.exe" manage.py runserver 0.0.0.0:8000
pause
