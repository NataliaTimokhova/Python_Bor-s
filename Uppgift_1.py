# Skriv in din kod för Uppgift 1 här nedan
# ----------------------------------------

import numpy as np 

print()
print("Uppgift 1a")
# Uppgift 1a:
# -----------

def formula(x, y):                          # först skapas funktionen vilken används senare
    return x**2 + y**2

NP_A = np.fromfunction(formula, (10, 8), dtype=int)    # 10 antal rader, 8 antal stolpar i array
print(NP_A)
print()
print()
print("Uppgift 1b")

# Uppgift 1b:
# -----------

result = np.array([[NP_A[2, 1], NP_A[2, 4]], [NP_A[1, 5], NP_A[5, 4]]])
print(result)
print()
print()
print("Uppgift 1c") 

# Uppgift 1c:
# -----------

NP_A_list = NP_A.tolist()
print(NP_A_list)
print()                                     # en tom rad för klarhet
for rad in NP_A_list:
    for element in rad:
        if 20 < element < 50:
            print(element, end=" ")
print()
print()
print("Uppgift 1d") 

# Uppgift 1d:
# -----------

print()
print('1. Summa av max och min värde i varje rad')

for rad in NP_A:
    max_value = np.max(rad)
    min_value = np.min(rad)
    rad_sum = max_value + min_value
    rad_mean = np.mean(rad)
    print(rad_sum, end=" ")
print()
print()

print('2. Medelvärdet av varje rad')
for rad in NP_A:
    max_value = np.max(rad)
    min_value = np.min(rad)
    rad_mean = np.mean(rad)
    print(rad_mean, end=" ")
print()
print()
    
# samma princip för kolumner, behövs att transponera först 
print('1.Summa av max och min värde i varje kolumn')
for rad in NP_A.T:
    max_value = np.max(rad)
    min_value = np.min(rad)
    rad_sum = max_value + min_value
    rad_mean = np.mean(rad)
    print(rad_sum, end=" ")
print()
print()
    
print('2. Medelvärdet av varje kolumn')
for rad in NP_A.T:
    max_value = np.max(rad)
    min_value = np.min(rad)
    rad_mean = np.mean(rad)
    print(rad_mean, end=" ")
print()
print()
print("Uppgift 1e") 
print()

# Uppgift 1e:
# -----------

transformed_array = np.where(NP_A > 107, -100, NP_A)
print(transformed_array)
print()
print()
print("Uppgift 1f") 
print()

# Uppgift 1f:
# -----------

data = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
          4, 4, 4, 4, 4, 112, 112, 112, 112, 112,
          16, 16, 16, 16, 16, 25, 25, 25, 25, 25,
          36, 36, 36, 36, 36, 112, 112, 112, 112, 112,
          64, 64, 64, 64, 64, 81, 81, 81, 81, 81]

NP_Arr = np.array(data, dtype=float)

print(NP_Arr)

# Uppgift 1g:
# -----------

import matplotlib.pyplot as plt

# värden för diagram
x = np.arange(len(NP_Arr))
y1 = NP_Arr**2 + 10*NP_Arr
y2 = NP_Arr**2
y3 = 10*NP_Arr

# rita graferna
plt.plot(x, y1, label='NP_Arr**2 + 10*NP_Arr', color='green')
plt.plot(x, y2, label='NP_Arr**2', color='red')
plt.plot(x, y3, label='10*NP_Arr', color='blue')
plt.legend()

# Visa diagrammet
plt.show()


