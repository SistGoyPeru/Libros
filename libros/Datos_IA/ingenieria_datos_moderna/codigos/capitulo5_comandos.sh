# Capítulo 5: Comandos básicos de dbt

# Ejecutar todos los modelos
dbt run

# Ejecutar solo un modelo específico
dbt run --select stg_orders

# Ejecutar modelo y sus dependencias (aguas arriba)
dbt run --select stg_orders+

# Ejecutar modelo y sus descendientes (aguas abajo)
dbt run --select +fact_orders

# Compilar SQL sin ejecutar
dbt compile

# Generar documentación
dbt docs generate
dbt docs serve   # Abre http://localhost:8080

# Probar fuentes (comprueba que las tablas existen)
dbt source freshness
