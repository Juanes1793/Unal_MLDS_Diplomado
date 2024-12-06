### **Diccionario de datos**

#### **Base de datos 1**
Conjunto de datos sobre la demanda eléctrica de una microrred ubicada en un campus en San Diego, EE.UU., con registros tomados entre el 01/01/2018 y el 29/02/2020. La información se recolectó a intervalos de 15 minutos y se encuentra en formato CSV.

| Variable            | Descripción                                                | Tipo de dato  | Rango/Valores posibles         | Fuente de datos                                                                                       |
|---------------------|------------------------------------------------------------|---------------|---------------------------------|------------------------------------------------------------------------------------------------------|
| `DateTime`          | Fecha y hora de la medición de consumo eléctrico.          | Temporal      | 01/01/2018 - 29/02/2020        | [UCSD-Microgrid-Database](https://github.com/sushilsilwal3/UCSD-Microgrid-Database/tree/master)      |
| `TotalCampusLoad`   | Carga total de energía consumida en el campus.             | Continua      | 0 - Máximo registrado          | [UCSD-Microgrid-Database](https://github.com/sushilsilwal3/UCSD-Microgrid-Database/tree/master)      |
| `OnCampusGeneration`| Energía generada dentro del campus.                        | Continua      | 0 - Máximo registrado          | [UCSD-Microgrid-Database](https://github.com/sushilsilwal3/UCSD-Microgrid-Database/tree/master)      |
| `SDG&E Import`      | Energía importada desde San Diego Gas & Electric.          | Continua      | 0 - Máximo registrado          | [UCSD-Microgrid-Database](https://github.com/sushilsilwal3/UCSD-Microgrid-Database/tree/master)      |
| `AdjustedDemand`    | Demanda ajustada del campus considerando generación local. | Continua      | 0 - Máximo registrado          | [UCSD-Microgrid-Database](https://github.com/sushilsilwal3/UCSD-Microgrid-Database/tree/master)      |


- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.



