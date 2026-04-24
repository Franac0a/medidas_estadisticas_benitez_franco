import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Edades reales de los estudiantes
edades = np.array([
    21, 20, 20, 19, 28, 21, 18, 21, 25, 19,
    20, 20, 21, 19, 19, 21, 19, 25, 25, 19,
    19, 20, 21, 20, 19, 24, 22, 19, 34, 20,
    26, 27, 20, 20, 25, 25, 19, 19, 24, 19,
    23, 19, 19, 19, 30, 20, 22
])

print("Edades:", edades)

# Tipo de variable
print("Tipo de variable: Cuantitativa discreta")

# Medidas estadísticas básicas
media = np.mean(edades)
mediana = np.median(edades)
varianza = np.var(edades)
desviacion_estandar = np.std(edades)
rango = np.max(edades) - np.min(edades)

# Percentiles
Q1 = np.percentile(edades, 25)
Q2 = np.percentile(edades, 50)
Q3 = np.percentile(edades, 75)

# Moda con pandas
moda = pd.Series(edades).mode()[0]

# Mostrar resultados
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion_estandar)
print("Rango:", rango)
print("Percentil 25 (Q1):", Q1)
print("Percentil 50 (Q2):", Q2)
print("Percentil 75 (Q3):", Q3)

# Histograma
plt.hist(edades, bins=10, edgecolor="black")
plt.title("Distribución de edades de los estudiantes")
plt.xlabel("Edades")
plt.ylabel("Frecuencia")
plt.show()