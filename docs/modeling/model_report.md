# Reporte del Modelo LSTM Vanilla

## Descripción del Modelo

El modelo LSTM Vanilla es una red neuronal recurrente que utiliza una sola capa de unidades LSTM para capturar patrones temporales y realizar predicciones. Incluye:

- *1 capa LSTM* con 50 unidades y activación ReLU.
- *1 capa densa de salida* que genera una única predicción por entrada.

El modelo se entrena utilizando el optimizador *Adam* y la función de pérdida *Mean Squared Error (MSE)*.

## Arquitectura del Modelo

Resumen de la arquitectura:

```
Model: "sequential_1" 
 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┓
 ┃ Layer (type)                         ┃ Output Shape                ┃ Param #         ┃ 
 ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━┩ 
 │ lstm (LSTM)                          │ (None, 50)                  │ 10,400          │ 
 ├──────────────────────────────────────┼─────────────────────────────┼─────────────────┤ 
 │ dense_1 (Dense)                      │ (None, 1)                   │ 51              │ 
 └──────────────────────────────────────┴─────────────────────────────┴─────────────────┘ 
 Total params: 10,451 Trainable params: 10,451 Non-trainable params: 0
```

## Entrenamiento del Modelo

### Configuración

- *Optimizador:* Adam
- *Función de pérdida:* MSE
- *Número de épocas:* 20
- *Early Stopping:* Implementado para detener el entrenamiento si no hay mejoras en la validación.

### Proceso de Entrenamiento

Resultados por época:

| Época | Loss (Entrenamiento) | Loss (Validación) |
|-------|-----------------------|-------------------|
| 1     | 0.0060               | 0.000556          |
| 2     | 0.000372             | 0.000340          |
| 3     | 0.000252             | 0.000295          |
| ...   | ...                  | ...               |
| 20    | 0.000194             | 0.000249          |

El modelo muestra una mejora constante hasta converger en la última época.

## Predicciones

El modelo predice valores en la serie temporal utilizando las secuencias de entrada. La salida se desnormaliza para comparar con los valores reales.

### Comparación de Predicciones vs. Valores Reales

Ejemplo de comparación en el conjunto de entrenamiento:

| Train Predictions | Actuals   |
|--------------------|-----------|
| 37,786.64         | 37,760.28 |
| 37,817.11         | 37,426.30 |
| 37,466.03         | 37,421.87 |
| ...               | ...       |

## Métricas de Evaluación

Se evaluaron las predicciones utilizando métricas estándar de series temporales:

- *Mean Squared Error (MSE):* 0.000211
- *Mean Absolute Error (MAE):* 0.00978
- *Mean Squared Log Error (MSLE):* 0.000130
- *Mean Absolute Percentage Error (MAPE):* 4.10%

## Análisis de Resultados

- *Fortalezas:*
  - Un MAPE del 4.10% indica alta precisión en la predicción.
  - El bajo error cuadrático medio (MSE) muestra que el modelo captura los patrones temporales con buena exactitud.
  - La simplicidad de la arquitectura permite un entrenamiento rápido.

- *Debilidades:*
  - El modelo podría no capturar adecuadamente patrones más complejos debido a su arquitectura univariada y de una sola capa.
  - Sensibilidad a datos atípicos debido a la falta de regularización explícita.

## Conclusiones

El modelo LSTM Vanilla ha demostrado un excelente rendimiento en la predicción de series temporales, con errores mínimos en las métricas. Sin embargo, hay oportunidades para mejorar:

1. *Ajuste de Hiperparámetros:* Optimizar el número de unidades LSTM, la tasa de aprendizaje y el tamaño de las secuencias de entrada.
2. *Pruebas con Modelos Multivariados:* Incluir más variables explicativas para capturar patrones adicionales.
3. *Experimentación con Arquitecturas Avanzadas:* Probar LSTM multicapa, GRU o modelos híbridos para mejorar aún más el rendimiento.

En general, este modelo establece una sólida línea base para tareas de predicción de series temporales.