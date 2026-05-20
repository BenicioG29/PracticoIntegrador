
M = 
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]



print("Promedio por función:")

for i in range(3):
    suma = 0

    for j in range(3):
        suma = suma + M[i][j]

    promedio = suma / 3

    print("Funcion", i + 1, ":", promedio)


print("\nPromedio por servidor:")

for j in range(3):
    suma = 0

    for i in range(3):
        suma = suma + M[i][j]

    promedio = suma / 3

    print("Servidor", j + 1, ":", promedio)
    
git add .
git commit -m "Este código recorre la matriz M utilizando ciclos for para calcular los promedios. Primero analiza cada fila para obtener el promedio de ejecución de cada función y luego analiza cada columna para calcular el promedio de cada servidor. Se usan variables acumuladoras para sumar los valores y después dividir por la cantidad de elementos. El programa fue realizado únicamente con matrices, ciclos y operaciones básicas."
git push