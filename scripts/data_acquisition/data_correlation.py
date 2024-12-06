from config import DATA_DIR, BASE_DIR
import pandas as pd
import plotly.express as px

#%% Leemos el dataset
# Leemos el  json desde la carpeta adquired_data_files
df = pd.read_json(DATA_DIR / "time_series_data.json")
df_forecast = df[["DateTime", "TotalCampusLoad"]]

# Eliminamos datos repetidos o duplicados
df_forecast.drop_duplicates(subset='DateTime', keep='last', inplace=True)

#%% Se organizan los datos por fecha

# Organizamos el dataset para que quede organizado por fecha
df_forecast_sorted = df_forecast.copy()
df_forecast_sorted.rename(columns = {'TotalCampusLoad	':'Consumo'}, inplace = True)                    #Se cambia el nombre de serie 1 a Total personas por Día para tene rmás clairdad
df_forecast_sorted['DateTime'] = pd.to_datetime(df_forecast_sorted.DateTime).dt.tz_localize(None)          # Revisar  #Se convierte la columba DateTime a formato fecha sin el formato UTC
df_forecast_sorted.sort_values(by=['DateTime'], axis=0, ascending=True, inplace=True)       #Se ordenan los datos
df_forecast_sorted.reset_index(inplace=True, drop=True)
df_forecast_sorted


#%% Datos resumidos por mes año y día
df_forecast_sorted = df_forecast_sorted.set_index('DateTime')

print(f"#" * 50)
print(df_forecast_sorted.resample("m").sum().head(100))
print(f"#" * 50)


#%% Distribución de los datos por días de semana, meses y año, etc
# Se toman los valores de la columna "DateTime" convertida a índice
df_forecast_sorted['Dia_semana'] = df_forecast_sorted.index.dayofweek
df_forecast_sorted['Dia_año'] = df_forecast_sorted.index.dayofyear
df_forecast_sorted['Mes'] = df_forecast_sorted.index.month
df_forecast_sorted['Hora'] = df_forecast_sorted.index.hour
df_forecast_sorted['Nombre_Dia'] = df_forecast_sorted.index.day_name()
df_forecast_sorted['Dia_Mes'] = df_forecast_sorted.index.day # Day of Month
df_forecast_sorted['Fecha'] = df_forecast_sorted.index.date
df_forecast_sorted['Estación_Año'] = df_forecast_sorted['Mes'].apply(lambda month_number: (month_number%12 + 3)//3)



#%% Correlaciones
# Matriz de correlación
df_forecast_filtered = df_forecast_sorted[["TotalCampusLoad", "Dia_semana", "Dia_año", "Mes", "Hora", "Dia_Mes", "Estación_Año"]]
correlation_matrix  = df_forecast_filtered.corr()

# Guardamos la imagen en un archivo
fig = px.imshow(correlation_matrix, text_auto=True)
fig.update_layout(title_text="Matriz de correlación")
fig.write_image(str(BASE_DIR / "docs" / "data" / "correlation_matrix.png"))


#%% Consumo de la microrred
# plotly doesn't allow us to access the index, so let's copy it into a column
df_forecast_filtered['date_and_time'] = df_forecast_filtered.index

# plotting
fig = px.line(df_forecast_filtered,
              x='date_and_time',
              y='TotalCampusLoad',
              title="Consumo_Microrred")
fig.update_traces(line=dict(width=0.05))
fig.update_layout(xaxis_title='Fecha & Hora (yyyy/mm/dd hh:MM)',
                  yaxis_title='Consumo_Microrred')
#fig.show()
fig.write_image(str(BASE_DIR / "docs" / "data" / "consumo_microrred.png"))


#%% Consumo de la microrred por estaciones del año 

# aggregated data
_ = df_forecast_filtered\
    .groupby(['Hora', 'Estación_Año'], as_index=False)\
    .agg({'TotalCampusLoad':'median'})

# plotting
fig = px.line(_,
              x='Hora',
              y='TotalCampusLoad',
              color='Estación_Año',
              title='Media de consumo de la microrred por Estaciones del Año')
fig.update_layout(xaxis_title='Hora',
                  yaxis_title='Consumo de la Microrred')
#fig.show()
fig.write_image(str(BASE_DIR / "docs" / "data" / "consumo_microrred_estaciones_año.png"))