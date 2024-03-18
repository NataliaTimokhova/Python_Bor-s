# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:37:55 2023

@author: 
"""

import pandas as pd # Modulen Pandas importeras 
import matplotlib.pyplot as plt #Modulen matplotlib importeras 


df_worldpubind  = pd.read_csv('worldpubind.csv', sep = ';')
#  #Filen 'worldpubind.csv' läsas in


popul_change = ((df_worldpubind["2021"] - df_worldpubind["1960"])/df_worldpubind["1960"])*100 #En ny kolumn skapas 'population_change' i data.framet
df_worldpubind['population_change'] = popul_change

 
sort_lagst_popul_change = df_worldpubind.sort_values(by = 'population_change', ascending = True) #data.framet sorteras enligt kolumnen "population_change" i ökande ordning
sort_lagst_popul_change_rent = sort_lagst_popul_change.dropna(subset=['population_change']) #De rader med bortfall i kolumnen 'population_change' väljs bort
popul_change_lagst = sort_lagst_popul_change_rent.head(5)[["Country Name","population_change"]] #De första 5 raderna av data.frame och kolumnerna av intresse väljs
popul_change_lagst['population_change'] = popul_change_lagst['population_change'].round(decimals = 2) #Värden i kolumnen "population_change" avrundas till 2 decimaler

sort_storst_popul_change = df_worldpubind.sort_values(by = 'population_change', ascending = False)  #data.framet sorteras enligt kolumnen "population_change" i fallande ordning
sort_storst_popul_change_rent = sort_storst_popul_change.dropna(subset=['population_change']) #Som ovan 
popul_change_storst = sort_storst_popul_change_rent.head(5)[["Country Name","population_change"]]  #Som ovan 
popul_change_storst['population_change'] = popul_change_storst['population_change'].round(decimals = 2)  #Som ovan 

concatenated_popul_change = pd.concat([popul_change_lagst, popul_change_storst], axis=0) #De två data.framen som skapades ovan sammanfogas till ett (axis=0, alltså matchas kolumnerna)
string_popul_change = concatenated_popul_change.to_string(formatters={"Country Name":'{{:<{}s}}'.format(concatenated_popul_change["Country Name"].str.len().max()).format}, col_space = 12, index=False, header=False) #Det sammanfogade data.framet konverteras till ett formaterat sträng
string_concatenated_popul_change = string_popul_change.splitlines() #konvertering to lista för att formattera tabellen nedan

print ("\t Befolkningsutvecklingen hos ett antal länder under åren 1960-2021") 
print ("Land \t\t\t\t\t\t  Befolkningsutveckling")
print (" \t\t\t\t\t\t\t mellan 1960 och 2021 [%]")
print ("-----------------------------------------------------------------------")
print("Länder där befolkningen minskar mest")
print(*string_concatenated_popul_change[0:5], sep = "\n") # De första 5 elementen av listan skrivs ut
print("Länder där befolkningen ökar mest")
print(*string_concatenated_popul_change[5:], sep = "\n") # De sista 5 elementen av listan skrivs ut
 
countries = popul_change_lagst["Country Name"] #Variabel till x-axeln
popchange = popul_change_lagst['population_change'] #Variabel till y-axel
fig = plt.figure(figsize = (8,4)) #En 800x400 figuryta initieras 
ax = fig.add_axes([0,0,1,1]) #Diagramobjektet ax inititeras 
ax.bar(countries, popchange, color=('blue', 'orange', 'darkgreen', 'red', 'purple')) #Utvalda länder (de första av den sorterade listan) som x-värden och deras befolkningsförädning som y-värden #Färger väljs
ax.set_title("Länder med minst och störst befolkhningsökning") #Diagrammets titel
ax.set_ylabel("Befolkningsökning (% av folkmängd)") #Etikett på y-label
plt.xticks(rotation=45) #Länderna roteras 45 grader
plt.grid()  #En grid skapas 
plt.show()
 
countries = popul_change_storst["Country Name"] #Variabel till x-axeln
popchange = popul_change_storst['population_change']  #Variabel till y-axel
fig = plt.figure(figsize = (8,4))         #En 800x400 figuryta initieras 
ax = fig.add_axes([0,0,1,1])       #Diagramobjektet ax inititeras 
ax.bar(countries, popchange, color=('blue', 'orange', 'darkgreen', 'red', 'purple')) #Utvalda länder (de första av den sorterade listan) som x-värden och deras befolkningsförädning som y-värden #Färger väljs
ax.set_title("Länder med minst och störst befolkhningsökning") #Diagrammets titel
ax.set_ylabel("Befolkningsökning (% av folkmängd)") #Etikett på y-label
plt.xticks(rotation=45)   #Länderna roteras 45 grader
plt.grid()   #En grid skapas 
plt.show()

# Uppgift b
svar = input("Skriv ett land: ")
# filtering the rows 

for ind, column in enumerate(df_worldpubind.iloc[:, 4:66].iloc[:, 1:].columns): #For-satsen löper igenom varje kolumn av intresse (befolkning i år 1960-2021, 62 kolumner totalt)
    df_worldpubind[f"{column}_procent_change"] = ((df_worldpubind.iloc[:, 4:66].iloc[:, ind+1] - df_worldpubind.iloc[:, 4:66].iloc[:, ind]) / df_worldpubind.iloc[:, 4:66].iloc[:, ind])*100
                          #61 nya kolumner skapas enligt formeln: ((antal_invånare_år_x – antal_invånare_år_x-1) / antal_invånare_år_x-1) *100
                          #Då skapas 61 nya kolumner (1961_procent_change till 2021_procent_change)
                          
df_worldpubind_transposed = df_worldpubind.set_index('Country Name').T #Dataframet blir transponerad, så att länderna blir kolumner
df_worldpubind_transposed.index = df_worldpubind_transposed.index.set_names('Year') #Nu sätts åren som den första kolumnen
df_worldpubind_transposed = df_worldpubind_transposed.reset_index() #och index blir 0 till 126 


import numpy as np


df_worldpubind_transposed.loc[65,:]=np.nan #Raden "population_change" (som inte  längre behövs) ersätts med en tom rad. 
                                           #Detta är nödvändigt, eftersom vi hade 62 rader (1960-2021) med befolkning, och 61 rader (1961-2021)
                                           #med befolkningsförädning. Då kan den tomma raden inkluderas för att få den önskade grafen nedan


import matplotlib.pyplot as plt


fig = plt.figure(figsize=(8,6)) # En 800x600 pixel figuryta initieras



year            = df_worldpubind_transposed.loc[3:64, 'Year'] #Rader 1960-2021 av kolumnen "Year" väljs som värden i x-axeln

population    = df_worldpubind_transposed.loc[3:64, svar] #De rader som motsvarar befolkningsmängd under 1960-2021 av kolumnen som motsvarar det valda landet väljs som den högra y-axeln

population_change = df_worldpubind_transposed.loc[65:, svar] #En NaN rad och de rader som motsvarar befolkningsföränding under 1961-2021 av kolumnen som motsvarar det valda landet väljs som den vänstra y-axeln


ax1 = fig.add_axes([0,0,1,1])   # Ett diagramobjekt 'ax1' skapas (vilket nyttjar den maximala figurytan)
ax1.plot(year, population_change, color = 'r', label = f'{svar} - befolkningsförändring')   # Befolkningsförädning plottas (vänstra y-axeln)
ax1.set_xlabel('År')                      # Etikett för x-axeln infogas
ax1.set_ylabel('befolkningsföränding', color='r')    # Etikett för den vänstra y-axeln infogas
ax1.tick_params(axis='y', labelcolor='r')  # Skalstrecken för vänstra y-axeln formatteras
ax1.legend(loc='upper left')               # Etikett i övre vänstra hörnet för befolkningförändring infogas
plt.grid(axis = "both")                    #En grid skapas 
# ---------------------------------------------------------------------------------------------------------------------

ax2 = ax1.twinx()                          # Här skapas den högra y-axeln. ett diagramobjekt ax2 skapas

# ---------------------------------------------------------------------------------------------------------------------

ax2.plot(year, population, color = 'b', label = f'{svar} - folkmängd')   # Folkmängden plottas (högra y-axeln)
ax2.set_ylabel('Folkmängd', color='b')     # Etikett för den vänstra y-axeln infogas
ax2.tick_params(axis='y', labelcolor='b')   # Skalstrecken för högra y-axeln formatteras
ax2.legend(loc='upper right')               # Etikett i övre högra hörnet för folkmängden infogas
plt.xticks(year[::10])                      # Bara var tionde år visas 
plt.show()
