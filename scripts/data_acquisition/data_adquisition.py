import pandas as pd
import json
from tabulate import tabulate
from pathlib import Path

# Url principal del dataset
data_url = "https://raw.githubusercontent.com/Juanes1793/Proyectos-Data-Science/main/Base_datos/DemandCharge.csv"

# lectura del dataset y conversión a dataframe
df = pd.read_csv(data_url)

# transformación de los datos para mejorar su visualización
print(tabulate(df.head(15), headers='keys', tablefmt='psql'))

# Save the Dataframe to a json file in adquired_data folder

time_series_data_dict = df.to_dict(orient='records')

# Path to the adquired_data folder

BASE_DIR = Path.cwd()
DATA_DIR = BASE_DIR / "adquired_data_files"

# Create the adquired_data folder if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)

# Save the Dataframe to a json file in adquired_data folder
with open(DATA_DIR / "time_series_data.json", "w") as f:
    json.dump(time_series_data_dict, f)

print(f"Data saved to {DATA_DIR}")

