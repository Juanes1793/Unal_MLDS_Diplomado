# Project Charter - Entendimiento del Negocio

## Integrantes del Grupo:



|**Integrantes**                            | **Correo** |
|------------------------------------------|---------------------------------------------------------------------------------------------------|
|Juan Esteban López Cardona | juanes1793@gmail.com                |
|Nelson Ferrucho  González | nelson.ferrucho@gmail.com              |
|Andres Camilo Rodriguez Patarroyo |acamro@gmail.com                |


## Nombre del Proyecto

**Proyecto Series de tiempo para la prediccion de la demanda en una microred**

## Marco del Proyecto

 Una microred es un circuito eléctrico que produce y distribuye energía de forma autónoma, y puede operar conectada o desconectada de la red eléctrica principal. Las microrredes son una solución para suministrar energía sostenible a comunidades pequeñas, especialmente a las que están alejadas de los grandes centros urbanos.

## Objetivo del Proyecto

 Aplicar el método de GRU secuence to secuence para el pronóstico de la demanda en una microrred utilizando series de tiempo.

 Con la información de la demanda nos permite realizar pronóstico a futuro de cada 15 minutos con un horizonte de pronóstico para la demanda de la microrred de un día hacia el futuros.


### **1.1. Trasfondo del Negocio**
---

- **¿Quién es el cliente o los beneficiarios del proyecto?**

  La base de datos de la demanda de la potencia eléctrica de un microrred utilizada es la de una microrred ubicada en un campus en San Diego, Estados Unidos , la cual tiene 75.844 datos registrados desde el 01/01/2018 hasta el 29/02-2020. La información fue recolectada con un tiempo de muestreo de 15 minutos. Por lo que el cliente es la universidad de San Diego, que busca optimizar y predecir el consumo en la microrred.

- **¿En qué dominio se encuentran?**

  Este proyecto se ubica dentro del dominio del predicción de consumo electrico para obtener un sector y zona especifico. El análisis de consumos permite a la empresa optimizar los costos y calidad de servicio en la zona.


- **¿Qué problemas del negocio o del dominio estamos tratando de solucionar?**

  Con la información de la demanda nos permite realizar pronóstico a futuro de cada 15 minutos con un horizonte de pronóstico para la demanda de la microrred de un día hacia el futuro. En conclusión estamos tratando de predecir el pronóstico de la demanda eléctrica para una microrred.

 ### **1.2. Alcance**
---



- **¿Qué  solución de _Deep Learning_  queremos implementar**

  
  Aplicar el método de GRU secuence to secuence para el pronóstico de la demanda en una microrred utilizando series de tiempo.

- **¿Qué  se hará?**
Se desarrollará un modelo de GRU, La GRU, también conocida como Gated Recurrent Unit, se introdujo en 2014 para resolver el problema común de gradiente desvanecido al que se enfrentaban los programadores. Muchos también consideran la GRU una variante avanzada de la LSTM debido a sus diseños similares y a sus excelentes resultados. Como se ha mencionado anteriormente, las Unidades Recurrentes Cerradas (GRU) son una variación avanzada de las SRRN (redes neuronales recurrentes estándar)




**¿De qué forma el cliente o beneficiario utilizará el producto del proyecto**


  - Optimizar los gastos en consumo de energia para la toma de decisiones sobre el servicio. .

  - Monitorear el impacto de cambios en el servicio o la aplicación mediante la comparación del modelo con los datos reales, permitiendo tomar desciones sobre cambios de mejora posibles a realizar .

  - Adaptabilidad a Cambios en el Comportamiento de la Demanda.

  - Optimización del Uso de Recursos Energéticos

  - Gestión Eficiente del Almacenamiento de Energía

  - Mayor precisión en los pronósticos de demanda energética.

  - Mejora de la Eficiencia Energética. 

### *1.3. Plan*

| *Actividad*                            | *Duración Estimada* | *Descripción*                                                                                   |
|------------------------------------------|-----------------------|---------------------------------------------------------------------------------------------------|
| *1. Preparacion de los datos:* | 3 días                | Tratamiento de los  datos de demanda en la microred. |
| *2. Preprocesamiento de los datos*      | 5 días                | Utilizan funciones para evaluar la desviacion y huecos posibles en los datos de entrada    |
| *3. Evaluacion distribucion de los datos y su contenido*         | 4 días                | Seleccion de las columnas disponibles en el dataset para realizar el modelo de tratamiento. |
| *4. Selección de modelo y entrenamiento* | 7 días                | Definición de capas : reset gate, Update gate, Candidate for hidden state. |
| *5. Aplicacion y Compilacion  del modelo*     | 3 días                | Establecer la funcion de perdida, la optimizacion y metricas para el modelo. |
| *6. Entrenamiento del modelo*     | 5 días                | Entrenamiento del modelo y  ajuste de hiperparámetros para mejorar rendimiento. |
| *7. Evaluacion de resultados*        | 3 días                |Presentacion de resultados obtener métricas como Test Mean Squared Error, Test Mean Absolute Error, Test Mean squared log error       |

## *2. Datos*

### *2.1. Origen*
---

 - *¿De dónde vienen los datos?*

  El corpus es un dataset tomado de GitHup que contiene un conjunto de datos La base de datos de la demanda de la potencia eléctrica de un microrred utilizada es la de una microrred ubicada en un campus en San Diego, Estados Unidos , la cual tiene 75.844 datos registrados desde el 01/01/2018 hasta el 29/02-2020. La información fue recolectada con un tiempo de muestreo de 15 minutos.
  
  [Enlace de donde obtuvimos la información del pronoóstico de la demanda de una microred](https://github.com/sushilsilwal3/UCSD-Microgrid-Database/tree/master)

- *¿Se usa alguna herramienta o proceso para la descarga de la información?*

  Se almacena el dataset como raw data en un respositorio de Github y se abre el link mediante una función de pandas y lo trabajos como un dataframe en GoogleColab.
  
- *¿Qué tipo de datos estamos manejando?*

  El conjunto de datos contiene variables continuas, son las mediciones del consumo de potencia de una microred. Este dateset cuenta con las siguientes caracteristicas:

  1. DateTime: fecha de medicion consumo. Variable de tipo temporal o fecha/hora.
  2. TotalCampusLoad: Variable continua.
  3. OnCampusGeneration: Variable continua.
  4. SDG&E Import. Variable continua.
  5. AdjustedDemand. Variable continua.