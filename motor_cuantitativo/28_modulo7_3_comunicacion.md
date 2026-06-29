# Cómo Comunicar Hallazgos Matemáticos a Stakeholders

El análisis cuantitativo más brillante es inútil si no puedes comunicar sus resultados a quienes toman decisiones. Este capítulo te enseña a traducir conceptos técnicos en narrativa accionable.

## El Problema de Comunicar Matemáticas

Los stakeholders no técnicos necesitan:
- **Respuestas claras**, no procesos
- **Decisiones**, no metodologías
- **Confianza** en los resultados, no fórmulas

```python
# Mal: comunicación técnica
"""
Aplicamos una regresión logística con regularización L2
y validación cruzada estratificada de 5 folds.
El AUC fue de 0.87 con un intervalo de confianza del 95%
de [0.84, 0.90]. El odds ratio de la variable X fue de 2.3.
"""

# Bien: comunicación orientada a negocio
"""
Podemos identificar al 70% de los clientes que se van a dar de baja
con un 85% de precisión. Las señales más tempranas son:
llamadas a soporte y quejas recientes. Con esta info, podemos
ofrecer descuentos proactivos a los clientes en riesgo.
"""
```

## La Pirámide de la Comunicación Cuantitativa

```
        ╱  Decisión  ╲          ← ¿Qué hacemos?
       ╱  Recomendación ╲       ← ¿Qué sugiero?
      ╱    Conclusiones    ╲    ← ¿Qué significa?
     ╱      Hallazgos        ╲  ← ¿Qué encontré?
    ╱        Datos             ╲ ← ¿Qué tengo?
```

## Traduciendo Conceptos Técnicos

| Término técnico | Traducción para negocio |
|-----------------|------------------------|
| "Valor p < 0.05" | "Hay evidencia suficiente para afirmar que el cambio funciona" |
| "Intervalo de confianza del 95%" | "El verdadero efecto está entre X e Y, con alta confianza" |
| "AUC = 0.85" | "El modelo acierta 8 de cada 10 veces" |
| "R² = 0.72" | "El 72% del comportamiento se explica por estos factores" |
| "Error estándar" | "El margen de error de nuestra estimación" |
| "Correlación no implica causalidad" | "Aunque X e Y se mueven juntos, necesitamos un experimento para probar que X causa Y" |
| "Sobreajuste" | "El modelo memorizó los datos de prueba, no aprendió patrones generales" |

## El Principio de la Audiencia

```python
def adaptar_mensaje(audiencia, resultados):
    """Adapta el mensaje según la audiencia"""
    mensajes = {}

    if audiencia == 'directivo':
        mensajes = {
            'titulo': 'Impacto en el negocio',
            'metricas': ['ROI', 'clientes retenidos', 'ingresos adicionales'],
            'detalle_tecnico': 'bajo',
            'accion': 'invertir recursos',
        }
    elif audiencia == 'analista':
        mensajes = {
            'titulo': 'Metodología y resultados',
            'metricas': ['AUC', 'precisión', 'recall', 'valor p'],
            'detalle_tecnico': 'alto',
            'accion': 'validar supuestos y reproducir',
        }
    elif audiencia == 'cliente':
        mensajes = {
            'titulo': 'Beneficios para ti',
            'metricas': ['tiempo ahorrado', 'dinero ahorrado', 'mejora'],
            'detalle_tecnico': 'nulo',
            'accion': 'adoptar el cambio',
        }

    return mensajes
```

## Visualización Efectiva

```python
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Mala visualización: gráfico 3D innecesario, colores confusos
# (no ejecutar, es ilustrativo)

# Buena visualización: simple, clara, directa
def grafico_comparacion_simple(control, tratamiento, metrica='Tasa de conversión'):
    """Gráfico simple y profesional para comparar A/B"""
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    # Barras con IC
    medias = [np.mean(control), np.mean(tratamiento)]
    errores = [np.std(control, ddof=1)/np.sqrt(len(control)),
               np.std(tratamiento, ddof=1)/np.sqrt(len(tratamiento))]

    ax[0].bar(['Control', 'Tratamiento'], medias, yerr=errores,
              capsize=10, color=['#6b9bc5', '#e8834a'])
    ax[0].set_ylabel(metrica)
    ax[0].set_title('Comparación de grupos')
    ax[0].grid(axis='y', alpha=0.3)

    # Diferencia
    diff = media_trat - media_control
    ax[1].bar(['Diferencia'], [diff],
              yerr=[np.sqrt(errores[0]**2 + errores[1]**2)],
              capsize=10, color='#4c72b0')
    ax[1].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax[1].set_ylabel(f'Diferencia en {metrica}')
    ax[1].set_title('Efecto del tratamiento')

    return fig
```

### Reglas de Visualización para Stakeholders

1. **Un gráfico, un mensaje.** No abarrotes
2. **Etiquetas claras.** No asumas que saben leer el eje Y
3. **Colores con propósito.** Azul/verde para positivo, rojo para negativo
4. **Evita 3D.** Distorsiona las proporciones
5. **Incluye intervalos de confianza.** Muestra la incertidumbre
6. **Primero la conclusión.** El título debe ser el hallazgo, no la descripción

```python
# Ejemplo de mal título: "Gráfico de barras de ingresos por mes"
# Ejemplo de buen título: "Los ingresos aumentaron un 15% después del rediseño"
```

## Storytelling con Datos

### La Estructura Narrativa

```
1. CONTEXTO: Situación actual
   "Nuestra tasa de retención ha caído al 75% en los últimos 6 meses."

2. CONFLICTO: El problema
   "No sabíamos qué clientes se irían ni por qué."

3. ANÁLISIS: Lo que hicimos
   "Analizamos el comportamiento de 10,000 clientes y encontramos 3 señales tempranas."

4. HALLAZGO: Lo que descubrimos
   "Los clientes que llaman a soporte 3+ veces tienen un 80% de probabilidad de irse."

5. ACCIÓN: Lo que proponemos
   "Si llamamos a esos clientes con una oferta personalizada, podemos retener al 60%."
```

### Template de Presentación Ejecutiva

```markdown
# Proyecto: [Nombre del proyecto]

## Resumen (30 segundos)
[Una frase con el hallazgo principal y la acción recomendada]

## El Problema
[Contexto: qué motivó el análisis]

## Lo que Hicimos
[Muy breve: qué datos, qué método]

## Lo que Encontramos
[El hallazgo principal, con 1-2 visualizaciones simples]

## Lo que Recomendamos
[Acciones concretas, con impacto esperado]

## Apéndice Técnico
[Detalles para quienes los quieran — al final, no interrumpen la historia]
```

## Checklist de Comunicación

| Aspecto | Bueno | Malo |
|---------|-------|------|
| Longitud | 3 diapositivas clave | 50 diapositivas |
| Jerga | "Mejora del 20%" | "El odds ratio ajustado es 1.23" |
| Visualización | Una barra con IC | Mapa de calor 3D |
| Certeza | "La evidencia sugiere" | "Esto prueba que" |
| Acción | "Recomiendo invertir $X" | "El valor p fue significativo" |
| Estructura | Problema → Hallazgo → Acción | Aquí están todos los datos |

## 🎯 Ejercicios Prácticos

1. **Ejercicio 1:** Toma un análisis que hayas hecho (o simula uno) y escribe dos versiones del resumen: una para el equipo técnico y otra para el director de la empresa.

2. **Ejercicio 2:** Encuentra un gráfico en una noticia o artículo que sea engañoso o confuso. Rediseñalo para que sea más claro.

3. **Ejercicio 3:** Prepara una presentación de 3 diapositivas (en markdown) explicando un A/B test que muestra un lift del 5% con p=0.04. La audiencia es el equipo de producto.

4. **Ejercicio 4:** Traduce los siguientes términos a lenguaje de negocio: "multicolinealidad", "heterocedasticidad", "sobreajuste", "AUC", "sesgo del estimador".

## 📝 Resumen del Capítulo

- Adapta el mensaje a la **audiencia**: directivos quieren decisiones, analistas quieren detalles
- Traduce la **jerga técnica** a lenguaje de negocio
- Las visualizaciones deben ser **simples, claras y con un solo mensaje**
- La estructura narrativa: **contexto → conflicto → análisis → hallazgo → acción**
- La **incertidumbre** se comunica (IC), no se oculta
- Sé **honesto** sobre las limitaciones del análisis
- Termina siempre con una **recomendación accionable**
- Menos es más: 3 diapositivas clave > 50 diapositivas con todo

**Conceptos clave aprendidos:** comunicación efectiva, storytelling, visualización de datos, traducción técnica, pirámide de comunicación, audiencia objetivo, resumen ejecutivo
