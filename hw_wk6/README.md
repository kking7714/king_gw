

```python
# Observed Trends:
#     Trend 1: An apparent drop in city temperature occurs at 20 degrees latitude and continues to lower as latitude increases.
#     Trend 2: Based on the 500 random cities selected there is little to no correlation between latitude and other weather stats analyzed.
#     Trend 3: Querying a larger number of cities and aggregating more dates would likely provide better insight to latitude correlations of weather trends.

```


```python
import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import openweathermapy.core as ow
```


```python
# User provides API key 
api_key = input("Please enter your OpenWeather API key: ")
key = str(api_key)
settings = {"units":"imperial","appid":api_key}
#current date
d = datetime.datetime.today()
now = (d.strftime('%m/%d/%Y'))
```


```python
path = 'Resources/citipy-0.0.5/citipy/worldcities.csv'
world_cities = pd.read_csv(path)
world_cities_df = world_cities.reset_index()
world_cities_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>Country</th>
      <th>City</th>
      <th>Latitude</th>
      <th>Longitude</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>ad</td>
      <td>andorra la vella</td>
      <td>42.500000</td>
      <td>1.516667</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>ad</td>
      <td>canillo</td>
      <td>42.566667</td>
      <td>1.600000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>ad</td>
      <td>encamp</td>
      <td>42.533333</td>
      <td>1.583333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>ad</td>
      <td>la massana</td>
      <td>42.550000</td>
      <td>1.516667</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>ad</td>
      <td>les escaldes</td>
      <td>42.500000</td>
      <td>1.533333</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Replace with user selection later on while allowing no more then 500
rand_select = input("How many cities would you like to search? ")
user_rand = int(rand_select)
if user_rand > 500:
    user_rand = 500
    print("\nYou chose too many cities to search. We've defaulted your query to 500.")

# Selects a random sample of cities from the data frame
cities_ = world_cities_df['City'].sample(n=user_rand)
cities = cities_.reset_index()
```

    How many cities would you like to search? 500



```python
# API loop with randomly selected cities. Print processing log with city number, city name, and requested URL

results = [] #store response here
print("Beginning Data Retrieval")
num = 0
for city in cities['City']:
    try: 
        response = ow.get_current(city, **settings)
        results.append(response)
        num = num + 1
        print("------------------------")
        print("Processing " + str(num) + " of " + str(user_rand) + ": ")
        print("City ID: " + str(response['id']) + " | " + "City Name: " + response['name'])
        print("http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + key + "&q=" + city)
    except:
        print("------------------------\nUnable to find record, moving to next city...")


```

    Beginning Data Retrieval
    ------------------------
    Processing 1 of 500: 
    City ID: 3074598 | City Name: Jablonne nad Orlici
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=jablonne nad orlici
    ------------------------
    Processing 2 of 500: 
    City ID: 510911 | City Name: Pervomayskiy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pervomayskiy
    ------------------------
    Processing 3 of 500: 
    City ID: 5382514 | City Name: Piedmont
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=piedmont
    ------------------------
    Processing 4 of 500: 
    City ID: 294611 | City Name: Kafr Kama
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kafar kama
    ------------------------
    Processing 5 of 500: 
    City ID: 2745912 | City Name: Utrecht
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=utrecht
    ------------------------
    Processing 6 of 500: 
    City ID: 666674 | City Name: Slobozia-Campineanca
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=campineanca
    ------------------------
    Processing 7 of 500: 
    City ID: 3664243 | City Name: Feijo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=feijo
    ------------------------
    Processing 8 of 500: 
    City ID: 2015545 | City Name: Tarbagatay
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tarbagatay
    ------------------------
    Processing 9 of 500: 
    City ID: 4579484 | City Name: Gantt
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=gantt
    ------------------------
    Processing 10 of 500: 
    City ID: 2995652 | City Name: Marly-le-Roi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=marly-le-roi
    ------------------------
    Processing 11 of 500: 
    City ID: 1488741 | City Name: Tyumentsevo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tyumentsevo
    ------------------------
    Processing 12 of 500: 
    City ID: 3670754 | City Name: Riofrio
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=riofrio
    ------------------------
    Processing 13 of 500: 
    City ID: 2654710 | City Name: Brighton
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=brighton
    ------------------------
    Processing 14 of 500: 
    City ID: 628397 | City Name: Hlusha
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=spornoye
    ------------------------
    Processing 15 of 500: 
    City ID: 2619844 | City Name: Horve
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=horve
    ------------------------
    Processing 16 of 500: 
    City ID: 1277324 | City Name: Bangaon
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bangaon
    ------------------------
    Processing 17 of 500: 
    City ID: 3574724 | City Name: Couva
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=couva
    ------------------------
    Processing 18 of 500: 
    City ID: 6556319 | City Name: Oberhaching
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=oberhaching
    ------------------------
    Processing 19 of 500: 
    City ID: 4635031 | City Name: La Vergne
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=la vergne
    ------------------------
    Processing 20 of 500: 
    City ID: 1269805 | City Name: Ikauna
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ikauna
    ------------------------
    Processing 21 of 500: 
    City ID: 2792424 | City Name: Liedekerke
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=liedekerke
    ------------------------
    Processing 22 of 500: 
    City ID: 3181680 | City Name: Boscotrecase
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=boscotrecase
    ------------------------
    Processing 23 of 500: 
    City ID: 300640 | City Name: Sirnak
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sirnak
    ------------------------
    Processing 24 of 500: 
    City ID: 3616726 | City Name: San Juan del Sur
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=san juan del sur
    ------------------------
    Processing 25 of 500: 
    City ID: 493600 | City Name: Shudayag
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=shudayag
    ------------------------
    Processing 26 of 500: 
    City ID: 2634887 | City Name: Walkden
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=walkden
    ------------------------
    Processing 27 of 500: 
    City ID: 1687599 | City Name: Santor
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=santor
    ------------------------
    Processing 28 of 500: 
    City ID: 3471522 | City Name: Arinos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=arinos
    ------------------------
    Processing 29 of 500: 
    City ID: 2800042 | City Name: Court-Saint-Etienne
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=court-saint-etienne
    ------------------------
    Processing 30 of 500: 
    City ID: 575457 | City Name: Boguchar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=boguchar
    ------------------------
    Processing 31 of 500: 
    City ID: 1720806 | City Name: Calabaca
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=calabaca
    ------------------------
    Processing 32 of 500: 
    City ID: 3522804 | City Name: Naranjos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=naranjos
    ------------------------
    Processing 33 of 500: 
    City ID: 1586185 | City Name: Cao Bang
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cao bang
    ------------------------
    Processing 34 of 500: 
    City ID: 2264557 | City Name: Ponta do Sol
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ponta do sol
    ------------------------
    Processing 35 of 500: 
    City ID: 546672 | City Name: Kokhma
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kokhma
    ------------------------
    Processing 36 of 500: 
    City ID: 1489863 | City Name: Tayzhina
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tayzhina
    ------------------------
    Processing 37 of 500: 
    City ID: 4262318 | City Name: North Vernon
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=north vernon
    ------------------------
    Processing 38 of 500: 
    City ID: 2800328 | City Name: Chievres
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=chievres
    ------------------------
    Processing 39 of 500: 
    City ID: 3456827 | City Name: Monte Mor
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=monte mor
    ------------------------
    Processing 40 of 500: 
    City ID: 3461528 | City Name: Ibiuna
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ibiuna
    ------------------------
    Processing 41 of 500: 
    City ID: 4166776 | City Name: Ocoee
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ocoee
    ------------------------
    Processing 42 of 500: 
    City ID: 3133349 | City Name: Ulsteinvik
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ulsteinvik
    ------------------------
    Processing 43 of 500: 
    City ID: 3151917 | City Name: Honefoss
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=honefoss
    ------------------------
    Processing 44 of 500: 
    City ID: 674526 | City Name: Luica
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=luica
    ------------------------
    Processing 45 of 500: 
    City ID: 1090467 | City Name: Boueni
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=boueni
    ------------------------
    Processing 46 of 500: 
    City ID: 2963155 | City Name: Kinsale
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kinsale
    ------------------------
    Processing 47 of 500: 
    City ID: 1680125 | City Name: Valderrama
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=valderrama
    ------------------------
    Processing 48 of 500: 
    City ID: 5789826 | City Name: Chelan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cholan
    ------------------------
    Processing 49 of 500: 
    City ID: 3415212 | City Name: Kopavogur
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kopavogur
    ------------------------
    Processing 50 of 500: 
    City ID: 4987990 | City Name: Canton
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=canton
    ------------------------
    Processing 51 of 500: 
    City ID: 3692863 | City Name: Rioja
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=rioja
    ------------------------
    Processing 52 of 500: 
    City ID: 678490 | City Name: Faget
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=faget
    ------------------------
    Processing 53 of 500: 
    City ID: 2515692 | City Name: La Orotava
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=la orotava
    ------------------------
    Processing 54 of 500: 
    City ID: 1278943 | City Name: Alwar Tirunagari
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=alwar tirunagari
    ------------------------
    Processing 55 of 500: 
    City ID: 673397 | City Name: Mihail Eminescu
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mihail eminescu
    ------------------------
    Processing 56 of 500: 
    City ID: 2110743 | City Name: Tomobe
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tomobe
    ------------------------
    Processing 57 of 500: 
    City ID: 113636 | City Name: Tafresh
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ashtian
    ------------------------
    Processing 58 of 500: 
    City ID: 5964215 | City Name: Granby
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=granby
    ------------------------
    Processing 59 of 500: 
    City ID: 1691804 | City Name: Recodo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=recodo
    ------------------------
    Processing 60 of 500: 
    City ID: 2623394 | City Name: Broager
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=broager
    ------------------------
    Processing 61 of 500: 
    City ID: 751949 | City Name: Ardesen
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ardesen
    ------------------------
    Processing 62 of 500: 
    City ID: 3613394 | City Name: Cofradia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cofradia
    ------------------------
    Processing 63 of 500: 
    City ID: 2189947 | City Name: Himatangi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=himatangi
    ------------------------
    Processing 64 of 500: 
    City ID: 1268266 | City Name: Kaman
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kaman
    ------------------------
    Processing 65 of 500: 
    City ID: 3197862 | City Name: Kolut
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bezdan
    ------------------------
    Processing 66 of 500: 
    City ID: 662531 | City Name: Voineasa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=voineasa
    ------------------------
    Processing 67 of 500: 
    City ID: 787456 | City Name: Orahovac
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=orahovac
    ------------------------
    Processing 68 of 500: 
    City ID: 2112571 | City Name: Ishioka
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ishioka
    ------------------------
    Processing 69 of 500: 
    City ID: 3087705 | City Name: Pszczyna
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pszczyna
    ------------------------
    Processing 70 of 500: 
    City ID: 1708942 | City Name: Kaytitinga
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kaytitinga
    ------------------------
    Processing 71 of 500: 
    City ID: 1258292 | City Name: Raya
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=raya
    ------------------------
    Processing 72 of 500: 
    City ID: 3387663 | City Name: Sertania
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sertania
    ------------------------
    Processing 73 of 500: 
    City ID: 3048627 | City Name: Magocs
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=magocs
    ------------------------
    Processing 74 of 500: 
    City ID: 4989133 | City Name: Clinton
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=clinton
    ------------------------
    Processing 75 of 500: 
    City ID: 3684510 | City Name: El Cocuy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=el cocuy
    ------------------------
    Processing 76 of 500: 
    City ID: 2519477 | City Name: Chipiona
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=chipiona
    ------------------------
    Processing 77 of 500: 
    City ID: 2112232 | City Name: Kitaibaraki
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kitaibaraki
    ------------------------
    Processing 78 of 500: 
    City ID: 4004647 | City Name: Huatabampo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=huatabampo
    ------------------------
    Processing 79 of 500: 
    City ID: 2524819 | City Name: Enna
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=enna
    ------------------------
    Processing 80 of 500: 
    City ID: 2661842 | City Name: Affoltern am Albis
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=affoltern
    ------------------------
    Processing 81 of 500: 
    City ID: 3392020 | City Name: Pio IX
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pio ix
    ------------------------
    Processing 82 of 500: 
    City ID: 2509650 | City Name: Vicar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=vicar
    ------------------------
    Processing 83 of 500: 
    City ID: 4328010 | City Name: Houma
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=houma
    ------------------------
    Processing 84 of 500: 
    City ID: 4853423 | City Name: Davenport
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=davenport
    ------------------------
    Processing 85 of 500: 
    City ID: 2619845 | City Name: Horuphav
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=horuphav
    ------------------------
    Processing 86 of 500: 
    City ID: 4992635 | City Name: Ferndale
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ferndale
    ------------------------
    Processing 87 of 500: 
    City ID: 3882582 | City Name: Loncoche
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=loncoche
    ------------------------
    Processing 88 of 500: 
    City ID: 1688859 | City Name: San Nicolas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=san nicolas
    ------------------------
    Processing 89 of 500: 
    City ID: 1274784 | City Name: Chandannagar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=chandannagar
    ------------------------
    Processing 90 of 500: 
    City ID: 3924679 | City Name: Vilhena
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=vilhena
    ------------------------
    Processing 91 of 500: 
    City ID: 6452007 | City Name: Villemomble
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=villemomble
    ------------------------
    Processing 92 of 500: 
    City ID: 2744042 | City Name: Zandvoort
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=zandvoort
    ------------------------
    Processing 93 of 500: 
    City ID: 677896 | City Name: Francesti
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=francesti
    ------------------------
    Processing 94 of 500: 
    City ID: 1253372 | City Name: Vasai
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=vasai
    ------------------------
    Processing 95 of 500: 
    City ID: 1215502 | City Name: Banda Aceh
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=banda aceh
    ------------------------
    Processing 96 of 500: 
    City ID: 576093 | City Name: Blagoyevo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=blagoyevo
    ------------------------
    Processing 97 of 500: 
    City ID: 3166262 | City Name: Spilimbergo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=spilimbergo
    ------------------------
    Processing 98 of 500: 
    City ID: 3471683 | City Name: Arcos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=arcos
    ------------------------
    Processing 99 of 500: 
    City ID: 1717520 | City Name: Cayungnan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cayungnan
    ------------------------
    Processing 100 of 500: 
    City ID: 680332 | City Name: Craiova
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=craiova
    ------------------------
    Processing 101 of 500: 
    City ID: 666126 | City Name: Stanceni
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=stanceni
    ------------------------
    Processing 102 of 500: 
    City ID: 615921 | City Name: Akhaldaba
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=akhaldaba
    ------------------------
    Processing 103 of 500: 
    City ID: 510442 | City Name: Pesochnoye
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pesochnoye
    ------------------------
    Processing 104 of 500: 
    City ID: 3637623 | City Name: Lagunillas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=lagunillas
    ------------------------
    Processing 105 of 500: 
    City ID: 2276492 | City Name: Harper
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=harper
    ------------------------
    Processing 106 of 500: 
    City ID: 2088143 | City Name: Porgera
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=laiagam
    ------------------------
    Processing 107 of 500: 
    City ID: 2281951 | City Name: Sassandra
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sassandra
    ------------------------
    Processing 108 of 500: 
    City ID: 2965535 | City Name: Cavan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cavan
    ------------------------
    Processing 109 of 500: 
    City ID: 246522 | City Name: Tibnah
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tibnah
    ------------------------
    Processing 110 of 500: 
    City ID: 695205 | City Name: Rudne
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=russkoye
    ------------------------
    Processing 111 of 500: 
    City ID: 4017144 | City Name: Bermejillo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bermejillo
    ------------------------
    Processing 112 of 500: 
    City ID: 5511077 | City Name: Reno
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=reno
    ------------------------
    Processing 113 of 500: 
    City ID: 1734599 | City Name: Kuala Kangsar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sungai pelek
    ------------------------
    Processing 114 of 500: 
    City ID: 3515358 | City Name: Tlaxcalancingo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tlaxcalancingo
    ------------------------
    Processing 115 of 500: 
    City ID: 3979819 | City Name: Zacualpan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=zacualpan
    ------------------------
    Processing 116 of 500: 
    City ID: 1852347 | City Name: Shimodate
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=shimodate
    ------------------------
    Processing 117 of 500: 
    City ID: 3395458 | City Name: Maragogi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=maragogi
    ------------------------
    Processing 118 of 500: 
    City ID: 1064980 | City Name: Fenoarivo Atsinanana
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=fenoarivo atsinanana
    ------------------------
    Processing 119 of 500: 
    City ID: 2351979 | City Name: Agbor
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=agbor
    ------------------------
    Processing 120 of 500: 
    City ID: 3020839 | City Name: Drancy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=drancy
    ------------------------
    Processing 121 of 500: 
    City ID: 1707513 | City Name: Langub
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=langub
    ------------------------
    Processing 122 of 500: 
    City ID: 1708724 | City Name: Kinalansan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kinalansan
    ------------------------
    Processing 123 of 500: 
    City ID: 2034754 | City Name: Shunyi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=shunyi
    ------------------------
    Processing 124 of 500: 
    City ID: 674933 | City Name: Lechinta
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=lechinta
    ------------------------
    Processing 125 of 500: 
    City ID: 3400541 | City Name: Exu
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=exu
    ------------------------
    Processing 126 of 500: 
    City ID: 1527121 | City Name: Tyup
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tyup
    ------------------------
    Processing 127 of 500: 
    City ID: 204283 | City Name: Watsa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=watsa
    ------------------------
    Processing 128 of 500: 
    City ID: 7844372 | City Name: Cibadak
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cibadak
    ------------------------
    Processing 129 of 500: 
    City ID: 676819 | City Name: Gradistea
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=gradistea
    ------------------------
    Processing 130 of 500: 
    City ID: 2699791 | City Name: Koping
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=koping
    ------------------------
    Processing 131 of 500: 
    City ID: 1220253 | City Name: Istaravshan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=uroteppa
    ------------------------
    Processing 132 of 500: 
    City ID: 3447212 | City Name: Suzano
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=suzano
    ------------------------
    Processing 133 of 500: 
    City ID: 3523559 | City Name: Mariano Escobedo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mariano escobedo
    ------------------------
    Processing 134 of 500: 
    City ID: 3429732 | City Name: Puerto Rico
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=puerto rico
    ------------------------
    Processing 135 of 500: 
    City ID: 3589770 | City Name: San Mateo Ixtatan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=san mateo ixtatan
    ------------------------
    Processing 136 of 500: 
    City ID: 2243940 | City Name: Ziguinchor
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ziguinchor
    ------------------------
    Processing 137 of 500: 
    City ID: 694992 | City Name: Rzhyshchiv
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=rzhyshchiv
    ------------------------
    Processing 138 of 500: 
    City ID: 684980 | City Name: Berveni
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=berveni
    ------------------------
    Processing 139 of 500: 
    City ID: 1723313 | City Name: Bugasong
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bugasong
    ------------------------
    Processing 140 of 500: 
    City ID: 5148326 | City Name: Brook Park
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=brook park
    ------------------------
    Processing 141 of 500: 
    City ID: 3561408 | City Name: El Cobre
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=el cobre
    ------------------------
    Processing 142 of 500: 
    City ID: 1692746 | City Name: Prosperidad
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=prosperidad
    ------------------------
    Processing 143 of 500: 
    City ID: 1260685 | City Name: Pallikondai
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pallikonda
    ------------------------
    Processing 144 of 500: 
    City ID: 1266029 | City Name: Kotaparh
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kotaparh
    ------------------------
    Processing 145 of 500: 
    City ID: 4756643 | City Name: Dumfries
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dumfries
    ------------------------
    Processing 146 of 500: 
    City ID: 3166714 | City Name: Seravezza
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=seravezza
    ------------------------
    Processing 147 of 500: 
    City ID: 1705540 | City Name: Los Arcos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=los arcos
    ------------------------
    Processing 148 of 500: 
    City ID: 671390 | City Name: Panet
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=panet
    ------------------------
    Processing 149 of 500: 
    City ID: 3001402 | City Name: Les Clayes-sous-Bois
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=les clayes-sous-bois
    ------------------------
    Processing 150 of 500: 
    City ID: 4470244 | City Name: Havelock
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=havelock
    ------------------------
    Processing 151 of 500: 
    City ID: 3190586 | City Name: Slavonski Brod
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=brod
    ------------------------
    Processing 152 of 500: 
    City ID: 6074099 | City Name: Millet
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=millet
    ------------------------
    Processing 153 of 500: 
    City ID: 6147353 | City Name: Sicamous
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sicamous
    ------------------------
    Processing 154 of 500: 
    City ID: 4467485 | City Name: Fuquay-Varina
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=fuquay-varina
    ------------------------
    Processing 155 of 500: 
    City ID: 1253330 | City Name: Vedaraniyam
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=vedaranniyam
    ------------------------
    Processing 156 of 500: 
    City ID: 569639 | City Name: Chegem
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=chegem
    ------------------------
    Processing 157 of 500: 
    City ID: 1567621 | City Name: Son Tay
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=son tay
    ------------------------
    Processing 158 of 500: 
    City ID: 3468720 | City Name: Buritizeiro
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=buritizeiro
    ------------------------
    Processing 159 of 500: 
    City ID: 4903024 | City Name: Mount Prospect
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mount prospect
    ------------------------
    Processing 160 of 500: 
    City ID: 2263049 | City Name: Serpa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=serpa
    ------------------------
    Processing 161 of 500: 
    City ID: 2184512 | City Name: Pleasant Point
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pleasant point
    ------------------------
    Processing 162 of 500: 
    City ID: 1256126 | City Name: Singtam
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=singtam
    ------------------------
    Processing 163 of 500: 
    City ID: 1225142 | City Name: Valvedditturai
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=valvedditturai
    ------------------------
    Processing 164 of 500: 
    City ID: 1623223 | City Name: Trucuk
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=trucuk
    ------------------------
    Processing 165 of 500: 
    City ID: 6174151 | City Name: Victoriaville
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=victoriaville
    ------------------------
    Processing 166 of 500: 
    City ID: 2737393 | City Name: Moreira de Conegos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=moreira de conegos
    ------------------------
    Processing 167 of 500: 
    City ID: 3584348 | City Name: Moncagua
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=moncagua
    ------------------------
    Processing 168 of 500: 
    City ID: 2312249 | City Name: Mushie
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mushie
    ------------------------
    Processing 169 of 500: 
    City ID: 3393783 | City Name: Novo Oriente
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=novo oriente
    ------------------------
    Processing 170 of 500: 
    City ID: 142554 | City Name: Hashtrud
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=hashtrud
    ------------------------
    Processing 171 of 500: 
    City ID: 471160 | City Name: Voznesenye
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=voznesenye
    ------------------------
    Processing 172 of 500: 
    City ID: 3057691 | City Name: Senica
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=senica
    ------------------------
    Processing 173 of 500: 
    City ID: 4945283 | City Name: Newton
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=newton
    ------------------------
    Processing 174 of 500: 
    City ID: 2742661 | City Name: Arvore
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=arvore
    ------------------------
    Processing 175 of 500: 
    City ID: 3654410 | City Name: Manta
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=manta
    ------------------------
    Processing 176 of 500: 
    City ID: 3385850 | City Name: Uirauna
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=uirauna
    ------------------------
    Processing 177 of 500: 
    City ID: 1854703 | City Name: Ogaki
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ogaki
    ------------------------
    Processing 178 of 500: 
    City ID: 7287492 | City Name: Volketswil
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=volketswil
    ------------------------
    Processing 179 of 500: 
    City ID: 2265914 | City Name: Monte Gordo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=monte gordo
    ------------------------
    Processing 180 of 500: 
    City ID: 686113 | City Name: Arsura
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=arsura
    ------------------------
    Processing 181 of 500: 
    City ID: 6174041 | City Name: Victoria
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=victoria
    ------------------------
    Processing 182 of 500: 
    City ID: 680690 | City Name: Coroisanmartin
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=coroisanmartin
    ------------------------
    Processing 183 of 500: 
    City ID: 658225 | City Name: Helsinki
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pousat
    ------------------------
    Processing 184 of 500: 
    City ID: 1709478 | City Name: Kampokpok
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=butason
    ------------------------
    Processing 185 of 500: 
    City ID: 2017705 | City Name: Poyarkovo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=poyarkovo
    ------------------------
    Processing 186 of 500: 
    City ID: 2518040 | City Name: El Viso del Alcor
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=el viso del alcor
    ------------------------
    Processing 187 of 500: 
    City ID: 3183284 | City Name: Alghero
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=alghero
    ------------------------
    Processing 188 of 500: 
    City ID: 510342 | City Name: Pestretsy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pestretsy
    ------------------------
    Processing 189 of 500: 
    City ID: 1255634 | City Name: Srinagar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=srinagar
    ------------------------
    Processing 190 of 500: 
    City ID: 667420 | City Name: Selimbar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=selimbar
    ------------------------
    Processing 191 of 500: 
    City ID: 2025630 | City Name: Chara
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=chara
    ------------------------
    Processing 192 of 500: 
    City ID: 2931521 | City Name: Eisenberg
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=eisenberg
    ------------------------
    Processing 193 of 500: 
    City ID: 478132 | City Name: Ust-Donetskiy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ust-donetskiy
    ------------------------
    Processing 194 of 500: 
    City ID: 1279062 | City Name: Alanganallur
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=alanganallur
    ------------------------
    Processing 195 of 500: 
    City ID: 1729351 | City Name: Buadtasan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=badtasan
    ------------------------
    Processing 196 of 500: 
    City ID: 663098 | City Name: Vatra Moldovitei
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=vatra moldovitei
    ------------------------
    Processing 197 of 500: 
    City ID: 3038638 | City Name: Agde
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=agde
    ------------------------
    Processing 198 of 500: 
    City ID: 601084 | City Name: Alytus
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=alytus
    ------------------------
    Processing 199 of 500: 
    City ID: 4170617 | City Name: Royal Palm Beach
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=royal palm beach
    ------------------------
    Processing 200 of 500: 
    City ID: 4215391 | City Name: Perry
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=perry
    ------------------------
    Processing 201 of 500: 
    City ID: 1655124 | City Name: Muang Phon-Hong
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=phonhong
    ------------------------
    Processing 202 of 500: 
    City ID: 3169539 | City Name: Recco
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=recco
    ------------------------
    Processing 203 of 500: 
    City ID: 2577162 | City Name: Gaoua
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=gaoua
    ------------------------
    Processing 204 of 500: 
    City ID: 2012646 | City Name: Zarubino
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=zarubino
    ------------------------
    Processing 205 of 500: 
    City ID: 665087 | City Name: Timisoara
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=timisoara
    ------------------------
    Processing 206 of 500: 
    City ID: 792767 | City Name: Belcista
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=belcista
    ------------------------
    Processing 207 of 500: 
    City ID: 2784199 | City Name: Waimes
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=waimes
    ------------------------
    Processing 208 of 500: 
    City ID: 3386264 | City Name: Toritama
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=toritama
    ------------------------
    Processing 209 of 500: 
    City ID: 1271306 | City Name: Ghazipur
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ghazipur
    ------------------------
    Processing 210 of 500: 
    City ID: 2454955 | City Name: Kolokani
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kolokani
    ------------------------
    Processing 211 of 500: 
    City ID: 3666409 | City Name: Uribia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=uribia
    ------------------------
    Processing 212 of 500: 
    City ID: 1736302 | City Name: Jitra
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=jitra
    ------------------------
    Processing 213 of 500: 
    City ID: 575343 | City Name: Bolokhovo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bolokhovo
    ------------------------
    Processing 214 of 500: 
    City ID: 686449 | City Name: Almasu
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=almasu
    ------------------------
    Processing 215 of 500: 
    City ID: 1260014 | City Name: Pavagada
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pavagada
    ------------------------
    Processing 216 of 500: 
    City ID: 1226992 | City Name: Taralanda
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=matale
    ------------------------
    Processing 217 of 500: 
    City ID: 183027 | City Name: Nyahururu
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=nyahururu
    ------------------------
    Processing 218 of 500: 
    City ID: 3685533 | City Name: Cucuta
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cucuta
    ------------------------
    Processing 219 of 500: 
    City ID: 1687894 | City Name: Santa Rosa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=santa rosa
    ------------------------
    Processing 220 of 500: 
    City ID: 713126 | City Name: Auly
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=auly
    ------------------------
    Processing 221 of 500: 
    City ID: 1259231 | City Name: Pundri
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pundri
    ------------------------
    Processing 222 of 500: 
    City ID: 1726602 | City Name: Barongis
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=barongis
    ------------------------
    Processing 223 of 500: 
    City ID: 3667773 | City Name: Suarez
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=suarez
    ------------------------
    Processing 224 of 500: 
    City ID: 5391811 | City Name: San Diego
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=san diego
    ------------------------
    Processing 225 of 500: 
    City ID: 1502073 | City Name: Krasnosel’kup
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=krasnoselkup
    ------------------------
    Processing 226 of 500: 
    City ID: 4346991 | City Name: Adelphi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=adelphi
    ------------------------
    Processing 227 of 500: 
    City ID: 5102369 | City Name: Palisades Park
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=palisades park
    ------------------------
    Processing 228 of 500: 
    City ID: 190544 | City Name: Konza
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=konza
    ------------------------
    Processing 229 of 500: 
    City ID: 665691 | City Name: Suseni
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=suseni
    ------------------------
    Processing 230 of 500: 
    City ID: 1337612 | City Name: Dhidhdhoo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dhidhdhoo
    ------------------------
    Processing 231 of 500: 
    City ID: 3400920 | City Name: Elesbao Veloso
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=elesbao veloso
    ------------------------
    Processing 232 of 500: 
    City ID: 5009586 | City Name: Shelby
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=shelby
    ------------------------
    Processing 233 of 500: 
    City ID: 2650839 | City Name: Dudley
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dudley
    ------------------------
    Processing 234 of 500: 
    City ID: 677479 | City Name: Ghelinta
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ghelinta
    ------------------------
    Processing 235 of 500: 
    City ID: 709078 | City Name: Frunze
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=frunze
    ------------------------
    Processing 236 of 500: 
    City ID: 6454424 | City Name: Trélon
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=liniere
    ------------------------
    Processing 237 of 500: 
    City ID: 3012649 | City Name: Issy-les-Moulineaux
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=issy-les-moulineaux
    ------------------------
    Processing 238 of 500: 
    City ID: 2647349 | City Name: Hatfield
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=hatfield
    ------------------------
    Processing 239 of 500: 
    City ID: 697624 | City Name: Perove
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=perove
    ------------------------
    Processing 240 of 500: 
    City ID: 2385836 | City Name: Préfecture de la Kémo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dekoa
    ------------------------
    Processing 241 of 500: 
    City ID: 261150 | City Name: Kandila
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kandila
    ------------------------
    Processing 242 of 500: 
    City ID: 3674962 | City Name: Medellin
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=medellin
    ------------------------
    Processing 243 of 500: 
    City ID: 2971117 | City Name: Valbonne
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=valbonne
    ------------------------
    Processing 244 of 500: 
    City ID: 3673386 | City Name: Paicol
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=paicol
    ------------------------
    Processing 245 of 500: 
    City ID: 255229 | City Name: Pyrgos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pirgos
    ------------------------
    Processing 246 of 500: 
    City ID: 3165420 | City Name: Torre Santa Susanna
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=torre santa susanna
    ------------------------
    Processing 247 of 500: 
    City ID: 3659544 | City Name: Celica
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=celica
    ------------------------
    Processing 248 of 500: 
    City ID: 191038 | City Name: Kitui
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kitui
    ------------------------
    Processing 249 of 500: 
    City ID: 1181611 | City Name: Chaman
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=chaman
    ------------------------
    Processing 250 of 500: 
    City ID: 2714903 | City Name: Finspang
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=finspang
    ------------------------
    Processing 251 of 500: 
    City ID: 3979982 | City Name: Yahualica
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=yahualica
    ------------------------
    Processing 252 of 500: 
    City ID: 785013 | City Name: Topola
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=topola
    ------------------------
    Processing 253 of 500: 
    City ID: 6550659 | City Name: Spremberg
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=spremberg
    ------------------------
    Processing 254 of 500: 
    City ID: 2659099 | City Name: Rapperswil
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=rapperswil
    ------------------------
    Processing 255 of 500: 
    City ID: 3687025 | City Name: Caucasia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=caucasia
    ------------------------
    Processing 256 of 500: 
    City ID: 256808 | City Name: Monastirakion
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=monastirakion
    ------------------------
    Processing 257 of 500: 
    City ID: 5932143 | City Name: Creemore
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=creemore
    ------------------------
    Processing 258 of 500: 
    City ID: 3089125 | City Name: Piekary Slaskie
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=piekary slaskie
    ------------------------
    Processing 259 of 500: 
    City ID: 894701 | City Name: Bulawayo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bulawayo
    ------------------------
    Processing 260 of 500: 
    City ID: 665628 | City Name: Taga
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=taga
    ------------------------
    Processing 261 of 500: 
    City ID: 5392900 | City Name: Santa Ana
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=santa ana
    ------------------------
    Processing 262 of 500: 
    City ID: 2509553 | City Name: Villanueva de la Serena
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=villanueva de la serena
    ------------------------
    Processing 263 of 500: 
    City ID: 6930918 | City Name: Atala
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=auala
    ------------------------
    Processing 264 of 500: 
    City ID: 1705424 | City Name: Lubigan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=lubigan
    ------------------------
    Processing 265 of 500: 
    City ID: 1271052 | City Name: Gola Bazar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=gola bazar
    ------------------------
    Processing 266 of 500: 
    City ID: 3687964 | City Name: Calarca
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=calarca
    ------------------------
    Processing 267 of 500: 
    City ID: 3974771 | City Name: Praxedis Guerrero
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=praxedis guerrero
    ------------------------
    Processing 268 of 500: 
    City ID: 2027109 | City Name: Barguzin
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=barguzin
    ------------------------
    Processing 269 of 500: 
    City ID: 3610789 | City Name: El Plan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=el plan
    ------------------------
    Processing 270 of 500: 
    City ID: 2510271 | City Name: Torre-Pacheco
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=torre-pacheco
    ------------------------
    Processing 271 of 500: 
    City ID: 2647178 | City Name: Helensburgh
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=helensburgh
    ------------------------
    Processing 272 of 500: 
    City ID: 3801262 | City Name: Isla Soyaltepec
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=soyaltepec
    ------------------------
    Processing 273 of 500: 
    City ID: 5955902 | City Name: Fort Nelson
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=fort nelson
    ------------------------
    Processing 274 of 500: 
    City ID: 3946177 | City Name: Calca
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=calca
    ------------------------
    Processing 275 of 500: 
    City ID: 478996 | City Name: Uni
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=uni
    ------------------------
    Processing 276 of 500: 
    City ID: 314903 | City Name: Foca
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=foca
    ------------------------
    Processing 277 of 500: 
    City ID: 4290988 | City Name: Elizabethtown
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=elizabethtown
    ------------------------
    Processing 278 of 500: 
    City ID: 2652586 | City Name: Coleraine
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=coleraine
    ------------------------
    Processing 279 of 500: 
    City ID: 217695 | City Name: Bunia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bunia
    ------------------------
    Processing 280 of 500: 
    City ID: 3592086 | City Name: Ocos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ocos
    ------------------------
    Processing 281 of 500: 
    City ID: 1726994 | City Name: Bantilan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bantilan
    ------------------------
    Processing 282 of 500: 
    City ID: 2610760 | City Name: Vamdrup
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=vamdrup
    ------------------------
    Processing 283 of 500: 
    City ID: 3447589 | City Name: Silvania
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=silvania
    ------------------------
    Processing 284 of 500: 
    City ID: 5115107 | City Name: Dix Hills
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dix hills
    ------------------------
    Processing 285 of 500: 
    City ID: 155187 | City Name: Makanya
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=makanya
    ------------------------
    Processing 286 of 500: 
    City ID: 667873 | City Name: Satu Mare
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=satu mare
    ------------------------
    Processing 287 of 500: 
    City ID: 674426 | City Name: Lunca Cernii de Jos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=lunca cernii de jos
    ------------------------
    Processing 288 of 500: 
    City ID: 521123 | City Name: Nizhneivkino
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=nizhneivkino
    ------------------------
    Processing 289 of 500: 
    City ID: 681510 | City Name: Cislau
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cislau
    ------------------------
    Processing 290 of 500: 
    City ID: 2035754 | City Name: Mingyue
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mingyue
    ------------------------
    Processing 291 of 500: 
    City ID: 473778 | City Name: Vidnoye
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=vidnoye
    ------------------------
    Processing 292 of 500: 
    City ID: 5188236 | City Name: Economy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=economy
    ------------------------
    Processing 293 of 500: 
    City ID: 533916 | City Name: Loyga
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=loyga
    ------------------------
    Processing 294 of 500: 
    City ID: 5345529 | City Name: El Cajon
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=el cajon
    ------------------------
    Processing 295 of 500: 
    City ID: 2523920 | City Name: Palermo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=palermo
    ------------------------
    Processing 296 of 500: 
    City ID: 3159894 | City Name: Brumunddal
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=brumunddal
    ------------------------
    Processing 297 of 500: 
    City ID: 1253986 | City Name: Udaipur
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=udaipur
    ------------------------
    Processing 298 of 500: 
    City ID: 555681 | City Name: Itum-Kali
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=itum-kale
    ------------------------
    Processing 299 of 500: 
    City ID: 4726206 | City Name: San Antonio
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=san antonio
    ------------------------
    Processing 300 of 500: 
    City ID: 5326297 | City Name: Barstow
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=barstow
    ------------------------
    Processing 301 of 500: 
    City ID: 370457 | City Name: Maridi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=maridi
    ------------------------
    Processing 302 of 500: 
    City ID: 4761054 | City Name: Glen Allen
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=glen allen
    ------------------------
    Processing 303 of 500: 
    City ID: 3012621 | City Name: Ivry-sur-Seine
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ivry-sur-seine
    ------------------------
    Processing 304 of 500: 
    City ID: 262159 | City Name: Gaitanion
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=gaitanion
    ------------------------
    Processing 305 of 500: 
    City ID: 3188635 | City Name: Turanj
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pagman
    ------------------------
    Processing 306 of 500: 
    City ID: 2514197 | City Name: Manises
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=manises
    ------------------------
    Processing 307 of 500: 
    City ID: 1608539 | City Name: Nakhon Nayok
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=nakhon nayok
    ------------------------
    Processing 308 of 500: 
    City ID: 352628 | City Name: Matay
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=matay
    ------------------------
    Processing 309 of 500: 
    City ID: 3893726 | City Name: Constitucion
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=constitucion
    ------------------------
    Processing 310 of 500: 
    City ID: 666989 | City Name: Sanmihaiu Almasului
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sanmihaiul-almasului
    ------------------------
    Processing 311 of 500: 
    City ID: 4155996 | City Name: Fort Myers Beach
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=fort myers beach
    ------------------------
    Processing 312 of 500: 
    City ID: 3602603 | City Name: Salama
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=salama
    ------------------------
    Processing 313 of 500: 
    City ID: 723470 | City Name: Strazske
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=strazske
    ------------------------
    Processing 314 of 500: 
    City ID: 4945121 | City Name: New Bedford
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=new bedford
    ------------------------
    Processing 315 of 500: 
    City ID: 782756 | City Name: Korce
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=korce
    ------------------------
    Processing 316 of 500: 
    City ID: 675385 | City Name: Izvoarele
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=izvoarele
    ------------------------
    Processing 317 of 500: 
    City ID: 1703020 | City Name: Malasila
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=malasila
    ------------------------
    Processing 318 of 500: 
    City ID: 3448596 | City Name: Sao Lourenco do Sul
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sao lourenco do sul
    ------------------------
    Processing 319 of 500: 
    City ID: 3399679 | City Name: Feira Nova
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=feira nova
    ------------------------
    Processing 320 of 500: 
    City ID: 3515431 | City Name: Tlalnepantla
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tlalnepantla
    ------------------------
    Processing 321 of 500: 
    City ID: 3002984 | City Name: Le Pecq
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=le pecq
    ------------------------
    Processing 322 of 500: 
    City ID: 569615 | City Name: Chekalin
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=chekalin
    ------------------------
    Processing 323 of 500: 
    City ID: 2773304 | City Name: Kuchl
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kuchl
    ------------------------
    Processing 324 of 500: 
    City ID: 3018074 | City Name: Fontainebleau
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=fontainebleau
    ------------------------
    Processing 325 of 500: 
    City ID: 5400075 | City Name: Sunnyvale
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sunnyvale
    ------------------------
    Processing 326 of 500: 
    City ID: 694273 | City Name: Shchors
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=shchors
    ------------------------
    Processing 327 of 500: 
    City ID: 1491219 | City Name: Sovetskoye
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sovetskoye
    ------------------------
    Processing 328 of 500: 
    City ID: 3583090 | City Name: Suchitoto
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=suchitoto
    ------------------------
    Processing 329 of 500: 
    City ID: 3601899 | City Name: San Marcos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=san francisco de ojuera
    ------------------------
    Processing 330 of 500: 
    City ID: 1717103 | City Name: Columbio
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=columbio
    ------------------------
    Processing 331 of 500: 
    City ID: 3406545 | City Name: Balsas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=balsas
    ------------------------
    Processing 332 of 500: 
    City ID: 257056 | City Name: Mykonos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mikonos
    ------------------------
    Processing 333 of 500: 
    City ID: 2856639 | City Name: Osterburg
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=osterburg
    ------------------------
    Processing 334 of 500: 
    City ID: 2960800 | City Name: Belvaux
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=belvaux
    ------------------------
    Processing 335 of 500: 
    City ID: 4844309 | City Name: Torrington
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=torrington
    ------------------------
    Processing 336 of 500: 
    City ID: 3056683 | City Name: Vrutky
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=vrutky
    ------------------------
    Processing 337 of 500: 
    City ID: 676634 | City Name: Grozesti
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=grozesti
    ------------------------
    Processing 338 of 500: 
    City ID: 3195930 | City Name: Mahala
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=breza
    ------------------------
    Processing 339 of 500: 
    City ID: 4101241 | City Name: Benton
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=benton
    ------------------------
    Processing 340 of 500: 
    City ID: 1700282 | City Name: Matiompong
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=matiompong
    ------------------------
    Processing 341 of 500: 
    City ID: 519336 | City Name: Velikiy Novgorod
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=velikiy novgorod
    ------------------------
    Processing 342 of 500: 
    City ID: 2268250 | City Name: Ferreiras
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ferreiras
    ------------------------
    Processing 343 of 500: 
    City ID: 704885 | City Name: Korostyshiv
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=korostyshiv
    ------------------------
    Processing 344 of 500: 
    City ID: 5105957 | City Name: Waldwick
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=waldwick
    ------------------------
    Processing 345 of 500: 
    City ID: 519690 | City Name: Novaya Gollandiya
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sinkat
    ------------------------
    Processing 346 of 500: 
    City ID: 1265053 | City Name: Lar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=lar
    ------------------------
    Processing 347 of 500: 
    City ID: 2013952 | City Name: Ust-Ilimsk
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ust-ilimsk
    ------------------------
    Processing 348 of 500: 
    City ID: 179330 | City Name: Thika
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=thika
    ------------------------
    Processing 349 of 500: 
    City ID: 3199017 | City Name: Izola
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=izola
    ------------------------
    Processing 350 of 500: 
    City ID: 2953358 | City Name: Bad Salzuflen
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bad salzuflen
    ------------------------
    Processing 351 of 500: 
    City ID: 616056 | City Name: Yeranos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tazagyukh
    ------------------------
    Processing 352 of 500: 
    City ID: 4014553 | City Name: Chapala
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=chapala
    ------------------------
    Processing 353 of 500: 
    City ID: 3020021 | City Name: Epinay-sur-Orge
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=epinay-sur-orge
    ------------------------
    Processing 354 of 500: 
    City ID: 6162949 | City Name: Terrace
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=terrace
    ------------------------
    Processing 355 of 500: 
    City ID: 1785462 | City Name: Zaoyang
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=zaoyang
    ------------------------
    Processing 356 of 500: 
    City ID: 3518138 | City Name: San Pablo Autopan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=autopan
    ------------------------
    Processing 357 of 500: 
    City ID: 897456 | City Name: Sinazongwe
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sinazongwe
    ------------------------
    Processing 358 of 500: 
    City ID: 1618205 | City Name: Ban Khlong Phae
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=wiset chai chan
    ------------------------
    Processing 359 of 500: 
    City ID: 2398929 | City Name: Mbigou
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mbigou
    ------------------------
    Processing 360 of 500: 
    City ID: 3620390 | City Name: Chichigalpa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=chichigalpa
    ------------------------
    Processing 361 of 500: 
    City ID: 3628503 | City Name: San Carlos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=san carlos
    ------------------------
    Processing 362 of 500: 
    City ID: 603303 | City Name: Robertsfors
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sikea
    ------------------------
    Processing 363 of 500: 
    City ID: 1815456 | City Name: Changzhou
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=changzhou
    ------------------------
    Processing 364 of 500: 
    City ID: 1275971 | City Name: Bhilai
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bhilai
    ------------------------
    Processing 365 of 500: 
    City ID: 7626370 | City Name: Falkhytta
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=aukra
    ------------------------
    Processing 366 of 500: 
    City ID: 1508517 | City Name: Bystryy Istok
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bystryy istok
    ------------------------
    Processing 367 of 500: 
    City ID: 3911925 | City Name: La Paz
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=la paz
    ------------------------
    Processing 368 of 500: 
    City ID: 3028263 | City Name: Castres
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=castres
    ------------------------
    Processing 369 of 500: 
    City ID: 263471 | City Name: Bendevís
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=iraklion
    ------------------------
    Processing 370 of 500: 
    City ID: 4153132 | City Name: Delray Beach
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=delray beach
    ------------------------
    Processing 371 of 500: 
    City ID: 518209 | City Name: Novoselitskoye
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=novoselitskoye
    ------------------------
    Processing 372 of 500: 
    City ID: 3455161 | City Name: Para de Minas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=para de minas
    ------------------------
    Processing 373 of 500: 
    City ID: 258091 | City Name: Louros
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=louros
    ------------------------
    Processing 374 of 500: 
    City ID: 2514301 | City Name: Mao
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mao
    ------------------------
    Processing 375 of 500: 
    City ID: 1275321 | City Name: Bongaigaon
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bongaigaon
    ------------------------
    Processing 376 of 500: 
    City ID: 3588726 | City Name: Sipacapa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sipacapa
    ------------------------
    Processing 377 of 500: 
    City ID: 2786318 | City Name: Spa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=spa
    ------------------------
    Processing 378 of 500: 
    City ID: 663950 | City Name: Valcau de Jos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=valcau de jos
    ------------------------
    Processing 379 of 500: 
    City ID: 3991253 | City Name: Purepero
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=purepero
    ------------------------
    Processing 380 of 500: 
    City ID: 366426 | City Name: Tandalti
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tandalti
    ------------------------
    Processing 381 of 500: 
    City ID: 1701150 | City Name: Maragondon
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=maragondon
    ------------------------
    Processing 382 of 500: 
    City ID: 5015599 | City Name: Wyandotte
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=wyandotte
    ------------------------
    Processing 383 of 500: 
    City ID: 2658904 | City Name: Saanen
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=saanen
    ------------------------
    Processing 384 of 500: 
    City ID: 1688954 | City Name: San Miguel
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=san miguel
    ------------------------
    Processing 385 of 500: 
    City ID: 2110541 | City Name: Yamoto
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=yamoto
    ------------------------
    Processing 386 of 500: 
    City ID: 3604835 | City Name: Mezapa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mezapa
    ------------------------
    Processing 387 of 500: 
    City ID: 1807687 | City Name: Huaicheng
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=huaicheng
    ------------------------
    Processing 388 of 500: 
    City ID: 2155862 | City Name: Nambour
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=nambour
    ------------------------
    Processing 389 of 500: 
    City ID: 5509952 | City Name: Paradise
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=paradise
    ------------------------
    Processing 390 of 500: 
    City ID: 3133402 | City Name: Ulefoss
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ulefoss
    ------------------------
    Processing 391 of 500: 
    City ID: 765749 | City Name: Lukow
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=lukow
    ------------------------
    Processing 392 of 500: 
    City ID: 3543299 | City Name: Puerto Padre
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=puerto padre
    ------------------------
    Processing 393 of 500: 
    City ID: 3451121 | City Name: Rio Negro
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=rio negro
    ------------------------
    Processing 394 of 500: 
    City ID: 1730307 | City Name: Apud
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=apud
    ------------------------
    Processing 395 of 500: 
    City ID: 5334928 | City Name: Castro Valley
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=castro valley
    ------------------------
    Processing 396 of 500: 
    City ID: 514460 | City Name: Osinovo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=osinovo
    ------------------------
    Processing 397 of 500: 
    City ID: 3466704 | City Name: Castro
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=castro
    ------------------------
    Processing 398 of 500: 
    City ID: 4256426 | City Name: Dale
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dale
    ------------------------
    Processing 399 of 500: 
    City ID: 673632 | City Name: Mediesu Aurit
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mediesu aurit
    ------------------------
    Processing 400 of 500: 
    City ID: 4815462 | City Name: Moundsville
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=moundsville
    ------------------------
    Processing 401 of 500: 
    City ID: 3531674 | City Name: Cancuc
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cancuc
    ------------------------
    Processing 402 of 500: 
    City ID: 663197 | City Name: Varasti
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=varasti
    ------------------------
    Processing 403 of 500: 
    City ID: 3459452 | City Name: Junqueiropolis
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dracena
    ------------------------
    Processing 404 of 500: 
    City ID: 2636005 | City Name: Thornaby-on-Tees
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=thornaby
    ------------------------
    Processing 405 of 500: 
    City ID: 5164390 | City Name: New Philadelphia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=new philadelphia
    ------------------------
    Processing 406 of 500: 
    City ID: 3575039 | City Name: Arouca
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=arouca
    ------------------------
    Processing 407 of 500: 
    City ID: 256879 | City Name: Mithymna
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mithimna
    ------------------------
    Processing 408 of 500: 
    City ID: 1709593 | City Name: Calumboyan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=calumboyan
    ------------------------
    Processing 409 of 500: 
    City ID: 1695383 | City Name: Pangao
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pangao
    ------------------------
    Processing 410 of 500: 
    City ID: 1708301 | City Name: Labnig
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=labnig
    ------------------------
    Processing 411 of 500: 
    City ID: 483692 | City Name: Temizhbekskaya
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=temizhbekskaya
    ------------------------
    Processing 412 of 500: 
    City ID: 680342 | City Name: Craidorolt
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=craidorolt
    ------------------------
    Processing 413 of 500: 
    City ID: 3432043 | City Name: La Plata
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=la plata
    ------------------------
    Processing 414 of 500: 
    City ID: 691469 | City Name: Tokmak
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tokmak
    ------------------------
    Processing 415 of 500: 
    City ID: 5321473 | City Name: Winslow
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=winslow
    ------------------------
    Processing 416 of 500: 
    City ID: 3600057 | City Name: Zopilotepe
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=zopilotepe
    ------------------------
    Processing 417 of 500: 
    City ID: 3051657 | City Name: Harta
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=harta
    ------------------------
    Processing 418 of 500: 
    City ID: 1167528 | City Name: Quetta
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=quetta
    ------------------------
    Processing 419 of 500: 
    City ID: 675215 | City Name: Jirlau
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=jirlau
    ------------------------
    Processing 420 of 500: 
    City ID: 3617694 | City Name: Matiguas
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=matiguas
    ------------------------
    Processing 421 of 500: 
    City ID: 712969 | City Name: Bakhchysaray
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bakhchysaray
    ------------------------
    Processing 422 of 500: 
    City ID: 3457697 | City Name: Marilandia
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=marilandia
    ------------------------
    Processing 423 of 500: 
    City ID: 3514440 | City Name: Xochistlahuaca
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=xochistlahuaca
    ------------------------
    Processing 424 of 500: 
    City ID: 1708234 | City Name: Lacag
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=lacag
    ------------------------
    Processing 425 of 500: 
    City ID: 1684491 | City Name: Tagbina
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tagbina
    ------------------------
    Processing 426 of 500: 
    City ID: 3404833 | City Name: Brejo Santo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=brejo santo
    ------------------------
    Processing 427 of 500: 
    City ID: 1715655 | City Name: Dansuli
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dansuli
    ------------------------
    Processing 428 of 500: 
    City ID: 3390326 | City Name: Ribeirao
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ribeirao
    ------------------------
    Processing 429 of 500: 
    City ID: 3395336 | City Name: Maribondo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=maribondo
    ------------------------
    Processing 430 of 500: 
    City ID: 949703 | City Name: Thaba Nchu
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=thaba nchu
    ------------------------
    Processing 431 of 500: 
    City ID: 2995150 | City Name: Maubeuge
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=maubeuge
    ------------------------
    Processing 432 of 500: 
    City ID: 1717569 | City Name: Cayanguan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cayangwan
    ------------------------
    Processing 433 of 500: 
    City ID: 3045341 | City Name: Simontornya
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=simontornya
    ------------------------
    Processing 434 of 500: 
    City ID: 3072781 | City Name: Kremze
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kremze
    ------------------------
    Processing 435 of 500: 
    City ID: 1260064 | City Name: Patrasaer
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kushmurun
    ------------------------
    Processing 436 of 500: 
    City ID: 672118 | City Name: Oancea
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=oancea
    ------------------------
    Processing 437 of 500: 
    City ID: 2876282 | City Name: Lohfelden
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=lohfelden
    ------------------------
    Processing 438 of 500: 
    City ID: 689945 | City Name: Verenchanka
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=verenchanka
    ------------------------
    Processing 439 of 500: 
    City ID: 555994 | City Name: Ishcherskaya
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ishcherskaya
    ------------------------
    Processing 440 of 500: 
    City ID: 1709039 | City Name: Kauswagan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kauswagan
    ------------------------
    Processing 441 of 500: 
    City ID: 1278667 | City Name: Anantnag
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=anantnag
    ------------------------
    Processing 442 of 500: 
    City ID: 2988507 | City Name: Paris
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=paris
    ------------------------
    Processing 443 of 500: 
    City ID: 3176746 | City Name: Forli
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=forli
    ------------------------
    Processing 444 of 500: 
    City ID: 6540649 | City Name: Suzzara
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=suzzara
    ------------------------
    Processing 445 of 500: 
    City ID: 3860259 | City Name: Cordoba
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=cordoba
    ------------------------
    Processing 446 of 500: 
    City ID: 2872126 | City Name: Meitingen
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=meitingen
    ------------------------
    Processing 447 of 500: 
    City ID: 2517111 | City Name: Granadilla de Abona
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=granadilla de abona
    ------------------------
    Processing 448 of 500: 
    City ID: 1272861 | City Name: Dhari
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dhari
    ------------------------
    Processing 449 of 500: 
    City ID: 1684364 | City Name: Tagoytoy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=tagoytoy
    ------------------------
    Processing 450 of 500: 
    City ID: 502903 | City Name: Rameshki
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=rameshki
    ------------------------
    Processing 451 of 500: 
    City ID: 575480 | City Name: Bogovarovo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bogovarovo
    ------------------------
    Processing 452 of 500: 
    City ID: 1805753 | City Name: Jinan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=jinan
    ------------------------
    Processing 453 of 500: 
    City ID: 1172389 | City Name: Lakhi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=lakhi
    ------------------------
    Processing 454 of 500: 
    City ID: 2744675 | City Name: Westervoort
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=westervoort
    ------------------------
    Processing 455 of 500: 
    City ID: 1700618 | City Name: Maslog
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=maslog
    ------------------------
    Processing 456 of 500: 
    City ID: 3172253 | City Name: Nizza Monferrato
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=nizza monferrato
    ------------------------
    Processing 457 of 500: 
    City ID: 3516497 | City Name: Suchiate
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=suchiate
    ------------------------
    Processing 458 of 500: 
    City ID: 4991640 | City Name: East Lansing
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=east lansing
    ------------------------
    Processing 459 of 500: 
    City ID: 1283617 | City Name: Bhaktapur
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bhaktapur
    ------------------------
    Processing 460 of 500: 
    City ID: 3587587 | City Name: Zacapa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=zacapa
    ------------------------
    Processing 461 of 500: 
    City ID: 3607294 | City Name: Langue
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=langue
    ------------------------
    Processing 462 of 500: 
    City ID: 3164028 | City Name: Vittorio Veneto
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=vittorio veneto
    ------------------------
    Processing 463 of 500: 
    City ID: 5356868 | City Name: Highland
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=highland
    ------------------------
    Processing 464 of 500: 
    City ID: 1725157 | City Name: Binalbagan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=binalbagan
    ------------------------
    Processing 465 of 500: 
    City ID: 675407 | City Name: Izbiceni
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=izbiceni
    ------------------------
    Processing 466 of 500: 
    City ID: 514966 | City Name: Orichi
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=orichi
    ------------------------
    Processing 467 of 500: 
    City ID: 3470059 | City Name: Bernardino de Campos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=bernardino de campos
    ------------------------
    Processing 468 of 500: 
    City ID: 3130616 | City Name: Alcala de Henares
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=alcala de henares
    ------------------------
    Processing 469 of 500: 
    City ID: 597231 | City Name: Marijampole
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=marijampole
    ------------------------
    Processing 470 of 500: 
    City ID: 2640729 | City Name: Oxford
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=oxford
    ------------------------
    Processing 471 of 500: 
    City ID: 1708859 | City Name: Kiblawan
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=kiblawan
    ------------------------
    Processing 472 of 500: 
    City ID: 700159 | City Name: Mykolayivka
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mykolayivka
    ------------------------
    Processing 473 of 500: 
    City ID: 1259939 | City Name: Pehowa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=pehowa
    ------------------------
    Processing 474 of 500: 
    City ID: 2015913 | City Name: Suntar
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=suntar
    ------------------------
    Processing 475 of 500: 
    City ID: 1702032 | City Name: Manay
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=manay
    ------------------------
    Processing 476 of 500: 
    City ID: 149703 | City Name: Sumbawanga
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sumbawanga
    ------------------------
    Processing 477 of 500: 
    City ID: 464891 | City Name: Zapadnaya Dvina
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=zapadnaya dvina
    ------------------------
    Processing 478 of 500: 
    City ID: 2433055 | City Name: Dourbali
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dourbali
    ------------------------
    Processing 479 of 500: 
    City ID: 583573 | City Name: Russkiy Aktash
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=russkiy aktash
    ------------------------
    Processing 480 of 500: 
    City ID: 2784555 | City Name: Virton
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=virton
    ------------------------
    Processing 481 of 500: 
    City ID: 3589913 | City Name: San Juan Cotzal
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=san juan cotzal
    ------------------------
    Processing 482 of 500: 
    City ID: 1064275 | City Name: Ihosy
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ihosy
    ------------------------
    Processing 483 of 500: 
    City ID: 567748 | City Name: Chufarovo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=chufarovo
    ------------------------
    Processing 484 of 500: 
    City ID: 3449319 | City Name: Sao Carlos
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sao carlos
    ------------------------
    Processing 485 of 500: 
    City ID: 4755158 | City Name: Dale City
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=dale city
    ------------------------
    Processing 486 of 500: 
    City ID: 3516050 | City Name: Temascalapa
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=temascalapa
    ------------------------
    Processing 487 of 500: 
    City ID: 1256340 | City Name: Sihora
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sihora
    ------------------------
    Processing 488 of 500: 
    City ID: 1255491 | City Name: Sultanpur
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sultanpur
    ------------------------
    Processing 489 of 500: 
    City ID: 1253080 | City Name: Vriddhachalam
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=ulundurpettai
    ------------------------
    Processing 490 of 500: 
    City ID: 4346788 | City Name: Zachary
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=zachary
    ------------------------
    Processing 491 of 500: 
    City ID: 1263255 | City Name: Mayang Imphal
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=mayang imphal
    ------------------------
    Processing 492 of 500: 
    City ID: 731384 | City Name: Godech
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=godec
    ------------------------
    Processing 493 of 500: 
    City ID: 4167545 | City Name: Palm Harbor
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=crystal beach
    ------------------------
    Processing 494 of 500: 
    City ID: 3449476 | City Name: Santo Augusto
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=santo augusto
    ------------------------
    Processing 495 of 500: 
    City ID: 532675 | City Name: Lysva
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=lysva
    ------------------------
    Processing 496 of 500: 
    City ID: 3903987 | City Name: Sucre
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sucre
    ------------------------
    Processing 497 of 500: 
    City ID: 2657030 | City Name: Arnold
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=arnold
    ------------------------
    Processing 498 of 500: 
    City ID: 556463 | City Name: Imeni Vorovskogo
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=imeni vorovskogo
    ------------------------
    Processing 499 of 500: 
    City ID: 2831088 | City Name: Sonthofen
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=sonthofen
    ------------------------
    Processing 500 of 500: 
    City ID: 2618415 | City Name: Koge
    http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=5c054ddbd58eca2ada6575729a0313df&q=koge



```python
#retrieve relevant weather info
temp_max = [data.get("main").get("temp_max") for data in results]
humid = [data.get("main").get("humidity") for data in results]
cloud = [data.get("clouds").get("all") for data in results]
wind = [data.get("wind").get("speed") for data in results]

#retrieve location information
name = [data.get("name") for data in results]
country = [data.get("sys").get("country") for data in results]
lat = [data.get("coord").get("lat") for data in results]
lon = [data.get("coord").get("lon") for data in results]
date = [data.get("dt") for data in results]

# create dictionary with results
wx_dict = {"City":name,"Cloudiness":cloud,"Country":country,
           "Date":date,"Humidity":humid,"Lat":lat,"Lon":lon,
           "Max Temp":temp_max, "Wind Speed":wind}
# create dataframe
city_wx_df = pd.DataFrame(wx_dict)
```


```python
city_wx_df.to_csv('city_weather.csv')
city_wx_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Cloudiness</th>
      <th>Country</th>
      <th>Date</th>
      <th>Humidity</th>
      <th>Lat</th>
      <th>Lon</th>
      <th>Max Temp</th>
      <th>Wind Speed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Jablonne nad Orlici</td>
      <td>75</td>
      <td>CZ</td>
      <td>1508871600</td>
      <td>100</td>
      <td>50.03</td>
      <td>16.60</td>
      <td>48.20</td>
      <td>1.12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pervomayskiy</td>
      <td>68</td>
      <td>RU</td>
      <td>1508873827</td>
      <td>78</td>
      <td>53.25</td>
      <td>40.29</td>
      <td>23.06</td>
      <td>3.60</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Piedmont</td>
      <td>20</td>
      <td>US</td>
      <td>1508871480</td>
      <td>22</td>
      <td>37.82</td>
      <td>-122.23</td>
      <td>87.80</td>
      <td>16.11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Kafr Kama</td>
      <td>0</td>
      <td>IL</td>
      <td>1508871000</td>
      <td>64</td>
      <td>32.72</td>
      <td>35.44</td>
      <td>71.60</td>
      <td>3.36</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Utrecht</td>
      <td>75</td>
      <td>NL</td>
      <td>1508873100</td>
      <td>88</td>
      <td>52.09</td>
      <td>5.12</td>
      <td>62.60</td>
      <td>19.46</td>
    </tr>
  </tbody>
</table>
</div>




```python
temp_df = city_wx_df.sort_values('Max Temp', ascending=False)
temp_range = temp_df['Max Temp']
```


```python
#City Latitude vs. Max Temperature
fig = plt.figure(figsize=(10,8))
plt.scatter(city_wx_df['Lat'], city_wx_df['Max Temp'])
plt.grid()
plt.title("City Latitude vs. Max Temperature " + "(" + now +")") 
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (F)")
plt.show()
fig.savefig('Temp_vs_Lat.png')
```


![png](output_9_0.png)



```python
#City Latitude vs. Humidity
fig = plt.figure(figsize=(10,8))
plt.scatter(city_wx_df['Lat'], city_wx_df['Humidity'], color='cornflowerblue')
plt.grid()
plt.title("City Latitude vs. Humidity " + "(" + now +")") 
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.show()
fig.savefig('Humidity_vs_Lat.png')
```


![png](output_10_0.png)



```python
#City Latitude vs. Cloudiness
fig = plt.figure(figsize=(10,8))
plt.scatter(city_wx_df['Lat'], city_wx_df['Cloudiness'],color='lightskyblue')
plt.grid()
plt.title("City Latitude vs. Cloudiness " + "(" + now +")") 
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")
plt.show()
fig.savefig('Cloudiness_vs_Lat.png')
```


![png](output_11_0.png)



```python
#City Latitude vs. Wind Speed
fig = plt.figure(figsize=(10,8))
plt.scatter(city_wx_df['Lat'], city_wx_df['Wind Speed'],color='steelblue')
plt.grid()
plt.title("City Latitude vs. Wind Speed " + "(" + now +")") 
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")
plt.show()
fig.savefig('WindSpeed_vs_Lat.png')
```


![png](output_12_0.png)



```python

```
