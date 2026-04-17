# Métricas de Impacto

En este proyecto se evaluaron modelos de clasificación utilizando el dataset de Titanic, cuyo objetivo es predecir si un pasajero sobrevive o no.

## Métricas consideradas

Para evaluar el rendimiento del modelo se consideran tres métricas principales:

- Accuracy
- Precision
- Recall

### Accuracy

La accuracy mide el porcentaje de predicciones correctas sobre el total de observaciones.

Es una métrica simple y útil cuando se busca una visión general del rendimiento del modelo.

### Precision

La precision indica qué proporción de las predicciones positivas fue correcta.

Es importante en contextos donde los falsos positivos son costosos.

### Recall

El recall mide qué proporción de los casos positivos reales fueron correctamente identificados.

Es clave cuando se busca minimizar los falsos negativos.

## Elección de la métrica

En este trabajo se utiliza la accuracy como métrica principal, ya que permite comparar de forma directa el rendimiento entre diferentes estrategias de validación, como Train/Test Split y Stratified K-Fold.

Dado que el objetivo del laboratorio es analizar la estabilidad y desempeño general del modelo, la accuracy resulta adecuada para evaluar y comparar ambos enfoques.

## Conclusión

Si bien métricas como precision y recall aportan información más específica, la accuracy permite una comparación clara y directa entre los métodos utilizados, siendo suficiente para el objetivo de este análisis.