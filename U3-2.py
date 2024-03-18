# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:55:52 2023

@author: 
"""
import pandas as pd # Modulen Pandas importeras 
import numpy as np #Modulen Numpy importeras 
import matplotlib.pyplot as plt # Modulen matplotlib importeras 

df_cia_factbook = pd.read_csv('cia_factbook.csv', sep = ';')  #Filen 'cia_factbook.csv' läsas in

density = df_cia_factbook["population"] / df_cia_factbook["area"] #Varje värde i kolumnen "population" divideras med respektive värde i kolumnen "area" för att skapa en ny kolumn "density"
df_cia_factbook['density'] = density                              #Den nya kolumnen skapas 
svar = input("Skriv ett land. Alternativt skriv antal länder (från 1 till 10), och + (för att få länder med störst befolkningstäthet) eller - (för länder med lägst befolkningstäthet), t ex 7+ eller 5-: ")
# Inmatningsraden, användaren får två olika alternativt, som sparas som "svar" 

try:    #I try-blocket kan koden generera en felsignal (ValueError, om användaren skriver fel information)
    if df_cia_factbook['country'].eq(svar).any(): #If-satsen: Om användaren väljer att skriva ett land, söks om landet finns i kolumn "country"
        land = df_cia_factbook[df_cia_factbook['country'].str.contains(svar)] #Landet sparas,
        landets_tathet = land["density"].to_string(index=False)            #och dess täthet extraheras from dataframet och sparas 
        print(f"Befolkningstäthet av {svar} är lika med {landets_tathet} inv/km2") #Landets täthet skrivs ut
    elif int(svar[:-1]) >= 1 and int(svar[:-1]) <= 10 and svar[-1] == '+':   #If-satsen sätter det alternativa villkoret att svaret börjar med en siffra från 1 till 10 och ett + tecken
        sort_list_storst = df_cia_factbook.sort_values(by = "density", ascending = False) #Dataframe sorteras enligt tätheten i fallande ordning, så att länder med största tätheten hamnar uppe 
        sort_list_storst.replace([np.inf], np.nan, inplace=True) #Inf ändras till NaN
        sort_list_storst_rent = sort_list_storst.dropna(subset=["density"])  #Rader med bortfall (NaN) i kolumn "density" väljs bort
        antal_lander_storst = int(svar[:-1])                                # Siffran väljs från strängen (som matades in) och konverteras till integer
        density_storst = sort_list_storst_rent.head(antal_lander_storst)["density"] #Ur det sorterade (och rensade) dataframet väljs de första raderna (antal länder som användaren vill ha) och kolumnen "density"
        countries_storst = sort_list_storst_rent.head(antal_lander_storst)["country"] #Sedan väljs kolumnen "country" (samt de första raderna, som ovan)                                                    #Länderna skrivs ut
        fig = plt.figure(figsize = (8,4)) #En 800x400 figuryta initieras 
        ax = fig.add_axes([0,0,1,1])      #Diagramobjektet ax initieras 
        ax.bar(countries_storst, density_storst)  #Utvalda länder (de första av den sorterad listan) som x-värden och deras täthet som y-värden
        ax.set_title("Länder med störst befolkhningstäthet") #Diagrammets titel
        ax.set_ylabel("Befolkningstäthet (inv/km2)") #Etikett på y-label
        plt.xticks(rotation=45)                      #Länderna i x-axeln (x-ticks) roteras 45 grader
        plt.grid()                                    #En grid skapas 
        plt.show()
    elif int(svar[:-1]) >= 1 and int(svar[:-1]) <= 10 and svar[-1] == '-': #Det alternativa villkoret att svaret innehåller ett "-" tecken sätts (och en siffra från 1 till 10, som ovan)
        sort_list_lagst = df_cia_factbook.sort_values(by = "density", ascending = True) #I detta fall sorteras dataframe i ökande ordning. Resten av koden fungerar på samma sätt som ovan, till länder med lägst täthet skrivs ut. 
        sort_list_lagst.replace([np.inf], np.nan, inplace=True)
        sort_list_lagst_rent = sort_list_lagst.dropna(subset=["density"]) 
        antal_lander_lagst = int(svar[:-1])
        density_lagst = sort_list_lagst_rent.head(antal_lander_lagst)["density"]
        countries_lagst = sort_list_lagst_rent.head(antal_lander_lagst)["country"]
        fig = plt.figure(figsize = (8,4)) 
        ax = fig.add_axes([0,0,1,1])      
        ax.bar(countries_lagst, density_lagst) #Stapeldiagrammet fungerar som ovan, men länder med lägst täthet väljs
        ax.set_title("Länder med lägst befolkhningstäthet") 
        ax.set_ylabel("Befolkningstäthet (inv/km2)")  
        plt.xticks(rotation=45)       
        plt.grid()                    
        plt.show()
    elif int(svar[:-1]) <= 0 or int(svar[:-1]) >= 10 or svar[-1] != "+" or svar[-1] != "-": #Ifall ett icke-acceptabellt nummer skrivs eller +/- tecken inte finns i svaret, ska instruktioner till avnändaren skrivas ut
        print("1 till maximum 10 länder är tillåtna (glom inte + eller - till slut). Vänligen försök igen")
except ValueError: #Except-blocket exekveras, om feltyp ValueError uppstår (t ex om användaren anger fel namn på land eller om hen skriver någonting annat än siffra)
    print("Skriv ett land med RÄTT stavning PÅ ENGELSKA. En lista med tillgängla länder i alfabetisk ordning finns nedan. Alternativt skriv ett NUMERISKT VÄRDE från 1-10 TILLSAMMANS MED ett +/- tecken")   #Extra instuktioner skrivs ut
    sorted_by_country_utan_nan = df_cia_factbook.sort_values(by = "country", ascending = True).dropna(subset=["density"]) #Dessutom väljs kolumnen "country", så att en lista med alla namn på engelska i alfabetisk ordning skrivs ut till användarens hjälp
    print(sorted_by_country_utan_nan["country"].to_string(index=False))
