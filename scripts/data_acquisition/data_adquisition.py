import pandas as pd
from tabulate import tabulate

# Url principal del dataset
data_url = "https://raw.githubusercontent.com/Juanes1793/Proyectos-Data-Science/main/Base_datos/DemandCharge.csv"

# lectura del dataset y conversión a dataframe
df = pd.read_csv(data_url)

# transformación de los datos para mejorar su visualización
print(tabulate(df.head(15), headers='keys', tablefmt='psql'))