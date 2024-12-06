# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

### *2.1. Resumen General de los datos*
---

* *¿Cuántos documentos tiene el dataset?*

Si se observa la siguiente tabla, se pueden ver algunas descripciones a nivel general de los datos, el número de entradas que son 75844 . La media del consumo de la microrred desde el 1 de Enero del 2018 hasta el 29 de Febrero del 2020 fue de 34415.848772. También se puede apreciar la desviación estándar, los percentiles principales y los datos en que han menor y mayor consumo de la microrred, siendo  26100.030000 y 51437.470000 los valores respectivos


* *¿En qué formato están guardados los datos?*

Los datos están guardados en un DataFrame de pandas, que es una estructura de datos en Python usada para manipular y analizar datos tabulares. Además:

La columna DateTime está en formato de cadena de texto (object).
La columna TotalCampusLoad está en formato numérico (float64).
Por lo tanto, los datos están organizados en formato tabular con 75,844 filas y 2 columnas.

* ¿Hay datos faltantes, documentos vacíos o de mala calidad?

*Comprobamos* si hay valores nulos en el dataFrame

Como se puede ver, no se tienen valores nulos por lo que es posible continuar con el análisis del DataFrame

* ¿Hay datos duplicados o repetidos?
Hay 12 duplicados

## Resumen de calidad de los datos

En esta sección se presenta un resumen de la calidad de los datos. Se describe la cantidad y porcentaje de valores faltantes, valores extremos, errores y duplicados. También se muestran las acciones tomadas para abordar estos problemas.

## Variable objetivo

En esta sección se describe la variable objetivo. Se muestra la distribución de la variable y se presentan gráficos que permiten entender mejor su comportamiento.

## Variables individuales

En esta sección se presenta un análisis detallado de cada variable individual. Se muestran estadísticas descriptivas, gráficos de distribución y de relación con la variable objetivo (si aplica). Además, se describen posibles transformaciones que se pueden aplicar a la variable.

## Ranking de variables

En esta sección se presenta un ranking de las variables más importantes para predecir la variable objetivo. Se utilizan técnicas como la correlación, el análisis de componentes principales (PCA) o la importancia de las variables en un modelo de aprendizaje automático.

## Relación entre variables explicativas y variable objetivo

En esta sección se presenta un análisis de la relación entre las variables explicativas y la variable objetivo. Se utilizan gráficos como la matriz de correlación y el diagrama de dispersión para entender mejor la relación entre las variables. Además, se pueden utilizar técnicas como la regresión lineal para modelar la relación entre las variables.
