# Apéndice C: Configuración de GCP y Costes

## Free Tier de Google Cloud

Google Cloud ofrece un **free tier** generoso que cubre la mayoría de lo que necesitas para este libro:

| Servicio | Free Tier | Límite mensual |
|----------|-----------|----------------|
| BigQuery | 10 GB de almacenamiento | Gratis |
| BigQuery | 1 TB de consultas procesadas | Gratis |
| Cloud Functions | 2 millones de invocaciones | Gratis |
| Cloud Functions | 400,000 GB-segundos de computación | Gratis |
| Cloud Storage | 5 GB por región | Gratis |
| Cloud Scheduler | 3 trabajos programados | Gratis |
| Looker Studio | Ilimitado | Gratis |

Además, al crear tu cuenta obtienes **$300 USD en créditos** para usar durante 90 días.

## Costes estimados del proyecto TechStore

Con los datos de TechStore (~6000 pedidos, ~500 productos, ~250 clientes):

| Concepto | Estimación mensual |
|----------|-------------------|
| Almacenamiento BigQuery | ~100 MB → < $0.01 |
| Consultas (aprendizaje) | ~2 GB/mes → < $0.01 |
| Cloud Functions (pruebas) | ~1000 invocaciones → $0.00 |
| Cloud Storage (informes) | ~10 MB → $0.00 |
| **Total estimado** | **< $0.50 USD/mes** |

## Cómo monitorear costes

### Alertas de presupuesto

1. Ve a `console.cloud.google.com/billing`
2. "Presupuestos y alertas" → "Crear presupuesto"
3. Nombre: "TechStore Analytics"
4. Monto: $5 USD/mes
5. Alertas: 50%, 90%, 100%
6. Notificaciones: Email a tu cuenta

### Recomendaciones para ahorrar costes

1. **Siempre previsualiza**: usa `LIMIT 0` para estimar coste antes de ejecutar
2. **Elimina tablas temporales**: borra datasets de prueba cuando termines
3. **Particiona y agrupa**: reduce datos escaneados hasta 90%
4. **Evita SELECT ***: selecciona solo columnas necesarias
5. **Usa la consola de facturación**: revisa semanalmente
6. **Pausa recursos no usados**: detén VMs, elimina funciones de prueba
7. **Usa committed use discounts**: si tienes carga predecible (más avanzado)

## Troubleshooting común

### Error: "Billing account not found"
- Solución: verifica que la facturación esté habilitada en `console.cloud.google.com/billing`

### Error: "Access Denied: BigQuery BigQuery"
- Solución: habilita la API de BigQuery en "APIs y servicios" → "Biblioteca"

### Error: "Dataset not found in location"
- Solución: verifica que el dataset existe y estás en la región correcta

### Error: "Exceeded rate limits"
- Solución: espera unos segundos y reintenta. Reduce la concurrencia

### Error: "401 Unauthorized" en gcloud
- Solución: ejecuta `gcloud auth login` y `gcloud auth application-default login`

### Error: Cloud Function deployment timeout
- Solución: reduce dependencias, verifica que requirements.txt esté completo

## Regiones recomendadas

| Región | Descripción | Coste |
|--------|-------------|-------|
| `us-central1` | Iowa, USA | Más barato |
| `us-east1` | Carolina del Sur, USA | Barato |
| `europe-west1` | Bélgica | Bueno para Europa |
| `southamerica-east1` | São Paulo, Brasil | Más caro |
| `asia-southeast1` | Singapur | Bueno para Asia |

Para este libro, usa `us-central1` (menor coste, buena latencia global).

## Recursos adicionales

- **Documentación BigQuery**: https://cloud.google.com/bigquery/docs
- **Pricing Calculator**: https://cloud.google.com/products/calculator
- **Google Cloud Skills Boost**: https://www.cloudskillsboost.google/
- **BigQuery public datasets**: https://cloud.google.com/bigquery/public-data
- **Looker Studio Help**: https://support.google.com/looker-studio
