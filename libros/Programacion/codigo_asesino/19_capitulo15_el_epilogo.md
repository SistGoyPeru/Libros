# Capítulo 15: El Epílogo — La Verdad del Quipu Blanco

## Proyecto Integrador: La revelación y el cierre

---

La cita era en el mirador de San Blas, el barrio más alto de Neo-Cusco. Desde allí, se veía toda la ciudad: las cúpulas doradas de la catedral, los rascacielos de vidrio del centro financiero, y las montañas que abrazaban el valle sagrado.

Lara llegó sola. Tenía los ojos hinchados de llorar.

—Inti no era solo mi jefe —dijo, sin saludar—. Era mi mentor. Mi guía. Mi... mi segundo padre.

—¿Segundo padre? —preguntó Wayra.

—Mi padre biológico es Rodrigo Mamani. Pero nunca fue un padre para mí. Me usó. Me infiltró en el laboratorio de Inti para robar información. Pero Inti lo descubrió... y en lugar de echarme, me perdonó. Me enseñó. Me dio un propósito.

—¿Y por eso lo mataron?

—No. Yo no lo maté. Pero sé quién lo hizo.

Lara tomó un objeto de su mochila. Era un quipus, pero no como los que habían visto antes. Este era más pequeño, más íntimo, hecho de lana de alpaca blanca y roja.

—Inti me dio esto la noche antes de morir. Dijo: "Si algo me pasa, dale esto a Wayra Condori. Ella sabrá qué hacer."

Wayra tomó el quipus con manos temblorosas. En la cuerda principal, los nudos formaban un patrón que reconocía: era código binario. Pero no binario común: era binario inca, donde el nudo hacia la derecha era 1 y hacia la izquierda era 0.

—Necesito Python para decodificar esto —dijo Wayra.

## El código final

Wayra abrió su laptop y escribió el último script del caso:

```python
# ============================================
# EL ÚLTIMO CÓDIGO: DECODIFICANDO EL QUIPUS
# ============================================

# El quipus de Inti: nudos hacia derecha (1) e izquierda (0)
# Estos son los patrones de las cuerdas secundarias

quipu_final = {
    "cuerda_1": "1011",    # Derecha, Izq, Derecha, Derecha
    "cuerda_2": "0001",    # Izq, Izq, Izq, Derecha
    "cuerda_3": "1110",    # Derecha, Derecha, Derecha, Izq
    "cuerda_4": "1010",    # Derecha, Izq, Derecha, Izq
    "cuerda_5": "1101",    # Derecha, Derecha, Izq, Derecha
}

print("=== DECODIFICANDO EL QUIPUS FINAL DE INTI ===\n")

# Convertir binario a texto
for cuerda, binario in quipu_final.items():
    # Convertir binario a decimal
    decimal = int(binario, 2)
    # Convertir decimal a carácter ASCII (mayúsculas desde 65)
    letra = chr(decimal + 64)  # A=1, B=2, etc.
    
    print(f"  {cuerda}: {binario} → {decimal:2} → '{letra}'")

# El mensaje completo
mensaje = ""
for cuerda, binario in quipu_final.items():
    decimal = int(binario, 2)
    letra = chr(decimal + 64)
    mensaje += letra

print(f"\n  ► Mensaje completo: {mensaje}")

# Pero el mensaje está incompleto... necesita una clave
# La clave está en el quipu blanco original: [1,3,5,7,9,11]
clave_quipu_blanco = [1, 3, 5, 7, 9, 11]

# Aplicar la clave al mensaje
print(f"\n  ► Aplicando clave del quipu blanco...")
mensaje_descifrado = ""
for i, letra in enumerate(mensaje):
    posicion_clave = clave_quipu_blanco[i] if i < len(clave_quipu_blanco) else 0
    # Desplazar la letra según la clave
    nueva_pos = (ord(letra) - 65 + posicion_clave) % 26
    letra_descifrada = chr(nueva_pos + 65)
    mensaje_descifrado += letra_descifrada
    print(f"  {letra} + {posicion_clave} → {letra_descifrada}")

print(f"\n  ★ MENSAJE DESCIFRADO: {mensaje_descifrado} ★")
```

Wayra ejecutó el código. La terminal mostró:

```
=== DECODIFICANDO EL QUIPUS FINAL DE INTI ===

  cuerda_1: 1011 → 11 → 'K'
  cuerda_2: 0001 →  1 → 'A'
  cuerda_3: 1110 → 14 → 'N'
  cuerda_4: 1010 → 10 → 'J'
  cuerda_5: 1101 → 13 → 'M'

  ► Mensaje completo: KANJM

  ► Aplicando clave del quipu blanco...
  K + 1 → L
  A + 3 → D
  N + 5 → S
  J + 7 → Q
  M + 9 → W

  ★ MENSAJE DESCIFRADO: LDSQW ★
```

—No tiene sentido —dijo Raúl—. "LDSQW" no significa nada.

—Porque no está completo —respondió Wayra—. El quipu tiene más cuerdas. Solo estamos viendo las principales.

Revisó el quipus físico. En la parte inferior, había cuerdas más delgadas, casi invisibles. Contó los nudos.

```python
# Continuación: cuerdas secundarias del quipu
quipu_secundario = {
    "sec_1": "1001",   # -> 9 -> I
    "sec_2": "0101",   # -> 5 -> E
    "sec_3": "1000",   # -> 8 -> H
    "sec_4": "1111",   # -> 15 -> O (desplazado con clave)
    "sec_5": "0110",   # -> 6 -> F
}

print("\n=== CUERDAS SECUNDARIAS ===\n")

mensaje_completo = mensaje_descifrado  # LDSQW
for cuerda, binario in quipu_secundario.items():
    decimal = int(binario, 2)
    letra = chr(decimal + 64)
    mensaje_completo += letra
    print(f"  {cuerda}: {binario} → {decimal:2} → '{letra}'")

print(f"\n  ► Mensaje extendido: {mensaje_completo}")

# Aplicar la clave completa
print(f"\n  ► Aplicando clave completa...\n")

clave_extendida = clave_quipu_blanco + [2, 4, 6, 8, 10]
resultado_final = ""

for i, letra in enumerate(mensaje_completo):
    if i < len(clave_extendida):
        nueva_pos = (ord(letra) - 65 + clave_extendida[i]) % 26
        letra_final = chr(nueva_pos + 65)
        resultado_final += letra_final
        print(f"  {letra} + {clave_extendida[i]} → {letra_final}")
    else:
        resultado_final += letra

print(f"\n  ★ {resultado_final} ★")
```

El resultado apareció en la pantalla. Wayra sintió que el aire se congelaba.

```
  ★ KILLA ★
```

—Killa —susurró—. Mama Killa.

—¿La hermana? —preguntó Raúl, incrédulo—. ¿La hermana de Inti mató a su propio hermano?

—No... —dijo Lara, que había estado observando en silencio—. No. Ella lo protegió. Toda su vida lo protegió.

—¿De qué?

—De Los Herederos de Pizarro. De Rodrigo. De todos los que querían usar Yachay para sus propios fines. Inti sabía que si moría, Yachay no debía caer en manos equivocadas. Y Mama Killa... ella se aseguró de que eso no pasara.

Wayra entendió todo. El quipu no señalaba a la asesina. Señalaba a la **guardiana**. Mama Killa no había matado a Inti. Había hecho algo más importante: había protegido su legado.

—Pero entonces... —dijo Wayra—. ¿Quién mató a Inti?

Lara bajó la mirada.

—Mi padre. Rodrigo Mamani.

—Pero Rodrigo no tenía acceso al laboratorio...

—No. Pero yo sí. Y él usó mi cuenta. No me dijo lo que iba a hacer. Me pidió que le diera mi contraseña para "revisar unos archivos". Yo confiaba en él. Era mi padre.

—¿Y la llamada de Inti a las 02:30?

—Inti descubrió que alguien había entrado con mi cuenta. Me llamó para preguntarme si estaba bien. Le dije que yo no estaba en el laboratorio. Y él dijo... dijo: "Entonces ve a casa de tu tía Killa. Ahora. No vuelvas al laboratorio hasta que yo te llame."

—Te estaba protegiendo —dijo Wayra—. Sabía que ibas a ser la culpable ideal.

—Y lo fui. Mi padre usó mi cuenta. Mis huellas estaban en el teclado porque trabajaba ahí todos los días. Mi ADN estaba por todo el laboratorio. Todo apuntaba a mí.

—Pero el quipu de Inti... —dijo Raúl—. El mensaje dice "KILLA". ¿Por qué?

Wayra sonrió tristemente.

—Porque Inti no estaba señalando al asesino. Estaba señalando a la única persona que sabía la verdad y podía proteger a Lara. Su hermana. Mama Killa.

## El cierre del caso

Tres días después, la policía encontró pruebas definitivas contra Rodrigo Mamani. Los registros bancarios mostraban transferencias a un exmiembro del laboratorio que había manipulado los registros de acceso. Las cámaras de seguridad de un banco cercano mostraban a Rodrigo comprando una tarjeta SIM desechable a las 01:30 de la madrugada del crimen.

Lara fue exonerada. Pero su vida había cambiado para siempre. Había perdido a su mentor, había descubierto la verdad sobre su padre, y había encontrado un nuevo propósito.

Mama Killa, la hermana de Inti, se convirtió en la guardiana oficial de Yachay. Y Wayra Condori... Wayra se convirtió en la primera Investigadora Digital del Círculo del Sol.

El Código Asesino había hecho su trabajo. Pero no de la forma que esperaban. No había señalado a un culpable: había revelado una red de mentiras, lealtades y sacrificios que ningún algoritmo podía haber previsto.

Porque al final, la verdad no está en los datos. Está en las personas que los interpretan.

---

## Tu legado

Has llegado al final de este viaje. Has aprendido Python desde variables hasta programación orientada a objetos. Has resuelto un asesinato. Has descifrado quipus digitales.

Pero esto no es el final. Es el comienzo.

El conocimiento ancestral inca decía que cada persona es un quipu: una combinación única de hilos y nudos que cuenta una historia. Tu historia como programador apenas comienza.

Los quipus digitales de Inti Quispe siguen ahí, esperando ser descifrados. Yachay sigue activo, aprendiendo de los patrones ancestrales. Y el Círculo del Sol... bueno, el Círculo del Sol siempre está buscando nuevos guardianes.

*"Ama suwa, ama llulla, ama qilla"*
(No robes, no mientas, no seas perezoso)

— Que el código te acompañe.

---
