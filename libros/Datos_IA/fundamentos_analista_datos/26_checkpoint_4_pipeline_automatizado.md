# Checkpoint 4: Pipeline de Análisis Automatizado

## Integración final

Este checkpoint valida que has construido un pipeline completo y funcional que integra SQL, Python y Excel en un flujo automatizado.

## Parte 1: Verificación del pipeline

Ejecuta tu pipeline Python completo y verifica:

1. El script se ejecuta sin errores
2. Genera el archivo `reporte_final_techstore.xlsx`
3. El archivo tiene todas las hojas esperadas
4. Los datos son consistentes (comprueba totales contra SQL)

### Script de verificación

Crea `verificar_pipeline.py`:

```python
"""
verificar_pipeline.py
Verifica que el pipeline funciona correctamente
"""
import sqlite3
import pandas as pd
import os

print("=== VERIFICACIÓN DEL PIPELINE ===\n")

# 1. Verificar conexión a BD
print("1. Conexión a base de datos...")
conn = sqlite3.connect("codigos/techstore.db")
tablas = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
print(f"   Tablas encontradas: {len(tablas)}")
print(f"   Tablas: {', '.join(tablas['name'].tolist())}")

# 2. Verificar totales
print("\n2. Verificación de totales...")
total_sql = pd.read_sql("""
    SELECT COUNT(*) AS pedidos,
           ROUND(SUM(total), 2) AS ingresos,
           ROUND(AVG(total), 2) AS ticket_promedio
    FROM orders WHERE status = 'Completado'
""", conn)
print(f"   Pedidos completados: {total_sql['pedidos'][0]}")
print(f"   Ingresos totales: {total_sql['ingresos'][0]:,.2f}€")
print(f"   Ticket promedio: {total_sql['ticket_promedio'][0]:,.2f}€")

conn.close()

# 3. Verificar que existe el reporte
print("\n3. Verificación de reporte...")
reporte = "reporte_final_techstore.xlsx"
if os.path.exists(reporte):
    tamaño = os.path.getsize(reporte) // 1024
    print(f"   Reporte encontrado: {reporte} ({tamaño} KB)")
    
    # Verificar hojas
    xl = pd.ExcelFile(reporte)
    print(f"   Hojas: {xl.sheet_names}")
else:
    print(f"   [FALTA] No se encontró {reporte}")

# 4. Verificar cobertura de herramientas
print("\n4. Cobertura de aprendizaje:")
print("   SQL:    ✓ Consultas, JOINs, agregaciones, window functions")
print("   Excel:  ✓ Tablas dinámicas, Power Query, gráficos, Power Pivot")
print("   Python: ✓ variables, listas, dicts, funciones, pandas")
print("   Integración: ✓ SQL + Python + Excel pipeline")

print("\n=== VERIFICACIÓN COMPLETADA ===")
```

## Parte 2: Validación cruzada

Verifica que los números coinciden entre herramientas:

```sql
-- SQL: Total de ventas completadas
SELECT ROUND(SUM(total), 2) FROM orders WHERE status = 'Completado';
```

```python
# Python: mismo cálculo con pandas
df = pd.read_sql("SELECT total FROM orders WHERE status = 'Completado'", conn)
print(df["total"].sum())
```

```excel
# Excel: Tabla dinámica filtrando status = Completado
# Valor: Suma de total
# ¿Coincide con SQL y Python?
```

Los tres deben dar exactamente el mismo número.

## Parte 3: Portfolio completo

Al finalizar este libro, tienes un portfolio con 4 proyectos:

| Proyecto | Herramientas | Qué hiciste |
|----------|-------------|-------------|
| 1. Análisis de Ventas Básicas | SQL + Excel + Python | Primeros pasos, métricas básicas |
| 2. Top 10 Productos | SQL + Excel + Python | JOINs, tablas dinámicas, visualización |
| 3. Análisis de Cohorte | SQL + Excel + Python | CTEs, Power Query, Python avanzado |
| 4. Pipeline Automatizado | SQL + Python + Excel | Integración total, dashboard |

Cada proyecto incluye:
- Consultas SQL
- Archivo Excel con análisis
- Script Python
- Dashboard o visualización

## Parte 4: Checklist final del libro

- [ ] Ejecuté el pipeline final sin errores
- [ ] Verifiqué que los totales coinciden en las 3 herramientas
- [ ] Mi dashboard responde las preguntas de negocio
- [ ] Tengo los 4 proyectos guardados en carpetas separadas
- [ ] Puedo explicar cada proyecto a un entrevistador
- [ ] Entiendo el flujo completo: SQL → Python → Excel
- [ ] Estoy listo para el siguiente libro de la colección
