# Capítulo 8: Cómo Montar tu Primer Agente en 30 Minutos

## 8.1 El Proyecto Más Simple que Puedes Hacer Hoy

Has llegado hasta aquí. Has leído los conceptos, los casos, las herramientas. Ahora es el momento de ensuciarte las manos.

Vamos a montar un agente de principio a fin. Algo útil, que puedas usar hoy mismo, sin código, sin técnicos, en treinta minutos.

El proyecto: **un agente que responda automáticamente las preguntas frecuentes de tu negocio por correo electrónico.**

Cuando termines este capítulo, tendrás un sistema funcionando que responderá automáticamente a tus clientes cuando pregunten por horarios, precios, dirección, o cualquier otra pregunta repetitiva.

## 8.2 Lo que Necesitas (y ya deberías tener)

- Una cuenta de Gmail (si no tienes, créala: gmail.com, 5 minutos)
- Una cuenta de Zapier (zapier.com, regístrate gratis, 2 minutos)
- Una cuenta de ChatGPT (chat.openai.com, regístrate gratis, 2 minutos)

Si ya tienes estas cuentas del capítulo 2, estás listo. Si no, créalas ahora. Te prometo que vale la pena.

## 8.3 Paso a Paso: Tu Primer Agente

### Paso 1: Identifica tus 5 preguntas más frecuentes

Este es el paso más importante. Si haces esto bien, el resto funciona solo.

Abre un documento de texto (Google Docs, bloc de notas, lo que sea) y escribe las 5 preguntas que más recibes de tus clientes. Si no estás seguro, revisa tus últimos mensajes de WhatsApp, correos, o conversaciones.

Para ayudarte, aquí tienes ejemplos de diferentes negocios:

**Panadería El Trigo:**
1. ¿A qué hora abren y cierran?
2. ¿Tienen pan sin gluten o productos aptos para celíacos?
3. ¿Hacen envíos a domicilio? ¿Cuánto cobran?
4. ¿Cuánto cuesta una torta personalizada para 15 personas?
5. ¿Aceptan tarjetas de crédito o solo efectivo?

**Taller Mecánico Pérez:**
1. ¿Tienen hora para esta semana?
2. ¿Cuánto cuesta un cambio de aceite?
3. ¿Hacen revisión técnica?
4. ¿Cuál es la dirección y horario?
5. ¿Aceptan tarjetas o solo efectivo?

**Restaurante La Esquina:**
1. ¿Tienen menú vegetariano/vegano?
2. ¿Hay que reservar o se puede ir sin reserva?
3. ¿Cuál es el horario?
4. ¿Hacen delivery? ¿Cuánto tardan?
5. ¿Tienen estacionamiento?

### Paso 2: Prepara a ChatGPT con tus preguntas y respuestas

Abre ChatGPT (chat.openai.com) y escribe un mensaje como este:

"Voy a darte las 5 preguntas más frecuentes de mi negocio con sus respuestas. Quiero que las memorices para que, cuando un cliente me haga alguna de estas preguntas, me ayudes a responder de forma automática.

Estas son mis preguntas y respuestas:

1. Pregunta: [escribe tu pregunta 1]
   Respuesta: [escribe tu respuesta 1]

2. Pregunta: [escribe tu pregunta 2]
   Respuesta: [escribe tu respuesta 2]

3. Pregunta: [escribe tu pregunta 3]
   Respuesta: [escribe tu respuesta 3]

4. Pregunta: [escribe tu pregunta 4]
   Respuesta: [escribe tu respuesta 4]

5. Pregunta: [escribe tu pregunta 5]
   Respuesta: [escribe tu respuesta 5]

Importante: cuando respondas, usa el mismo tono que yo uso con mis clientes. Ni muy formal ni muy informal. Natural y cercano."

Ejemplo real para Panadería El Trigo:

"Voy a darte las 5 preguntas más frecuentes de mi negocio con sus respuestas. Quiero que las memorices para que, cuando un cliente me haga alguna de estas preguntas, me ayudes a responder de forma automática.

Estas son mis preguntas y respuestas:

1. Pregunta: ¿A qué hora abren y cierran?
   Respuesta: Abrimos de lunes a sábado de 7:00 a 20:00. Los domingos abrimos solo hasta las 14:00.

2. Pregunta: ¿Tienen pan sin gluten?
   Respuesta: Sí, tenemos pan de masa madre sin gluten y empanadas integrales. Los preparamos bajo pedido con 24 horas de anticipación.

3. Pregunta: ¿Hacen envíos a domicilio?
   Respuesta: Sí, hacemos envíos a domicilio sin costo adicional para pedidos mayores a 20€. El tiempo de entrega es de 45 a 60 minutos.

4. Pregunta: ¿Cuánto cuesta una torta personalizada para 15 personas?
   Respuesta: Nuestras tortas personalizadas para 15 personas tienen un precio de 45€ a 65€, dependiendo de los ingredientes y la decoración. Debes pedirla con 3 días de anticipación.

5. Pregunta: ¿Aceptan tarjetas?
   Respuesta: Sí, aceptamos tarjetas de crédito y débito. También puedes pagar con efectivo o transferencia bancaria."

ChatGPT confirmará que ha entendido y memorizado la información.

### Paso 3: Configura el filtro en Gmail

Ahora vamos a decirle a Gmail que identifique automáticamente los correos que contienen preguntas frecuentes.

1. Inicia sesión en tu Gmail
2. Haz clic en el icono de ajustes (rueda dentada, arriba a la derecha)
3. Selecciona "Ver todos los ajustes"
4. Ve a la pestaña "Filtros y direcciones bloqueadas"
5. Haz clic en "Crear un filtro nuevo"
6. En el campo "Contiene las palabras", escribe palabras clave separadas por espacio o coma. Por ejemplo:
   `horario precio abren envío tarjetas dirección`
7. Haz clic en "Crear filtro"
8. Marca la opción "Aplicar la etiqueta" y selecciona "Nueva etiqueta..."
9. Crea una etiqueta llamada "Consultas frecuentes"
10. Marca también "Omitir la bandeja de entrada" (así los correos clasificados no saturan tu bandeja principal)
11. Haz clic en "Crear filtro"

A partir de ahora, cualquier correo que contenga esas palabras clave llegará automáticamente etiquetado como "Consultas frecuentes".

**Consejo:** empieza con 5 palabras clave. Si ves que se te escapan consultas importantes, añade más palabras clave con el tiempo.

### Paso 4: Conecta Gmail con ChatGPT usando Zapier

Este es el paso donde ocurre la magia. Vamos a decirle a Zapier: "Cuando llegue un correo con la etiqueta 'Consultas frecuentes', envíalo a ChatGPT para que genere una respuesta."

1. Inicia sesión en Zapier (zapier.com)
2. Haz clic en "Create" y luego en "Zap"
3. **Disparador (Trigger):** busca y selecciona "Gmail"
4. **Evento:** selecciona "New Labeled Email" (Nuevo correo etiquetado)
5. **Conecta tu cuenta de Gmail:** sigue los pasos de autorización (Zapier te pedirá permiso para acceder a tu Gmail)
6. **Configura el disparador:**
   - Label/Etiqueta: selecciona "Consultas frecuentes" (la que creaste en el paso 3)
   - Marca "Include attachments?" como No
7. Haz clic en "Continue" y luego en "Test trigger" para probar que Zapier puede ver tus correos
8. Si la prueba es exitosa, haz clic en "Continue"

Ahora viene la parte divertida:

9. **Acción (Action):** busca y selecciona "ChatGPT"
10. **Evento:** selecciona "Generate Response" (Generar respuesta) o "Conversation"
11. **Conecta tu cuenta de ChatGPT:** si es la primera vez, autoriza la conexión
12. **Configura el prompt:**

En el campo "User Message" (Mensaje de usuario), escribe:

```
Eres el asistente de atención al cliente de [nombre de tu negocio].
Tu tono es amable, cercano y profesional.

Estas son las preguntas frecuentes y sus respuestas:

[pregunta 1 con su respuesta]
[pregunta 2 con su respuesta]
[pregunta 3 con su respuesta]
[pregunta 4 con su respuesta]
[pregunta 5 con su respuesta]

Si la pregunta del cliente coincide con alguna de las anteriores, responde con la respuesta correspondiente de forma natural.

Si la pregunta NO está en la lista, responde:
"Gracias por tu consulta. Te he derivado con [nombre del dueño] que te responderá en la brevedad posible."

Pregunta del cliente: [aquí inserta el contenido del correo]
```

Para insertar el contenido del correo, haz clic en el icono de "Insert data" y selecciona el campo "Body" o "Plain Text" del correo.

13. Haz clic en "Continue" y luego en "Test action" para ver una respuesta de ejemplo
14. Revisa la respuesta. Si te gusta, activa el Zap. Si no, ajusta el prompt y prueba de nuevo.

### Paso 5: Configura la respuesta automática (Acción 2)

Ahora necesitamos que la respuesta generada por ChatGPT se envíe como correo de respuesta. Zapier permite añadir múltiples acciones.

1. Haz clic en el signo "+" debajo de la acción de ChatGPT
2. **Acción:** selecciona "Gmail"
3. **Evento:** selecciona "Send Reply" (Enviar respuesta)
4. En "In Reply To", selecciona el ID del correo original (Thread ID)
5. En "Body", selecciona la respuesta generada por ChatGPT (campo "Response" de la acción anterior)
6. En "Subject", deja el asunto original o pon "RE: [asunto original]"
7. Haz clic en "Continue" y prueba

### Paso 6: Activa y prueba

1. Una vez que todo esté configurado, dale un nombre a tu Zap (ej: "Responder consultas frecuentes")
2. Haz clic en "Publish" para activarlo
3. Envíate un correo de prueba a ti mismo preguntando "¿cuál es el horario?"
4. En unos minutos, deberías recibir la respuesta automática

**Felicidades. Acabas de montar tu primer agente de inteligencia artificial.**

## 8.4 Versión WhatsApp (Más Fácil)

Si prefieres empezar por WhatsApp porque tus clientes lo usan más, el proceso es aún más simple.

1. **Descarga WhatsApp Business** desde Google Play o App Store
2. **Configura tu perfil:** nombre del negocio, horarios, dirección, descripción breve
3. **Crea respuestas rápidas:**
   - Ve a Herramientas > Respuestas rápidas
   - Haz clic en el icono "+"
   - Escribe un acceso directo (ej: /horario) y el texto de la respuesta
   - Crea una para cada pregunta frecuente
4. **Configura el mensaje de bienvenida:**
   - Ve a Herramientas > Mensaje de bienvenida
   - Actívalo y escribe un mensaje como:
     "Gracias por contactar a [nombre del negocio]. Aquí tienes nuestras respuestas rápidas. Si tu consulta no está en la lista, te responderemos en breve."
5. **Configura el mensaje de ausencia:**
   - Ve a Herramientas > Mensaje de ausencia
   - Actívalo y programa el horario fuera del laboral
   - Escribe un mensaje como:
     "Gracias por escribirnos. Estamos fuera de horario. Te responderemos cuando abramos. Nuestro horario es [horario]."

**Tiempo estimado: 15 minutos. Resultado: respuestas automáticas a las preguntas más frecuentes por WhatsApp.**

## 8.5 Versión para Formularios Web

Si tienes una página web con formulario de contacto, puedes automatizar las respuestas:

1. **Conecta el formulario con Google Sheets:** la mayoría de los creadores de formularios (Google Forms, Typeform, etc.) tienen integración directa
2. **Configura Zapier:**
   - Disparador: "Google Sheets - New Row" (cuando llegue un nuevo registro)
   - Acción 1: "ChatGPT - Generate Response" con el prompt de atención al cliente
   - Acción 2: "Gmail - Send Email" al cliente que llenó el formulario
3. **Prueba y activa**

## 8.6 La Plantilla de Prompt Definitiva

Guarda esta plantilla. La vas a usar cada vez que crees un nuevo agente:

```
Eres el asistente de atención al cliente de [nombre del negocio].
Tu tono es [amable / profesional / cercano / divertido].

CONTEXTO DEL NEGOCIO:
[Tipo de negocio, productos/servicios principales, valores de la marca]

PREGUNTAS FRECUENTES (responde SOLO si la consulta coincide):
[Pregunta 1] → [Respuesta 1]
[Pregunta 2] → [Respuesta 2]
[Pregunta 3] → [Respuesta 3]

REGLAS:
- Si la consulta coincide con una pregunta frecuente, responde con la respuesta correspondiente
- Si la consulta NO coincide, responde: "Gracias por tu consulta. Te he derivado con [nombre] que te responderá en breve."
- No inventes información que no esté en la lista
- No respondas quejas o reclamos, derívalos siempre
- Usa un tono natural, no suenes a robot

CONSULTA DEL CLIENTE:
[Insertar consulta aquí]

RESPUESTA:
```

## 8.7 Próximos Pasos (Después de tu Primer Agente)

Una vez que tu primer agente esté funcionando, puedes mejorarlo progresivamente:

**Semana 1:** Añade más preguntas a la lista a medida que identificas nuevas consultas recurrentes
**Semana 2:** Conecta el agente con WhatsApp usando Twilio o WATI para cubrir ambos canales
**Semana 3:** Haz que el agente registre todas las consultas en una hoja de cálculo para analizar patrones
**Semana 4:** Programa un resumen semanal de las consultas recibidas: cuántas, de qué tipo, cuántas se derivaron a humano

## 8.8 Solución de Problemas Comunes

| Problema | Causa probable | Solución |
|----------|---------------|----------|
| El agente no responde | Zapier no está activo | Ve a Zapier y verifica que el Zap esté encendido (verde) |
| El agente responde cualquier cosa | El prompt no es específico | Revisa las preguntas y respuestas. Sé más preciso |
| Las respuestas suenan robóticas | El prompt no pide tono natural | Añade "Usa un tono natural y cercano, no suenes a robot" |
| No se activa el disparador | El filtro de Gmail no funciona | Envíate un correo de prueba y verifica que llegue etiquetado |
| ChatGPT se confunde | Demasiada información en el prompt | Simplifica. 5 preguntas máximo para empezar |
| Los clientes se quejan | El agente responde mal | Revisa los casos, ajusta el prompt, y deriva más consultas a humano |

## 8.9 Resumen

- El proyecto más simple para empezar es un agente que responda preguntas frecuentes por correo electrónico
- En 30 minutos puedes tenerlo funcionando con Gmail + Zapier + ChatGPT
- Las 5 preguntas más importantes: identifícalas revisando tus últimos mensajes reales
- El prompt correcto es la clave del éxito: sé específico, da ejemplos, define el tono
- WhatsApp Business es una alternativa más simple si tus clientes usan principalmente WhatsApp
- Después del primer agente, mejóralo progresivamente: más preguntas, más canales, análisis de datos
- Los errores son normales al principio. Ajusta el prompt y vuelve a probar
- Treinta minutos. Una tarea. Empieza hoy.
