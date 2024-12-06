from config import DATA_DIR
import pandas as pd

#%% Leemos el dataset
# Leemos el  json desde la carpeta adquired_data_files
df = pd.read_json(DATA_DIR / "time_series_data.json")
print(df.head(5))


#%% Número total de observaciones
n_total_observations = len(df)
print(f"El número total de observaciones es {n_total_observations}\n\n\n")
print(f"#" * 50)


#Variables con las que se van a trabajar 
"""
Primero que todo, como trabajaremos con series de tiempo y no trabajaremos con variables exógenas, 
es decir, solamente con una variable. Solamente nos quedaremos con la columna de tiempo y la variable 
llamada TotalCampusLoad. Por lo que haremos un filtrado inicial del dataset
"""
df_forecast = df[["DateTime", "TotalCampusLoad"]]
print(df_forecast.head(5))
print(f"#" * 50)

#%% ¿En qué formato están guardados los datos?
"""
Los datos están guardados en un DataFrame de pandas, que es una estructura de datos en Python usada para manipular y analizar datos tabulares. Además:

La columna DateTime está en formato de cadena de texto (object).
La columna TotalCampusLoad está en formato numérico (float64).
Por lo tanto, los datos están organizados en formato tabular con 75,844 filas y 2 columnas.

"""
print(f"Información sobre el dataset Modificado {df_forecast.info()}\n\n\n")
print(f"#" * 50)

# Hay presencia de valores Faltantes?

print(f"Comprobamos si hay valores nulos en el dataFrame\n\n\n")
print(df_forecast.isnull().sum())
print(f"#" * 50)
# Como se puede ver en la tabla, no se tienen valores nulos. 






