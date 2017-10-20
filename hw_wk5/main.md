

```python
# Observed Trends
# Trend 1: Urban areas tend to have more rides and drivers
# Trend 2: Despite having less rides and drivers, Rural areas usually have higher rates
# Trend 3: Fare cost ranges based on city type, likely due to driver availability and distanc per trip
```


```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
```


```python
path_city = 'Resources/city_data.csv'
path_ride = 'Resources/ride_data.csv'

city_df = pd.read_csv(path_city)
ride_df = pd.read_csv(path_ride)
```


```python
merge_data = pd.merge(city_df,ride_df, on='city')
merge_data = merge_data.sort_values('city')


# Urban Calculations
urban = merge_data.loc[merge_data['type'] == 'Urban']
u_city = urban.groupby('city')
urban_ride_count = u_city['ride_id'].count()
urban_fare_total = u_city['fare'].sum()
urban_avg_ride = round(urban_fare_total / urban_ride_count,2)

# Suburban Calculations
suburban = merge_data.loc[merge_data['type'] == 'Suburban']
s_city = suburban.groupby('city')
sub_ride_count = s_city['ride_id'].count()
sub_fare_total = s_city['fare'].sum()
sub_avg_ride = round(sub_fare_total / sub_ride_count,2)

# Rural Calculations
rural = merge_data.loc[merge_data['type'] == 'Rural']
r_city = rural.groupby('city')
r_ride_count = r_city['ride_id'].count()
r_fare_total = r_city['fare'].sum()
r_avg_ride = round(r_fare_total / r_ride_count,2)

```

merge_data.head()


```python
u_x_axis = urban_ride_count
u_y_axis = urban_avg_ride
plt.scatter(u_x_axis, u_y_axis, marker = "o", facecolors="orange", edgecolors="black", 
            linewidth='1',s=city_df['driver_count']*5, alpha=0.70)

s_x_axis = sub_ride_count
s_y_axis = sub_avg_ride
plt.scatter(s_x_axis, s_y_axis, marker = "o", facecolors="dodgerblue", edgecolors="black",
            linewidth='1',s=city_df['driver_count']*5, alpha=0.70)

r_x_axis = r_ride_count
r_y_axis = r_avg_ride
plt.scatter(r_x_axis, r_y_axis, marker = "o", facecolors="yellow", edgecolors="black",
            linewidth='1',s=city_df['driver_count']*5, alpha=0.70)

plt.title("Pyber Ride Sharing Data (2016)")
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare ($)")

labels = city_df['type'].unique()
plt.legend(labels, loc="best")
plt.figtext(1,0.65,"Note:\nCircle size correlates with\ndriver count per city.")
plt.tight_layout()
plt.show()
```


![png](output_5_0.png)



```python
total_fair = merge_data['fare'].sum()
urban_total = merge_data.loc[merge_data['type'] == 'Urban']
u_total = round((urban_total['fare'].sum()/total_fair) * 100,1)

rural_total = merge_data.loc[merge_data['type'] == 'Rural']
r_total = round((rural_total['fare'].sum() / total_fair) * 100,1)

suburban_total = merge_data.loc[merge_data['type'] == 'Suburban']
s_total = round((suburban_total['fare'].sum() / total_fair) * 100,1)
colors = ["salmon", "skyblue", "gold"]
sizes = [u_total, r_total, s_total]
explode = (0.1,0,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors, autopct="%1.1f%%",shadow=True,startangle=240)
plt.axis("equal")
plt.title("% of Total Fares by City Type")
plt.show()
```


![png](output_6_0.png)



```python
total_rides = merge_data['ride_id'].count()

u_rides = round((urban_total['ride_id'].count()/total_rides) * 100,1)

r_rides = round((rural_total['ride_id'].count()/ total_rides) * 100,1)

s_rides = round((suburban_total['ride_id'].count()/ total_rides) * 100,1)

colors = ["salmon", "skyblue", "gold"]
sizes = [u_rides, r_rides, s_rides]
explode = (0.1,0,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors, autopct="%1.1f%%",shadow=True,startangle=240)
plt.axis("equal")
plt.title("% of Total Rides by City Type")
plt.show()
```


![png](output_7_0.png)



```python
u_drivers = city_df[city_df['type'] == 'Urban']['driver_count'].sum()
r_drivers = city_df[city_df['type'] == 'Rural']['driver_count'].sum()
s_drivers = city_df[city_df['type'] == 'Suburban']['driver_count'].sum()
total_drivers = u_drivers + r_drivers + s_drivers
u_drivers = round((u_drivers/total_drivers)*100,1)
r_drivers = round((r_drivers/total_drivers)*100,1)
s_drivers = round((s_drivers/total_drivers)*100,1)

colors = ["salmon", "skyblue", "gold"]
sizes = [u_drivers, r_drivers, s_drivers]
explode = (0.1,0,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors, autopct="%1.1f%%",shadow=True,startangle=225)
plt.axis("equal")
plt.title("% of Total Drivers by City Type")
plt.show()
```


![png](output_8_0.png)



```python

```
