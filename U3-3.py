# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:51:05 2023

@author: 
"""

import pandas as pd # Modulen Pandas importeras 
import matplotlib.pyplot as plt #Modulen matplotlib importeras 


df_worldcities = pd.read_csv('worldcities.csv', sep = ';')
# Det första argumentet är filnamnet (sparat i working directory). Här används semikolon (;) som avgränsningstecken, vilket anges med det andra argumentet: sep=';'
    
df_worldcities['number_cities'] = df_worldcities.groupby('country')['country'].transform('count') #Ny kolumn "number_cities" (antal städer per land beräknas)
       
df_worldcities = df_worldcities[df_worldcities.groupby('country')['population'].transform('max') == df_worldcities['population']] #Dataframet uppdateras (av alla städer per land väljs den som har högst befolkningsmängd)

df_worldcities_sorterad = df_worldcities.sort_values(['number_cities'], ascending=[False]) #Dataframet sorteras enligt "number_cities" i fallande ordning, så att länder med störst antal städer hamnar uppe



df_worldcities_tio = df_worldcities_sorterad.head(10)[["country","number_cities", "city_ascii", "population"]] #De tio första länder av det sorterade data.framet (och kolumner av intresse) väljs 
df_worldcities_tio['population'] = df_worldcities_tio['population'].astype('int64') #Värden i kolumnen konverteras till int

print ("   Land \t\t\t\t\t Antal städer Största stad  Antal inv i största stad")
print ("-----------------------------------------------------------------------")
print(df_worldcities_tio.to_string(formatters={'country':'{{:<{}s}}'.format(df_worldcities_tio['country'].str.len().max()).format}, col_space = 16, index=False, header=False))
        #Data.framet skrivs ut som formatterat sträng


import numpy as np


fig, axes = plt.subplots(nrows=2, ncols=1, figsize = (8,8)) #De två stapeldiagrammen ska placeras över varandra (nrows=2, ncols=1)
df_worldcities_sorterad[["country", "number_cities"]].set_index("country").head(10).plot(ax=axes[0], kind='bar', width=0.7, grid=True) #Land som x-axel, antal länder som y-axel i den första digrammet
axes[0].legend().set_visible(False) #Den legend som visas by default tas bort
axes[0].set_title("Länder med flest antal städer", fontdict={'fontsize':8}) #Diagrammets titel
axes[0].set_ylabel("Antal städer", fontdict={'fontsize':7}) #Etikett på y-axel
axes[0].set_xlabel("Land", fontdict={'fontsize':7}) #Etikett på x-axel
axes[0].set_xticklabels(axes[0].get_xticklabels(),fontdict={'fontsize':7}) #Storlek av länderna (xticks)
y_ticks_cities = np.arange(0, 9000, 1000)  #y_ticks (och intervall) difinieras
axes[0].set_yticks(y_ticks_cities)
axes[0].set_yticklabels(y_ticks_cities, rotation=0, fontsize=7) #y_ticks formatteras
df_worldcities_sorterad[["city_ascii", "population"]].set_index("city_ascii").head(10).plot(ax=axes[1], kind='bar', width=0.7, grid=True) #Stad som x-axel, befolkning (för varje stad) som y-axel i den andra digrammet
axes[1].legend().set_visible(False) #Den legend som visas by default tas bort
axes[1].set_title("Den stärsta staden i respektive land", fontdict={'fontsize':8}) #Diagrammets titel
axes[1].set_ylabel('Antal invånare', fontdict={'fontsize':7}) #Etikett på y-axel
axes[1].set_xlabel("Stad", fontdict={'fontsize':7})  #Etikett på x-axel
axes[1].set_xticklabels(axes[1].get_xticklabels(),fontdict={'fontsize':7}) #Storlek av städerng(xticks)
y_ticks_popul = np.arange(0, 45000000, 5000000) #y_ticks (och intervall) difinieras
axes[1].set_yticks(y_ticks_popul)
axes[1].set_yticklabels(y_ticks_popul, rotation=0, fontsize=6) #y_ticks formatteras (OBS! Det går tyvärr inte att visas i scientific natation på y-axeln)
plt.tight_layout(); #Varje diagram får en lagom stor plats i ytan, så att allt information är synlig 
