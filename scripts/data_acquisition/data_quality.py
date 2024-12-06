from config import DATA_DIR
import pandas as pd

#%% Leemos el dataset
# Leemos el  json desde la carpeta adquired_data_files
df = pd.read_json(DATA_DIR / "time_series_data.json")


#%% Hay valores duplicados? 

print(f"#" * 50)
df_forecast = df[["DateTime", "TotalCampusLoad"]]
print(f"El número de observaciones duplicadas es {df['DateTime'].duplicated().sum()}\n\n\n")
print(f"#" * 50)