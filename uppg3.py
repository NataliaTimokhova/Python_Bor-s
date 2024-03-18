#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Inlämningsuppgift. Del 3"""

'''
In this task, we will continue to practice extracting, further processing and
present information stored in df_cia_factbook according to the descriptions below.

The program must consist of a menu where the user chooses one of the four menu options.
When a menu option is executed, the menu should come up again and a new option
must be selectable (1,2,3), etc. Menu option 4 exits the program.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import uppg1 as del_1


data = del_1.df_cia_factbook

   

def databehandling(data):
    
    while True:
        
        try:
            choice = int(input("\nVälj ett alternativ (1-4), 4 avslutar programmet: "))
            
            if choice == 1:
                """
                Menu option 1:
                This menu item should print a table (on the screen) with the columns
                country, area, birth_rate and life_exp_at_birth for that country(s)
                that meet the following criteria:
                    
                """
                
                # DATA PREPARATION
                mean_pop = data['population'].mean()
                mean_area = data['area'].mean()
                selected_data = data.loc[(data['population'] > mean_pop) & 
                                         (data['area'] < mean_area) & 
                                         (data['birth_rate'] > 15) & 
                                         (data['birth_rate'] < 24) & 
                                         (data['life_exp_at_birth'] > 70)].copy()
                
                table_data = selected_data[['country', 'area', 'birth_rate', 'life_exp_at_birth']].copy()
                table_data.dropna(subset=['country', 'area','birth_rate','life_exp_at_birth'], inplace=True)
                # rename the columns according to the tasks example
                table_data.rename(columns={'country': 'Land', 'area': 'Area [km2]', 
                                           'birth_rate': 'Antal födslar [per 1000 inv]', 
                                           'life_exp_at_birth': 'Livslängd [år]'}, inplace=True)
                
                
                # FORMATING OF THE OUTPUT
                print("-" * 70, "\n", table_data.to_string(index=False, header=True))


                
            elif choice == 2:
                
                """
                Menu option 2:
                In this menu item, we will examine the maturity of the Internet
                in the population of the countries found in the df_cia_factbook
                
                """

                # DATA PREPARATION
                data['internet_user_density'] = data['internet_users'] / (data['population'] / 100000)
                internet_data = data[['country', 'population', 'internet_user_density']]
                internet_data = internet_data.dropna(subset=['internet_user_density'])
            
                lowest_internet_users = internet_data.sort_values(by='internet_user_density').head(5)
                highest_internet_users = internet_data.sort_values(by='internet_user_density', ascending=False).head(5)
            
                lowest_table = lowest_internet_users[['country', 'population', 'internet_user_density']]
                lowest_table = lowest_table.rename(columns={'country': 'Land', 'population': 'Folkmängd',
                                                            'internet_user_density': 'Internetanvändare'})
                lowest_table.index = [f'({i+1}) {row["Land"]}' for i, row in lowest_table.iterrows()]
 
                
                highest_table = highest_internet_users[['country', 'population', 'internet_user_density']]
                highest_table = highest_table.rename(columns={'country': 'Land', 'population': 'Folkmängd',
                                                              'internet_user_density': 'Internetanvändare'})
                highest_table.index = [f'({i+1}) {row["Land"]}' for i, row in highest_table.iterrows()]
              
                
                # FORMATING OF THE OUTPUT
                table = pd.concat([lowest_table, highest_table], axis=1,
                                  keys=['Länder med lägst antal internetanvändare per 100.000 invånare',
                                        'Länder med högst antal internetanvändare per 100.000 invånare'])
                
                print(table.to_string(index=False, header=True))
                print('\nLänder med lägst antal internetanvändare per 100.000 invånare\n', "-" * 70, "\n",)
                print(lowest_table.to_string(index=False, header=True))                
                print('\nLänder med högst antal internetanvändare per 100.000 invånare\n', "-" * 70, "\n",)
                print(highest_table.to_string(index=False, header=True))

                
                
            elif choice == 3:
                """
                In this menu option, we will make an estimate about the countries in
                df_cia_factbook has a positive or negative population change
                expressed as a percentage of the population for the year covered by the calculation.
                
                """

                # DATA COUNTING
                data['population_growth_rate'] = (data['birth_rate'] - data['death_rate'] + data['net_migration_rate'])
                data['population_change'] = data['population_growth_rate'] / data['population'] * 100
                # Filter out NamN values
                data = data[data['population_change'].notna()]
                sorted_data = data.sort_values(by='population_change', ascending=False)
                top_pos = sorted_data.head(5)
                top_neg = sorted_data.tail(5)
                result = pd.concat([top_pos, top_neg])
                
                
                # FORMATING OF THE OUTPUT
                output = result[['country', 'birth_rate', 'death_rate', 'net_migration_rate', 'population_change']].reset_index(drop=True)
                output = output.rename(columns={
                    'country': 'Land',
                    'birth_rate': 'Antal Födslar',
                    'death_rate': 'Antal döda',
                    'net_migration_rate': 'Netto migration',
                    'population_change': 'Befolkningsförändring'})                
                print( "-" * 98)
                print('Länder med minst och störst befolkningsökning')
                print( "-" * 98)
                print(output.to_string(index=False, header=True))
                print( "-" * 98)

               
                # DIAGRAMM
                plt.style.use('ggplot')
                plt.figure(figsize=(10, 6))
                x_values = list(top_pos['country']) + list(top_neg['country'])
                y_values = list(top_pos['population_change']) + list(top_neg['population_change'])
                colors = ['green']*5 + ['red']*5
                plt.bar(x_values, y_values, color=colors)
                plt.xticks(rotation=45, ha='right')
                plt.title('Länder med minst och störst befolkningsökning')
                plt.show()

                
            elif choice == 4:
                print("Programmet avslutas, hej då.")
                break
                
            # a valid input type (integer), but not within range 1-4
            else:
                print('-----------------------------')
                print("Fel val")
        
        # the case when the user enters a non-integer value
        except ValueError:
            print('-----------------------------')
            print("Fel")


print(databehandling(data))