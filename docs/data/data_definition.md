# Definición de los datos

## Origen de los datos

El estado de California está trabajando para reforzar la resiliencia de la electricidad local acelerando la adopción de microrredes, en particular a través de su Programa de Incentivos para Microrredes (MIP). Este programa asigna a las tres empresas de servicios eléctricos más grandes del estado $200 millones de dolares para construir microrredes comunitarias que apoyen a las comunidades desfavorecidas, específicamente en áreas propensas a incendios y apagones de sus territorios de servicio. A continuancion se un estudio que localiza las zonas potencialmente elegibles para el nuevo MIP de California y mapea los sitios óptimos para las microrredes en virtud de los objetivos del MIP, así como de otros objetivos de modernización de la red. Identifica y clasifica dónde las microrredes podrían ser más beneficiosas mediante la siembra de un modelo de idoneidad de ArcGIS con criterios elegidos por las empresas de servicios públicos e informados por la Comisión de Servicios Públicos de California, la Oficina de Planificación e Investigación de California y los participantes del taller MIP. Estos criterios reflejan los esfuerzos de las empresas de servicios públicos para reforzar la resiliencia de las poblaciones clave en áreas vulnerables a las interrupciones e incluyen distritos de alto riesgo de incendio de nivel 2 y 3, ubicaciones de cortes de energía de seguridad pública anteriores, circuitos con niveles históricamente bajos de confiabilidad y poblaciones desfavorecidas / vulnerables. Otros criterios hablan de beneficios adicionales que las microrredes pueden proporcionar, como la reducción de la contaminación, el arbitraje de los precios marginales de la electricidad por ubicación y la integración de las energías renovables.

La microrred de la Universidad de California, San Diego, sirve a una comunidad universitaria a más de 45,000 personas, 13 millones de pies cuadrados en 450 edificios, 1,200 acres, y genera el 80% de la electricidad utilizada en el campus anualmente. El campus controla 42 MW de generación y luego compra energía en el mercado. Cuenta con 2 turbinas de gas de 13,5 MW; una turbina de vapor de 3 MW; 1,2 MW de energía solar; y un contacto PPA de 2 MW para energía de pila de combustible que utiliza metano de una planta de tratamiento de aguas residuales. Algunos llaman a las microrredes "agrupaciones localizadas" de fuentes de energía.

La microrred gestiona de forma más eficiente la demanda en tiempo real, suministrando y almacenando energía a un coste menor y menos contaminante que una red convencional. Tiene un sistema de almacenamiento de energía térmica de 3.8 millones de galones que utiliza para enfriar el agua por la noche para el aire acondicionado diurno. UCSD reporta ahorros de más de $800,000 en costos de energía por mes debido a su microrred. Los estudiantes están adquiriendo experiencia práctica con el sofisticado sistema de control que administra cientos de entradas e incluso calcula los patrones de nubes y los efectos de protección solar.

La microrred gestiona de forma más eficiente la demanda en tiempo real, suministrando y almacenando energía a un coste menor y menos contaminante que una red convencional. Tiene un sistema de almacenamiento de energía térmica de 3.8 millones de galones que utiliza para enfriar el agua por la noche para el aire acondicionado diurno. UCSD reporta ahorros de más de $800,000 en costos de energía por mes debido a su microrred. Los estudiantes están adquiriendo experiencia práctica con el sofisticado sistema de control que administra cientos de entradas e incluso calcula los patrones de nubes y los efectos de protección sola

**Beneficios de uso de microred elecrtica:**

Los sistemas de control de la microrred actúan como una planta de energía virtual que programa la generación, el almacenamiento y las importaciones de energía, y tiene en cuenta la demanda y los precios de la electricidad. La microrred también incluye un sistema de almacenamiento de energía térmica que captura el agua enfriada de un enfriador de absorción de 300 toneladas.  

**_Los beneficios de la microrred incluyen:_**


_Costos más bajos:_  La microrred puede reducir los costos de electricidad y los cargos por demanda máxima.  

_Reducción de la necesidad de energía de la red:_ La microrred puede reducir la necesidad de energía de la red eléctrica más grande.  

_Mayor resiliencia:_ La microrred puede mejorar la resiliencia a las interrupciones de la red.  

_Reducción de emisiones:_ La microrred puede reducir las emisiones y los impactos ambientales.  

_Energía durante emergencias:_ La microrred puede "aislarse" en una emergencia eléctrica, desconectándose de la red y manteniendo las funciones críticas. 


**Acerca del copus para analisis de datos**

El corpus es un dataset tomado de GitHub que contiene un conjunto de datos La base de datos de la demanda de la potencia eléctrica de una microrred ubicada en un campus en San Diego, Estados Unidos , la cual tiene 75.844 datos registrados desde el 01/01/2018 hasta el 29/02-2020. La información fue recolectada con un tiempo de muestreo de 15 minutos.
  
  [Enlace de donde obtuvimos la información del pronoóstico de la demanda de una microred](https://github.com/sushilsilwal3/UCSD-Microgrid-Database/tree/master)

Se almacena el dataset como raw data en un respositorio de Github y se abre el link mediante una función de pandas. Luego con el script que está en data_acquisition, llamado con el mismo nombre procedemos a  convertir esta dataset en un json y finalmente guardarlo en la carpeta llamada "adquired_data_files"


## Especificación de los scripts para la carga de datos

El script para la carga de datos se puede encontrar en la carpeta de data_acquisition con su mismo nombre, como se mencionaba anteriormente , simplemente se convierte la información relacionada que luego se utilizará para un análisis de serie de tiempo en un dataframe, posteriormente a un json y se guarda en la carpeta adquired_data_files

## Referencias a rutas o bases de datos origen y destino

Soportes sobre la documentacion origen:
[Informacion origen datos.](https://escholarship.org/content/qt00k3737s/qt00k3737s.pdf)
[Informacion origen datos.](https://www.sdge.com/more-information/our-company/about-us)
[Informacion origen datos.](https://ecomotion.us/the-u-c-san-diego-microgrid/#tab-id-1)

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

