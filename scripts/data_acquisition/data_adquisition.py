import pandas as pd
from tabulate import tabulate

data_url = "https://raw.githubusercontent.com/Juanes1793/Proyectos-Data-Science/main/Base_datos/DemandCharge.csv"

df = pd.read_csv(data_url)


print(tabulate(df.head(15), headers='keys', tablefmt='psql'))