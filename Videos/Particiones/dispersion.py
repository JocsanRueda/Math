import matplotlib.pyplot as plt
import numpy as np

# Funciones proporcionadas
def partition(n):
    if n == 0:
        return 1

    partitions = [0] * (n + 1)
    partitions[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            partitions[j] += partitions[j - i]

    return partitions[n]

# Generar valores para x y y utilizando las funciones
x_values = np.arange(1, 80)
y_true_values = [partition(x) for x in x_values]
y_measured_values = [1 / (4 * x * np.sqrt(3)) * np.exp(np.pi * np.sqrt(2 / 3 * x)) for x in x_values]

# Configuración de estilo similar a Manim
plt.style.use('dark_background')

# Crear el gráfico de dispersión
plt.scatter(x_values, y_true_values, label='Valor Real', color='blue', marker='o')
plt.scatter(x_values, y_measured_values, label='Valor Medido', color='red', marker='p')

# Personalizar el gráfico
plt.title('Gráfico de Dispersión')
plt.xlabel('Eje X (Valores Enteros)')
plt.ylabel('Valores de y')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
