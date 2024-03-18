
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Inlämningsuppgift. Del 4"""

'''
The program analyzes the percentage population development between 
the years 1960 and 2021 for the countries found in the DataFrame df_ worldpubind.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


df_worldpubind = pd.read_csv('worldpubind.csv', sep = ';') 
data = df_worldpubind 


def databehandling(data):
    
    while True:
        
        try:
            choice = int(input("\nVälj ett alternativ:\n1 för uppgift 4a\n2 avslutar programmet: "))
            
            if choice == 1:
                """
                Menu option 1:
                Create a table (on the screen) containing the percentage population change 
                for the 5 countries with the most negative population change (population decline)
                and the 5 countries with the most positive population change (ie population increase) 
                between the year 1960 and the year 2021. 
                Also display the same information graphically in two bar chart where the first bar chart
                shows the five countries with the negative population growth and the second bar chart 
                shows the countries with the positive population growth.
                    
                """
                
                # DATA PREPARATION
                data = data.loc[:, ['Country Name', '1960', '2021']].dropna()
                data['population_growth_percent'] = (data['2021'] - data['1960']) / data['1960'] * 100
                sorted_data = data.sort_values(by=['population_growth_percent'], ascending=False)
                
                top_pos = sorted_data.head(5)
                top_neg = sorted_data.tail(5)
                result = pd.concat([top_pos, top_neg])
                

                # FORMATING OF THE OUTPUT
                output = result[['Country Name', 'population_growth_percent']].reset_index(drop=True)
                output = output.rename(columns={
                    'Country Name': 'Land',
                    'population_growth_percent': 'Befolkningsutveckling mellan 1960 och 2021)'})                
                print( "-" * 98)
                print('Länder med minst och störst befolkningsutveckling')
                print( "-" * 98)
                print(output.to_string(index=False, header=True))
                print( "-" * 98)
                                
                
                # DIAGRAMMS
                
                # POSITIVE
                plt.style.use('ggplot')
                plt.figure(figsize=(10, 6))
                x_values = list(top_pos['Country Name'])
                y_values = list(top_pos['population_growth_percent'])
                colors = ['green']*5
                plt.bar(x_values, y_values, color=colors)
                plt.xticks(rotation=45, ha='right')
                plt.title('Länder med störst befolkningsökning mellan 1960 och 2021')
                plt.show()
                
                # NEGATIVE
                plt.style.use('ggplot')
                plt.figure(figsize=(10, 6))
                x_values = list(top_neg['Country Name'])
                y_values = list(top_neg['population_growth_percent'])
                colors = ['red']*5
                plt.bar(x_values, y_values, color=colors)
                plt.xticks(rotation=45, ha='right')
                plt.title('Länder med  störst befolkningsminskning mellan 1960 och 2021')
                plt.show()
                
                                
                
            elif choice == 2:
                print("Programmet avslutas, hej då.")
                break
                
            # a valid input type (integer), but not within range 1-4
            else:
                print('-----------------------------')
                print("Fel val")
        
        # the case when the user enters a non-integer value
        except ValueError:
            print('-----------------------------')
            print("Du tryckte fel, kontrollera stavning och att landet finns i listan")


print(databehandling(data))