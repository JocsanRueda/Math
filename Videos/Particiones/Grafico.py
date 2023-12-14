import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Definir la función partition
def partition(n):
    if n == 0:
        return 1

    partitions = [0] * (n + 1)
    partitions[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    return partitions[n]

# Generar datos para x
x_values = np.arange(1, 100)

# Calcular y_values utilizando la función proporcionada
y_values_real = [partition(x) for x in x_values]

# Calcular y_values aproximados
y_values_approx = [1 / (4 * x * np.sqrt(3)) * np.exp(np.pi * np.sqrt(2 / 3 * x)) for x in x_values]

# Configurar el estilo de Seaborn
sns.set_theme(style="whitegrid")

# Crear el gráfico de dispersión
f, ax = plt.subplots(figsize=(6.5, 6.5))
sns.despine(f, left=True, bottom=True)

# Definir el orden de claridad
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

# Crear el gráfico de dispersión con los valores generados
sns.scatterplot(x=x_values, y=y_values_real, label="Real", color="blue", ax=ax)
sns.scatterplot(x=x_values, y=y_values_approx, label="Aproximado", color="red", ax=ax,
                hue_order=clarity_ranking, sizes=(1, 8), palette="ch:r=-.2,d=.3_r", linewidth=0)

# Mostrar el gráfico
plt.legend()
plt.show()
