# -*- coding: utf-8 -*-
"""Workshop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cCa1WBUeFUxPRegvK7CyVC6DGmqTdd0W

# **SEABORN**

SEABORN es una librería de Python que te permite realizar gráficos para visualizar datos. Puedes configurarlos, editarlos, personalizarlos, etc. Los pasos básicos para utilizar esta librería son:
1. Preparar los datos
2. Graficar (plot) con Seaborn
3. Personalizar tu gráfico
4. Mostrar tu gráfico

### CASO TITANIC
Para esta clase nos concentramos en manipular la data proveniente del famoso accidente del Titanic. 
Estos datos se encuentran en la librería de Seaborn, por lo cual no será necesario descargar nada
"""

# 0. Importamos las librerías necesarias
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Preparar los datos

titanic = sns.load_dataset("titanic")
titanic.head()

# nombres de las columnas del dataframe
titanic.columns

# También podemos conocer más sobre los datos con las  siguientes funciones:
titanic.describe()

titanic.info()

# Ahora podemos proceder al análisis de los datos por medio de los gráficos

# GRÁFICO DE BARRAS
sns.set_style("darkgrid")
sns.set_palette('bright')
sns.countplot(x="survived", data=titanic)
plt.title("Número de pasajeros que sobrevivieron")
plt.show()

sns.countplot(x="survived", hue ="sex", data=titanic)
plt.title("Número de pasajeros por sexo que sobrevivieron")
plt.show()

# ¿Cuál es el rango de edad más frecuente entre pasajeros?
sns.histplot(x = "age", data = titanic)
plt.title("Histograma de edades de pasajeros") #definimos el título
plt.show() #mostramos el gráfico

sns.histplot(x = "age", data = titanic, hue = "survived")
plt.title("Histograma de edades de pasajeros") 
plt.show() #mostramos el gráfico

sns.histplot(x="age",data=titanic,hue="sex")
plt.title("Histograma de edades de pasajeros") 
plt.show() #mostramos el gráfico

# edad en el eje “x”, precio pagado en el eje “y”
# hue = sexo del pasajero
sns.scatterplot(x="age",y="fare", hue="who", data=titanic)
plt.title("Precio pagado por edad y género")
plt.show()

# edad en el eje “x”, precio pagado en el eje “y”
# hue = sexo del pasajero
plt.figure(figsize=(10,6))
sns.scatterplot(x="age",y="fare",size="class", hue="sex", data=titanic)
plt.title("Precio pagado por edad y género")
plt.show()

# edad en el eje “x”, precio pagado en el eje “y”
sns.pointplot(x="class",y="age",hue="sex",data=titanic)
plt.title("Promedio de precio pagado por edad y sexo")
plt.show()

"""---
### Reto grupal
Para esta reto nos concentramos en manipular la data proveniente de Titanic. 
Estos datos se encuentran en la librería de Seaborn, por lo cual no será necesario cargarlo.

### ¿Cuántos pasajeros había en cada clase?
"""

sns.countplot(x = "class", data = titanic)
plt.title("¿Cuántos pasajeros había en cada clase?")
plt.show()

"""###¿Cuántas mujeres y hombres hay por cada clase en el Titanic?




"""

sns.countplot(x = "class", hue = "sex", data = titanic)
plt.title("¿Cuántas mujeres y hombres hay por cada clase en el Titanic?")
plt.show()

"""### ¿Cuál es el rango de precio de boletos (fare) más frecuente?



"""

sns.histplot(x = "fare", data = titanic[titanic['fare']<=20])
plt.title("¿Cuál es el rango de precio de boletos (fare) más frecuente?")
plt.show()

"""#### ¿Cuál es el rango de precios de boletos más frecuente por sobrevivientes?


"""

sns.histplot(x = "fare", hue = "survived", data = titanic)
plt.title("¿Cuál es el rango de precios de boletos más frecuente por sobrevivientes?")
plt.show()

"""---
### CASO CAMBIO CLÍMATICO
Para esta clase nos concentramos en manipular la data sobre el cambio de temperatura. 
Estos datos no se encuentran en la librería de Seaborn, por lo cual será necesario cargarlo.



"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('GlobalTemperatures.csv',sep=',')
df

df.describe()

print(df.columns)

print(df.head())

from datetime import datetime

datetime.strptime('1750-01-01', '%Y-%m-%d').month    

datetime.strptime('1820-08-01', '%Y-%m-%d').strftime('%Y-%m')

years = []

for string in df['dt']:
  years.append(datetime.strptime(string, '%Y-%m-%d').year)

df['year'] = years
df=df[['dt','LandAverageTemperature','year']]
df

df_year = df.groupby('year').mean()
df_year

plt.figure(figsize=(15,8))
sns.lineplot(x='year', y='LandAverageTemperature',data = df_year)
plt.title('Temperatura por año')
plt.show()

# POR PAISES
df_paises = pd.read_csv('GlobalLandTemperaturesByCountry.csv',sep=',')
df_paises

# sacar el año sin loop
df_paises['year'] = df_paises['dt'].apply(lambda x: datetime.strptime(x, '%Y-%d-%m').year)
df_paises

avg_country = df_paises.groupby(['Country']).mean()
avg_country['Country'] = avg_country.index
avg_country[(avg_country['Country'] == 'Peru') | (avg_country['Country'] == 'China')]

# scatterplot, lineplot
plt.figure(figsize=(8,8))
sns.barplot(x = 'Country', y = 'AverageTemperature',
            data=avg_country[(avg_country['Country'] == 'Peru') | (avg_country['Country'] == 'China')])
plt.show()

# quitar los NaN de la base de datos
df_paises = df_paises.dropna()

df_paises[(df_paises['Country'] == 'Peru') | (df_paises['Country'] == 'China')]

mean_year = df_paises.groupby(['year','Country']).mean()
mean_year['year'] = mean_year.index.to_frame()['year']
mean_year['Country'] = mean_year.index.to_frame()['Country']
mean_year

mean_year[(mean_year['Country'] == 'Peru') | (mean_year['Country'] == 'China')]

plt.figure(figsize=(8,8))
sns.lineplot(x = 'year', y ='AverageTemperature',  hue = 'Country',
             data = mean_year[(mean_year['Country'] == 'Japan') | (mean_year['Country'] == 'China') | (mean_year['Country'] == 'India')])
plt.show()
