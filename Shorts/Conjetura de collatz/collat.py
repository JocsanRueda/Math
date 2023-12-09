import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iteraciones = {}


def collatz(n):
    r = 0
    n2 = n

    if not iscache(n):
        while n2 != 1:
            if iscache(n2):
                iteraciones[n] = r + iteraciones[n2]
                return 1
            elif n2 % 2 == 0:
                n2 /= 2.0
            else:
                n2 = 3 * n2 + 1.0
            r += 1

    iteraciones[n] = r
    return 1


def iscache(n):
    return n in iteraciones


n = 1
limite=100000
while(n<=limite):
    collatz(n)
    n+=1



# Convierte el diccionario en un DataFrame
df = pd.DataFrame(list(iteraciones.items()), columns=['Numero', 'Iteraciones'])

# Crea la gráfica de barras
plt.bar(df['Numero'], df['Iteraciones'])

# Agrega etiquetas y título
plt.xlabel('Numero')
plt.ylabel('Iteraciones')
plt.yticks(range(0,max(iteraciones.values())+1,50))
plt.xticks(range(0,len(iteraciones)+1,100000))
plt.title('Gráfica de Barras conjetura de collatz')

print(iteraciones)
# Muestra la gráfica
plt.show()


