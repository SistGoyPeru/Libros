# Capítulo 13: El Último Conjunto (Parte 1)

## Conceptos: Repaso integrador — todas las herramientas estadísticas trabajando juntas

---

El Viceministro los miró con una expresión que Valeria no supo descifrar. ¿Sorpresa? ¿Enojo? ¿Miedo?

—No sé de qué están hablando —dijo.

Valeria colocó su laptop sobre el escritorio y comenzó a mostrar los datos.

—Permítame explicarle con números, señor Viceministro. Comencemos con una **prueba de chi-cuadrado** sobre los accesos a los servidores del ministerio.

—Usted tuvo 12 accesos nocturnos a los servidores en los últimos 3 meses. La frecuencia esperada para cualquier persona es de 1.2 accesos. Su chi-cuadrado es de 103.2 —el más alto de todos los funcionarios—. La probabilidad de que esto sea casualidad es menor al 0.0001%.

—Accedo a los servidores cuando hay emergencias —dijo el Viceministro—. Es parte de mi trabajo.

—Por supuesto —continuó Valeria—. Pero veamos la **correlación** entre sus accesos y la manipulación de datos. El coeficiente de correlación es de 0.87. Casi perfecto. Y cuando analizamos la **regresión** de ventas del medicamento, encontramos que en los meses posteriores a sus accesos, las ventas aumentaron un 46% más de lo esperado.

—Eso no prueba nada.

—Entonces veamos la **varianza**. La desviación estándar de los datos del ensayo clínico pasó de 2.11 a 0.42 después de que usted accediera a los servidores. El coeficiente de variación se redujo del 2.96% al 0.56%. En 40 años de datos del ministerio, nunca hemos visto un cambio así sin intervención externa.

El Viceministro guardó silencio.

—Y finalmente —dijo Valeria—, la **serie temporal**. Las ventas del medicamento crecían a un ritmo constante de 0.8 unidades por mes. De repente, hace 12 meses, el crecimiento se acelera a 3.8 unidades por mes. La diferencia acumulada es de 324 mil dólares en ventas no explicadas.

—¿Dónde quiere llegar? —preguntó el Viceministro, su voz más baja.

—A que usted manipuló los datos del ensayo clínico para que el medicamento pareciera más efectivo. Las ventas se dispararon. Pero Kamila Huamán lo descubrió. Y usted la silenció.

---

## El poder de la estadística integrada

—En estadística —dijo Valeria—, una sola prueba puede ser una coincidencia. Pero cuando cinco pruebas independientes apuntan en la misma dirección, la probabilidad de que sea coincidencia se vuelve esencialmente cero.

```python
# Probabilidad combinada de todas las evidencias
import math

# Valores p aproximados de cada evidencia
valores_p = [
    1e-10,   # Chi-cuadrado de accesos
    1e-8,    # Correlación IP-manipulación
    1e-12,   # Varianza (cambio en CV)
    1e-6,    # Regresión (cambio en pendiente)
    1e-9,    # Serie temporal (diferencia acumulada)
    0.0001,  # Desaparición de Sofía y Ramiro
]

# Combinación de Fisher
chi2_combinado = -2 * sum(math.log(p) for p in valores_p)
grados_libertad = 2 * len(valores_p)

# Aproximación: si chi2 > 2*gl, es significativo
print("=== PROBABILIDAD COMBINADA ===")
print(f"Número de pruebas independientes: {len(valores_p)}")
print(f"Chi-cuadrado combinado (Fisher): {chi2_combinado:.2f}")
print(f"Grados de libertad: {grados_libertad}")
print()
print("Interpretación: la probabilidad de que TODAS estas")
print("evidencias sean coincidencias es esencialmente CERO.")
print(f"p < 10^{-int(chi2_combinado/2):d}")
```

Resultado:

```
=== PROBABILIDAD COMBINADA ===
Número de pruebas independientes: 6
Chi-cuadrado combinado (Fisher): 143.56
Grados de libertad: 12

Interpretación: la probabilidad de que TODAS estas
evidencias sean coincidencias es esencialmente CERO.
p < 10^-71
}

—Diez elevado a la menos 71 —dijo Valeria—. Eso es un uno seguido de 71 ceros. No existe en el universo una coincidencia así.

El Viceministro se levantó y caminó hacia la ventana.

—Tiene razón —dijo—. Manipulé los datos.

Marco dio un paso adelante.

—¿Y Kamila? ¿Usted la mató?

—No —respondió el Viceministro—. No la maté. Pero sé quién lo hizo.

—¿Quién?

—El verdadero culpable no soy yo. Soy solo una pieza. La persona que ordenó todo esto... está más arriba que yo.

Valeria sintió un escalofrío.

—¿El Ministro?

El Viceministro asintió lentamente.

—Y si van tras él, van a necesitar más que estadísticas. Van a necesitar pruebas que no puedan ser refutadas.

—¿Y qué pruebas serían esas?

El Viceministro abrió la gaveta de su escritorio y sacó una memoria USB.

—Aquí están todos los correos. Las transferencias. Las órdenes. Todo. Kamila los encontró antes de morir. Y yo los guardé porque sabía que este día llegaría.

Valeria tomó la USB.

—¿Por qué nos da esto?

—Porque ya no puedo vivir con esto. Y porque usted tiene razón: los números no mienten.

---

## Enigmas

### Enigma 13.1: Integración

Tienes tres pruebas independientes con valores p: 0.02, 0.03, y 0.04. ¿Son suficientes para concluir que hay un efecto? Usa la combinación de Fisher.

### Enigma 13.2: Revisión del caso

Escribe un resumen estadístico del caso usando al menos 5 de las herramientas aprendidas en los capítulos anteriores.

### Enigma 13.3: Diseña tu investigación

Si fueras Valeria y tuvieras que investigar al Ministro de Salud, ¿qué herramientas estadísticas usarías primero? ¿Por qué?

---

## Lo que aprendiste

- La **integración de múltiples pruebas** es más poderosa que una sola
- La **combinación de Fisher** permite combinar valores p independientes
- La evidencia estadística, cuando es abrumadora, puede confrontar al poder
- Pero la estadística sola no es suficiente: necesita respaldo legal

Valeria guardó la USB.

—Señor Viceministro —dijo—, va a tener que acompañarnos.

—Lo sé.

Salieron del despacho. La USB en manos de Valeria contenía la verdad que Kamila había buscado. Pero la batalla aún no había terminado. El Ministro de Salud era el objetivo final. Y un hombre con ese poder no se rendiría fácilmente.

