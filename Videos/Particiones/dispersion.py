import seaborn as sns
import matplotlib.pyplot as plt

# Configurar el estilo de Seaborn
sns.set_theme(style="whitegrid")

# Cargar el conjunto de datos de diamantes de ejemplo
diamonds = sns.load_dataset("diamonds")

# Crear el gráfico de dispersión
f, ax = plt.subplots(figsize=(6.5, 6.5))
sns.despine(f, left=True, bottom=True)

# Definir el orden de claridad
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]

# Crear el gráfico de dispersión
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2,d=.3_r",
                hue_order=clarity_ranking,
                sizes=(1, 8), linewidth=0,
                data=diamonds, ax=ax)

# Mostrar el gráfico
plt.show()
