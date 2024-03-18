# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 00:35:15 2023

@author: 
"""

import pandas as pd # Modulen Pandas importeras 
import matplotlib.pyplot as plt # Modulen matplotlib importeras 

df_cia_factbook = pd.read_csv('cia_factbook.csv', sep = ';')  #Filen 'cia_factbook.csv' läsas in


def meny():        # En funktion #meny" definieras (menyprogram med 4 olika alternativ) 
    while(True): # En while-sats tillämpas och ska avbrytas (break) efter val 4 (då programmet avslutas)
        
        print ('1. Tabell med land, area, antal fddslar, och livslängd ') # Val som presenteras i text 
        print ('2. Länder med lägst och störst antal internetanvändare per 100.000 invånare')
        print ("3. Länder med minst och störst befolkhningsökning")
        print ('4. Avsluta programmet')
        print

        val = int(input('Välj menyalternativ (1-4): ')) # Välj alternativ 

    
        if val == 1: #Om det första valet görs, ska det land (eller de länder) som uppfyller uppgiftens kriterier skrivas ut

            #alt 1
            medel_befolkning = df_cia_factbook["population"].mean()  #medelvärdet av den valda kolumnen "population"
            medel_area = df_cia_factbook["area"].mean()              #medelvärdet av den valda kolumnen "area"
            df_cia_factbook_rent = df_cia_factbook.dropna(subset=["area", "birth_rate", "life_exp_at_birth"]) #Rader med bortfall i variabler (kolumner) av intresse väljs bort
            
            filt = (df_cia_factbook_rent["population"] > medel_befolkning) & (df_cia_factbook_rent["area"] < medel_area) & (df_cia_factbook_rent["birth_rate"] <= 24) & (df_cia_factbook_rent["birth_rate"] >= 15) & (df_cia_factbook_rent["life_exp_at_birth"] > 70)
                          # Olika villkor sätts enligt uppgiftens instruktioner. De rader som uppfyller villkoren sparas som "filt"
            resultat = df_cia_factbook_rent.loc[filt, ["country", "area", "birth_rate", "life_exp_at_birth"]]
                      # En ny data.frame "resultat" skapas, som innehåller alla rader och kolumner av intresse 
            resultat[["area", "birth_rate", "life_exp_at_birth"]] = resultat[["area", "birth_rate", "life_exp_at_birth"]].astype('int64')
            
            print ("  Land \t\t\t\t Area \t\t\t  Antal fädslar Livslängd")
            print (" \t\t\t\t\t [km2]\t\t\t  [per 100 inv] [år]")
            print ("  ------------------------------------------------------------------")
            print(resultat.to_string(formatters={'country':'{{:<{}s}}'.format(resultat['country'].str.len().max()).format}, col_space = 13, index=False, header=False))
                         #En formatterad tabell skrivs ut

        elif val == 2: #Om det andra valet görs, ska länder med lägst och störst antal internetanvändare per 100.000 invånare

            #alt 2
            internet_density = df_cia_factbook["internet_users"] * (100000/df_cia_factbook["population"]) #En ny kolumn skapas 'internet_users_density' i data.framet 
            df_cia_factbook['internet_users_density'] = internet_density                                  
             
            sort_lagst = df_cia_factbook.sort_values(by = "internet_users_density", ascending = True) #data.framet sorteras enligt kolumnen 'internet_users_density' i ökande ordning
            sort_lagst_rent = sort_lagst.dropna(subset=["internet_users_density"]) #De rader med bortfall i kolumnen 'internet_users_density' väljs bort
            countries_int_lagst = sort_lagst_rent.head(5)[["country","population", "internet_users_density"]] #De första 5 raderna av data.frame och kolumnerna av intresse väljs
            countries_int_lagst['population'] = countries_int_lagst['population'].astype('int64') #Kolumnen population konverteras till int, så att den onödiga decimalen (.0) inte skrivs ut 
            countries_int_lagst['internet_users_density'] = countries_int_lagst['internet_users_density'].round(decimals = 1) #Värden i kolumnen 'internet_users_density' avrundas
             
            sort_storst = df_cia_factbook.sort_values(by = "internet_users_density", ascending = False)  #data.framet sorteras enligt kolumnen 'internet_users_density' i fallande ordning
            sort_storst_rent = sort_storst.dropna(subset=["internet_users_density"]) #Som ovan 
            countries_int_storst = sort_storst_rent.head(5)[["country","population", "internet_users_density"]] #Som ovan 
            countries_int_storst['population'] = countries_int_storst['population'].astype('int64')    #Som ovan 
            countries_int_storst['internet_users_density'] = countries_int_storst['internet_users_density'].round(decimals = 1)   #Som ovan 
             
            concatenated = pd.concat([countries_int_lagst, countries_int_storst], axis=0) #De två data.framen som skapades ovan sammanfogas till ett 
            string = concatenated.to_string(formatters={'country':'{{:<{}s}}'.format(concatenated['country'].str.len().max()).format}, col_space = 10, index=False, header=False) #Det sammanfogade data.framet konverteras till ett formaterat sträng
            string_concatenated = string.splitlines() #Stränget konverteras till listan (varje rad utgör ett separat element) för att lättare kunna formatera tabellen senare

            print ("Land \t\t\t\t\t Folkmängd \t\t\t Antal internetanvändare")
            print (" \t\t\t\t\t\t\t\t\t\t\t [per 100000 inv] ")
            print ("--------------------------------------------------------------------")
            print("Länder med lägst antal internetanvändare per 100.000 invånare")
            print(*string_concatenated[0:5], sep = "\n")    # De första 5 elementen av listan skrivs ut
            print("Länder med störst antal internetanvändare per 100.000 invånare")
            print(*string_concatenated[5:], sep = "\n")  # De sista 5 elementen av listan skrivs ut

            
        elif val == 3: 

            #alt 3
            popul_growth_rate = df_cia_factbook["birth_rate"] - df_cia_factbook["death_rate"] + df_cia_factbook["net_migration_rate"] #En ny kolumn 'population_growth_rate' skapas i data.framet
            df_cia_factbook['population_growth_rate'] = popul_growth_rate
            df_cia_factbook['population_change'] = df_cia_factbook['population_growth_rate']/10  #En ny kolumn 'population_growth_rate' skapas i data.framet
            
            sort_lagst_popchange = df_cia_factbook.sort_values(by = 'population_change', ascending = True) #data.framet sorteras enligt kolumnen 'population_change' i ökande ordning
            sort_lagst_popchange_rent = sort_lagst_popchange.dropna(subset=['population_change']) #De rader med bortfall i kolumnen 'population_change' väljs bort
            countries_popchange_lagst = sort_lagst_popchange_rent.head(5)[["country","birth_rate", "death_rate", "net_migration_rate", "population_change"]] #De första 5 raderna av data.frame och kolumnerna av intresse väljs
            countries_popchange_lagst["birth_rate"] = countries_popchange_lagst["birth_rate"].astype('int64') #Värden i kolumnen konverteras till int
            countries_popchange_lagst["death_rate"] = countries_popchange_lagst["death_rate"].astype('int64') #Värden i kolumnen konverteras till int
            countries_popchange_lagst["net_migration_rate"] = countries_popchange_lagst["net_migration_rate"].astype('int64') #Värden i kolumnen konverteras till int
            countries_popchange_lagst['population_change'] = countries_popchange_lagst['population_change'].round(decimals = 2) #Värden i kolumen avrundas
            
            sort_storst_popchange = df_cia_factbook.sort_values(by = 'population_change', ascending = False) #data.framet sorteras enligt kolumnen 'population_change' i fallande ordning
            sort_storst_popchange_rent = sort_storst_popchange.dropna(subset=['population_change']) #Som ovan
            countries_popchange_storst = sort_storst_popchange_rent.head(5)[["country","birth_rate", "death_rate", "net_migration_rate", "population_change"]] #Som ovan
            countries_popchange_storst["birth_rate"] = countries_popchange_storst["birth_rate"].astype('int64') #Som ovan
            countries_popchange_storst["death_rate"] = countries_popchange_storst["death_rate"].astype('int64') #Som ovan
            countries_popchange_storst["net_migration_rate"] = countries_popchange_storst["net_migration_rate"].astype('int64') #Som ovan
            countries_popchange_storst['population_change'] = countries_popchange_storst['population_change'].round(decimals = 2) #Som ovan
            
            concatenated_popchange = pd.concat([countries_popchange_lagst, countries_popchange_storst], axis=0) #De två data.framen som skapades ovan sammanfogas till ett
            string_popchange = concatenated_popchange.to_string(formatters={'country':'{{:<{}s}}'.format(concatenated_popchange['country'].str.len().max()).format}, col_space = 22, index=False, header=False) #Det sammanfogade data.framet konverteras till ett formaterat sträng
            string_concatenated_popchange = string_popchange.splitlines() #Stränget konverteras till listan (varje rad utgör ett separat element) för att kunna formatera tabellen senare
            
            print ("Land \t\t\t\t\t\t\t\t\t Antal födslar \t\t Antal döda \t Netto migration Befolkningsförändring")
            print (" \t\t\t\t\t\t\t\t\t\t [per 100000 inv] \t [per 100000 inv] [per 100000 inv] [% av folkmängd]")
            print ("-------------------------------------------------------------------------------------------------------------------")
            print("Länder där befolkningen minskar mest")
            print(*string_concatenated_popchange[0:5], sep = "\n") # De första 5 elementen av listan skrivs ut
            print("Länder där befolkningen ökar mest")
            print(*string_concatenated_popchange[5:], sep = "\n") # De sista 5 elementen av listan skrivs ut
            
            countries = concatenated_popchange['country'] #Länder som x-axeln
            popchange = countries_popchange_lagst['population_change'].append(countries_popchange_storst['population_change']) #bfolkningsöförädning som y-axeln
            fig = plt.figure(figsize = (8,4)) #En 800x400 figuryta initieras 
            ax = fig.add_axes([0,0,1,1])  #Diagramobjektet ax initieras 
            ax.bar(countries, popchange, color=('blue', 'orange', 'darkgreen', 'red', 'purple','brown','deeppink', 'grey','olive', 'aqua' )) #Variablerna plottas och färgerna definieras
            ax.set_title("Länder med minst och störst befolkhningsökning") #Diagrammets titel
            ax.set_ylabel("Befolkningsökning (% av folkmängd)") #Etikett på y-label
            plt.xticks(rotation=45) #Länderna i x-axeln (x-ticks) roteras 45 grader
            plt.grid() #En grid skapas 
            plt.show()
            
            
        elif val == 4: # Om val 4 görs, programmet avslutas och while-satsen avbryts
            print ('Avslutar\n')
            break 
        
meny()  #Funktionen anropas 