#!/usr/bin/env python
# coding: utf-8

# -------------------------------------------------------------------------------------------------------------------------------------------

"""
https://matplotlib.org/
"""


# plotta ett enkelt diagram i Python med hjälp av modulen matplotlib.

import matplotlib.pyplot as plt  #importerar matplotlib och dess undermodul pyplot och ge dessa namnet plt

data_to_plot = [1.2, 3.5, 4.1, 9.6, 7.1, 5.6]   #lista som innehåller den data som ska visas i diagrammet

plt.plot(data_to_plot)      #plot() bygger upp ett diagram med värdena från listan jämnt fördelat i x-led
plt.title('Trigonometrics')
plt.show()                  #show() visar diagrammet på skärmen




#att infoga diagramtitel och förklarande text på x- och y-axel.

import matplotlib.pyplot as plt  #importerar matplotlib och dess undermodul pyplot och ge dessa namnet plt

data_to_plot = [1.2, 3.5, 4.1, 9.6, 7.1, 5.6]

plt.plot(data_to_plot)         

#diagramtitel och förklarande text på x- och y-axel:
plt.title('Diagramtiteln hamnar här')
plt.xlabel('Förklarande text för x-axeln hamnar här')
plt.ylabel('Förklarande text för y-axeln hamnar här')

plt.show()                  #show() visar diagrammet på skärmen


#att ändra axelgradering med funktionerna xlim() och ylim().

import matplotlib.pyplot as plt 

data_to_plot = [1.2, 3.5, 4.1, 9.6, 7.1, 5.6]

plt.plot(data_to_plot)         
plt.title('Diagramtiteln hamnar här')
plt.xlabel('Förklarande text för x-axeln hamnar här')
plt.ylabel('Förklarande text för y-axeln hamnar här')

#ändra axelgradering:
plt.xlim(1,5)             #xlim(1,5) --> x-axeln visas mellan 1 och 5
plt.ylim(3,10)            #ylim(3,10) --> y-axeln visas mellan 3 och 10

plt.show()              



#ändra färg och lägg till en etikett

import matplotlib.pyplot as plt 

data_to_plot = [1.2, 3.5, 4.1, 9.6, 7.1, 5.6]

#ändra färg och lägg till en etikett:
plt.plot(data_to_plot, color = 'red', label='Kurvtext')         

plt.title('Diagramtiteln hamnar här')
plt.xlabel('Förklarande text för x-axeln hamnar här')
plt.ylabel('Förklarande text för y-axeln hamnar här')
plt.xlim(1,5)             
plt.ylim(3,10)           

#visa etiketten 'Kurvtext' i diagrammet:
plt.legend()

plt.show()              



#flera kurvor i samma diagram.

import matplotlib.pyplot as plt 

kurva_1 = [1.2, 3.5, 4.1, 9.6, 7.1, 5.6]      #kurva 1
kurva_2 = [2.1, 5.3, 1.4, 6.9, 1.7, 6.5]      #kurva 2

#lägg till en lista med x-koordinater:
x_koord = [0.5, 1.0, 1.5, 2, 2.5, 3]

#lägg till flera kurvor genom att använda flera plot()-funktioner:
plt.plot(x_koord, kurva_1, color = 'red', label='Etikett Kurva_1')                        #plot() för kurva 1
plt.plot(x_koord, kurva_2, color = 'blue', linestyle= 'dashed', label='Etikett Kurva_2')  #streckad kurva med
                                                                                          #linestyle
#att sätta bakgrundsfärg:
ax = plt.gca()
ax.set_facecolor('honeydew')

plt.title('Diagramtiteln hamnar här')
plt.xlabel('Förklarande text för x-axeln hamnar här')
plt.ylabel('Förklarande text för y-axeln hamnar här')      
plt.legend()

#skapa ett gridmönster
plt.grid()

plt.show()              

# -------------------------------------------------------------------------------------------------------------------------------------------

""" 
typer av linjen
https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/linestyles.html

Typer av color
https://matplotlib.org/3.1.0/gallery/color/named_colors.html

"""

# Källkod för avsnittet Matplotlib med objektorienterat gränssnitt




import matplotlib.pyplot as plt         # Ladda in modulen matplotlib.pyplot och ge denna alias plt
 
fig = plt.figure()                      # Skapa figurobjektet 'fig' som initierar en tom figuryta


import matplotlib.pyplot as plt         # Ladda in modulen matplotlib.pyplot och ge denna alias plt
 
fig = plt.figure(figsize=(8,4), dpi=100, facecolor = 'lightblue' )   # Skapa ett 800x400 pixel, 100 dpi 
                                                                     # figurobjekt med ljusblå yttre 
                                                                     # figurfärg

ax = fig.add_axes([0,0,1,1])            # Skapa ett diagramobjekt

ax.plot([1,2,3])                        # Plotta diagramobjektet



import matplotlib.pyplot as plt            # Ladda in modulen matplotlib.pyplot och ge denna alias plt
 
fig1 = plt.figure()                        # Skapa figurobjektet 'fig' som initierar en tom figuryta
fig1.set_size_inches(10,7)                 # Figurstorlek 10x7 inch (width, height)
ax1 = fig1.add_axes([0,0,1,1])             # Skapa maximal figuryta  --> 
                                           # [left, bottom, width, height] = [0,0,1,1]

x = [0,10,20,30,40,50]                     # x-värden
y = [0,5,3,6,2,7]                          # y-värden

ax1.plot(x,y)                              # Plottar x mot y
plt.show()




import matplotlib.pyplot as plt              # Ladda in modulen matplotlib.pyplot och ge denna alias plt
 
fig = plt.figure()                           # Skapa figurobjektet 'fig' som initierar en tom figuryta
fig.set_size_inches(10,7)                    # Figurstorlek 10x7 inch (width, height)
ax1 = fig.add_axes([0,0,1,1])                # Skapa diagramobjektet ax1 som nyttjar maximal figuryta:
                                             # [left, bottom, width, height] = [0,0,1,1]

ax2 = fig.add_axes( [0.3, 0.1, 0.4, 0.4] )   # Skapa diagramobjektet ax2 som nyttjar en reducerad figuryta
                                             # [left, bottom, width, height] = [0.3, 0.1, 0.4, 0.4]


x = [0,10,20,30,40,50]                       # x-värden
y = [0,5,3,6,2,7]                            # y-värden

ax1.plot(x,y)                                # Skapar innehållet i diagrammet med maximal figuryta
ax2.plot(x,y)                                # Skapar innehållet i diagrammet med reducerad figuryta
plt.show()                                   # Plottar dessa diagram
              

import matplotlib.pyplot as plt                 # Ladda in modulen matplotlib.pyplot och ge denna alias plt
 
fig = plt.figure()                              # Skapa figurobjektet 'fig' som initierar en tom figuryta
fig.set_size_inches(10,7)                       # Figurstorlek 10x7 inch (width, height)
ax1 = fig.add_axes([0,0,1,1])                   # Skapa diagramobjektet ax1 med som nyttjar maximal figuryta  --> 
                                                # [left, bottom, width, height] = [0,0,1,1]
ax1.set_title('Diagram med maximal figuryta')   # Sätt diagramrubrik till diagramobjektet ax1 
ax1.set_xlabel('x-värden')                      # Etikett för x-axeln
ax1.set_ylabel('y-värden')                      # Etikett för y-axeln
x = [0,10,20,30,40,50]                          # x-värden
y = [0,5,3,6,2,7]                               # y-värden

ax1.plot(x, y, color = 'b', marker = 'o', label='Kurvetikett', linestyle='--') # Skapar kurvan med
                                                                               # angivna attribut
ax1.legend(loc ='upper left')                   # Placerar kurvettiketten på önskad plats i diagrammet

plt.show()                                      # Plottar det färdiga diagrammet
              

"""
figurer

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
colors

https://matplotlib.org/stable/gallery/color/named_colors.html

"""



# Källkod till Matplotlib - flera diagram i samma figur

# -------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,4), dpi=100, facecolor = 'lightblue')

x = np.arange(1,10)             # Skapa x-värden 

# Diagram 1:
plt.subplot(1,2,1)              # Rutnät: 1 rad, 2 kolumner. Index = 1 --> diagrammet ritas i första rutan
plt.plot(x, x*x)                # Skapar kurvan
plt.title('kvadrat')
plt.xlabel('x-värden')
plt.ylabel('y-värden')
plt.tight_layout()              # Skapar ramen runt diagrammet

# Diagram 2:
plt.subplot(1,2,2)              # Rutnät: 1 rad, 2 kolumner. Index = 2 --> diagrammet ritas i andra rutan
plt.plot(x, np.sqrt(x))
plt.title('kvadatrot')
plt.xlabel('x-värden')
plt.ylabel('y-värden')
plt.tight_layout()              # Skapar ramen runt diagrammet

# -------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,4), dpi=100, facecolor = 'lightblue')

x = np.arange(1,10)             # Skapa x-värden 

# Diagram 1:
plt.figure(figsize=(8,4), dpi=100, facecolor = 'lightblue')
plt.subplot(2,2,1)              # Rutnät: 2 rader, 2 kolumner. Index = 1 --> diagrammet ritas i första rutan
plt.plot(x, x*x)                # Skapar kurvan
plt.title('kvadrat')
plt.xlabel('x-värden')
plt.ylabel('y-värden')
plt.tight_layout()              # Skapar ramen runt diagrammet

# Diagram 2:
plt.subplot(2,2,4)              # Rutnät: 2 rader, 2 kolumner. Index = 4 --> diagrammet ritas i 
                                # nedre högra rutan
plt.plot(x, np.sqrt(x))
plt.title('kvadatrot')
plt.xlabel('x-värden')
plt.ylabel('y-värden')
plt.tight_layout()              # Skapar en lagom stor ram runt diagrammet

# -------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6,6), dpi=100, facecolor = 'lightblue')   # Skapa ett figurobjekt

x = np.linspace(0,6.28,100)             # Skapa 100 st x-värden mellan 0 - 6.28

#Diagram 1:
ax1 = fig.add_subplot(1,1,1)            # Diagramobjektet ax1 innehåller 1 diagram
ax1.plot(x,np.sin(x), color='r')
ax1.set_title('sin')

#Diagram 2:
ax2 = fig.add_subplot(2,2,2)            # Diagramobjektet ax2 skapar möjligheten att plotta 4 diagram.
                                        # Här skapas bara 1 diagram som skrivs ut i övre högra rutan
ax2.plot(x,np.cos(x), color='g')         
ax2.set_title('cos')
plt.show()


# -------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,4), dpi=100, facecolor = 'lightblue') # Skapa ett figurobjekt
                                        
d = fig.subplots(nrows=2, ncols=2)       # Figurobjektet innehåller 4 diagram organiserade 
                                         # i två rader och 2 kolumner 

x = np.arange(1,10)                      # Skapa x-värden 
    
d[0][0].plot(x,x*x)                      # Diagrammet i övre vänstra hörnet
d[0][0].set_title('kvadrat')
d[0][1].plot(x,np.sqrt(x))               # Diagrammet i övre högra hörnet
d[0][1].set_title('kvadratrot') 
d[1][0].plot(x,np.exp(x))                # Diagrammet i nedre vänstra hörnet
d[1][0].set_title('exp')
d[1][1].plot(x,np.log(x))                # Diagrammet i nedre högra hörnet
d[1][1].set_title('log')
d[1][1].set_xlabel('x-värden diagram 4') # Etikett för x-axel diagram 4
d[1][1].set_ylabel('y-värden diagram 4') # Etikett för y-axel diagram 4

fig.tight_layout()                       # Skapar en lagom stor ram runt diagrammet

fig.savefig('matplotlib_subplots.jpg')   # Skapar och sparar en jpg-bild av diagrammen 


# -------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,4), dpi=100, facecolor = 'lightblue') # Skapa ett figurobjekt
#plt.xkcd()

print(plt.style.available)
plt.style.use('seaborn-paper')


d = fig.subplots(nrows=2, ncols=2)       # Figurobjektet innehåller 4 diagram organiserade 
                                         # i två rader och 2 kolumner 

x = np.arange(1,10)                      # Skapa x-värden 
    
d[0][0].plot(x,x*x)                      # Diagrammet i övre vänstra hörnet
d[0][0].set_title('kvadrat')
d[0][1].plot(x,np.sqrt(x))               # Diagrammet i övre högra hörnet
d[0][1].set_title('kvadratrot') 
d[1][0].plot(x,np.exp(x))                # Diagrammet i nedre vänstra hörnet
d[1][0].set_title('exp')
d[1][1].plot(x,np.log(x))                # Diagrammet i nedre högra hörnet
d[1][1].set_title('log')
d[1][1].set_xlabel('x-värden diagram 4') # Etikett för x-axel diagram 4
d[1][1].set_ylabel('y-värden diagram 4') # Etikett för y-axel diagram 4

fig.tight_layout()                       # Skapar en lagom stor ram runt diagrammet

fig.savefig('matplotlib_subplots.jpg')   # Skapar och sparar en jpg-bild av diagrammen 
plt.show()


