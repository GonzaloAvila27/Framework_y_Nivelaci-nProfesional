# Métricas de evaluación: Accuracy, Precision y Recall

En este trabajo usamos el dataset del Titanic, donde la idea es predecir si una persona sobrevive o no. Es un problema simple de clasificación: o sobrevive (1) o no sobrevive (0).

Cuando evaluamos un modelo, no alcanza con ver cuántas veces acierta en total. También es importante entender en qué se equivoca, porque no todos los errores son iguales.

Por ejemplo:
- Un falso positivo es cuando el modelo dice que alguien va a sobrevivir pero en realidad no sobrevive.
- Un falso negativo es cuando el modelo dice que alguien no va a sobrevivir pero en realidad sí sobrevive.

Dependiendo de lo que uno quiera analizar, uno de estos errores puede ser peor que el otro. Por eso no existe una sola métrica “mejor”.

La accuracy es la más simple: mide cuántas predicciones fueron correctas en total. El problema es que a veces puede engañar, sobre todo si hay muchos más casos de una clase que de otra.

La precision se fija en qué tan confiables son los positivos. O sea, de todos los que el modelo dijo que iban a sobrevivir, cuántos realmente sobrevivieron. Sirve cuando no querés equivocarte diciendo que algo es positivo cuando no lo es.

El recall, en cambio, se fija en no dejar pasar casos importantes. Mide cuántos de los que realmente sobrevivieron fueron detectados por el modelo. Sirve cuando te importa no perder positivos.

En resumen, la métrica que conviene usar depende del objetivo. Si querés encontrar la mayor cantidad posible de sobrevivientes, te conviene mirar recall. Si querés que tus predicciones sean más confiables, te conviene precision. Y la accuracy sirve como referencia general, pero no alcanza por sí sola.