#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Inlämningsuppgift. Del 2"""

'''
In Del 2, we will present information from the df_cia_factbook.
To decouple the code from Del 1, we import uppg1 as a new module del_1.

'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import uppg1 as del_1


# for activating the functions below we need to take data from Uppg1.py
data = del_1.df_cia_factbook



def transform_dataset(data):    
    
    '''
    This function will create a new variable "density" in df_cia_factbook as 
    the ratio between the population column and the area column
    and clean data from the rows with NaN and Inf values and delete the rows 
    with missing values in density.
    
    We add try:except code for catching errors if they are in the data set or
    if there are no keys of interest (population, area).
    '''   
    
    try:
        data = data.copy()   #otherwise the original dataframe may be modified
        data["density"] = data["population"]/data["area"]
        data["density"].replace([np.inf, -np.inf], np.nan, inplace=True)
        data_transformed = data.dropna(subset=['density'])
        
        return data_transformed
    
    except KeyError as e:
        print(f"KeyError: {e}. Kontrollera om data har 'population' och 'area' columner.")
    
    except Exception as e:
        print(f"Error: {e}.")


data_new = transform_dataset(data)




def count_of_density(data_new):
    
    '''
    This function will ask for an input and then represent the output as the density 
    of a country or a chart for 1-10 countries. 
    In descending order of the largest countries if the input is with +,
    in ascending order of the smallest countries if the input includes -
    and the value of the density if the input has only one country.
    
    '''    
    
    print('--------------------------------------------------------')
    print('För att beräkna befolkningstäthet kan du valja ett land (skriv på engelska)')
    print('eller ett antal av länder (max 10) som visar')
    print('de länderna med störst befolkningstäthet, ange ett heltal med plus, t.ex. 4+')
    print('de länderna med lägst befolkningstäthet, ange ett heltal med minus, t.ex. 4-')
    print('--------------------------------------------------------')
    
    # the program will not terminate until we enter the required input
    while True:
        country = input("Ange ett landsnamn på engelska eller ange ett tal med tecknet : ")
        
        # we check the input conditioned that the input is a number
        try:
            
            number_of_countries= int(country[:-1])
            if number_of_countries>10:
                number_of_countries = 10  # on the diagram we will have max 10 countries
                print('---------------------------------')
                print("\nMax antal länder som kan plottas är 10.")
            
            # We have different outputs for the plots depending on the sign + or -
            if country[-1]=='+':
                most_populated_countries = data_new.sort_values(by="density", ascending=False).head(number_of_countries)
                most_populated_countries.plot(kind="bar", x="country", y="density", legend=False, width=0.8)
                
                # plot
                plt.ylabel("Befolkningstäthet [inv/km2]")
                plt.xlabel("Länder")
                plt.title(f"Länder med störst befolkningstäthet")
                plt.xticks(rotation=45)
                plt.grid()
                plt.show()
                pass
                
                
            elif country[-1]=='-':
                least_populated_countries = data_new.sort_values(by="density", ascending=True).head(number_of_countries)
                least_populated_countries.plot(kind="bar", x="country", y="density", legend=False, width=0.8)
                
                # plot
                # We will not rotate the countries names here because of a large name for one of them
                plt.ylabel("Befolkningstäthet [inv/km2]")
                plt.xlabel("Länder")
                plt.title(f"Länder med lägst befolkningstäthet")
                plt.grid()
                plt.show()
                pass
                
            else:
                raise ValueError("Du tryckte varken + eller -\n")
            
            return f"\nDu kan se {number_of_countries} länder på diagrammet ovan."
                
            
        # we checked before the input conditioned that the input is a number (Value)
        # if not, we need to check if we have this single country in the list (Key)
        except ValueError:
            if country in data_new["country"].values:
                data_country = data_new[data_new["country"] == country]
                density_value = data_country["density"].values[0]
                return f"\nBefolkningstäthet av {country} är {density_value:.2f} inv/km2"
            else:
                print('-----------------------------')
                print("Du gav ett fel landsnamn eller tryckte varken + eller -")
                print("\nKontrollera reglerna för input ovanför")
                print('-----------------------------')
        except KeyError as e:
            print(f"\nKeyError: {e}. Kontrollera att du har stavat rätt och att landet finns i datamängden.\n")
        except IndexError as e:
            print(f"\nIndexError: {e}. Kontrollera att du gav ett tal i intervallet [1,10].\n")

            
print(count_of_density(data_new))  

        
           
            
            
            
