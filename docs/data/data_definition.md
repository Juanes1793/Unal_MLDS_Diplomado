# Definición de los datos

## Origen de los datos

El corpus es un dataset tomado de GitHub que contiene un conjunto de datos La base de datos de la demanda de la potencia eléctrica de un microrred utilizada es la de una microrred ubicada en un campus en San Diego, Estados Unidos , la cual tiene 75.844 datos registrados desde el 01/01/2018 hasta el 29/02-2020. La información fue recolectada con un tiempo de muestreo de 15 minutos.
  
  [Enlace de donde obtuvimos la información del pronoóstico de la demanda de una microred](https://github.com/sushilsilwal3/UCSD-Microgrid-Database/tree/master)

Se almacena el dataset como raw data en un respositorio de Github y se abre el link mediante una función de pandas. Luego con el script que está en data_acquisition, llamado con el mismo nombre procedemos a  convertir esta dataset en un json y finalmente guardarlo en la carpeta llamada "adquired_data_files"


## Especificación de los scripts para la carga de datos

El script para la carga de datos se puede encontrar en la carpeta de data_acquisition con su mismo nombre, como se mencionaba anteriormente , simplemente se convierte la información relacionada que luego se utilizará para un análisis de serie de tiempo en un dataframe, posteriormente a un json y se guarda en la carpeta adquired_data_files

## Referencias a rutas o bases de datos origen y destino

La base de datos de origen está alojada en el repositorio de GitHub:

[UCSD-Microgrid-Database.](https://github.com/sushilsilwal3/UCSD-Microgrid-Database/tree/master)

Los datos se almacenan como un archivo CSV en formato crudo (raw data).
Destino: Una vez transformados, los datos se guardan como archivos JSON en la carpeta local adquired_data_files.


### Rutas de origen de datos

# Ubicación de los archivos de origen:

El archivo de datos de origen está ubicado en:
https://github.com/sushilsilwal3/UCSD-Microgrid-Database/tree/master

# Estructura de los archivos de origen:

Los datos de origen tienen la siguiente estructura:

- DateTime: Fecha y hora de la medición (tipo temporal/fecha-hora).
- TotalCampusLoad: Carga total del campus (variable continua).
- OnCampusGeneration: Generación de energía en el campus (variable continua).
- SDG&E Import: Energía importada de San Diego Gas & Electric (variable continua).
- AdjustedDemand: Demanda ajustada (variable continua).


# Procedimientos de transformación y limpieza:

Se utiliza un script en la carpeta data_acquisition para cargar el archivo CSV utilizando pandas.
Los datos se convierten de un DataFrame a un archivo JSON mediante funciones de conversión de pandas.
El archivo JSON transformado se guarda en la carpeta local adquired_data_files para análisis posterior.

