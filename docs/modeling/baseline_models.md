# Reporte del Modelo Baseline

# Modelo GRU que hace parte de modelos LSTM 

## Descripción del Modelo

El modelo baseline utiliza una red GRU (Gated Recurrent Unit) diseñada para predecir valores de una serie temporal, en este caso, el consumo de una microrred. Este modelo establece un punto de referencia para evaluar el rendimiento de modelos más complejos en el futuro.

## Variables de Entrada

Las variables de entrada seleccionadas para el modelo son:

- `Dia_semana`
- `Dia_año`
- `Mes`
- `Hora`
- `Dia_Mes`
- `Estación_Año`

Además, se utiliza la secuencia de la demanda histórica (`TotalCampusLoad`) como característica principal.

## Variable Objetivo

La variable objetivo del modelo es:

- `TotalCampusLoad` (Demanda total del campus).

## Evaluación del Modelo

### Métricas de Evaluación

Se utilizaron las siguientes métricas para evaluar el rendimiento del modelo:

- **Mean Squared Error (MSE):** Evalúa el error cuadrático promedio entre los valores predichos y los reales.
- **Mean Absolute Error (MAE):** Mide el error absoluto promedio.
- **Mean Squared Logarithmic Error (MSLE):** Evalúa el error logarítmico promedio.
- **Mean Absolute Percentage Error (MAPE):** Proporciona el error porcentual promedio.

### Resultados de Evaluación

| Métrica                  | Resultado         |
|--------------------------|-------------------|
| **MSE**                 | 0.0005374         |
| **MAE**                 | 0.01835           |
| **MSLE**                | 0.0003073         |
| **MAPE**                | 7.43%             |

El modelo muestra un bajo error en las métricas, indicando un buen rendimiento en las predicciones.

## Análisis de los Resultados

- **Fortalezas:**
  - El MAPE de 7.43% demuestra que el modelo tiene un error porcentual relativamente bajo, lo que lo hace confiable para predicciones a corto plazo.
  - La configuración del modelo GRU con capas adicionales, BatchNormalization y Dropout mejora la capacidad de generalización y reduce el sobreajuste.
  - El uso de EarlyStopping evitó entrenamientos innecesarios, logrando un balance entre el ajuste y la eficiencia.

- **Debilidades:**
  - Aunque los errores absolutos son bajos, el modelo podría ser sensible a datos con alta variabilidad, especialmente en valores extremos.
  - Se entrenó únicamente con una serie univariada; modelos multivariados podrían capturar más complejidad y patrones ocultos.

## Conclusiones

El modelo baseline GRU tiene un desempeño sólido en la predicción de la demanda de la microrred, con métricas que indican alta precisión y bajo error. Sin embargo, hay espacio para mejorar mediante:

1. Incorporar más variables explicativas relevantes.
2. Experimentar con arquitecturas más avanzadas como redes LSTM o modelos híbridos.
3. Ajustar hiperparámetros para mejorar la capacidad de generalización.

## Referencias

- Dataset: `df_forecast_sorted`
- Arquitectura GRU diseñada en base a las mejores prácticas para series temporales.
- Métricas de evaluación implementadas con bibliotecas de `sklearn` y funciones personalizadas.
