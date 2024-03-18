#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Inlämningsuppgift. Del 1


-------------------------------------------------------------
We create the DataFrame objects using the Pandas module
based on files in scv format to be able to manipulate data:
    
      Object name                  File name
    df_cia_factbook     ut      cia_factbook.csv
    df_worldcities      ut      worldcities.csv
    df_worldpubind      ut      worldpubind.csv
-------------------------------------------------------------
"""

import pandas as pd


    
df_cia_factbook = pd.read_csv('cia_factbook.csv', sep = ';', 
                              encoding= 'latin_1', index_col='Index')

df_worldcities = pd.read_csv('worldcities.csv', sep = ';', 
                              encoding= 'latin_1', index_col='id')
    
df_worldpubind = pd.read_csv('worldpubind.csv', sep = ';') 
                              






