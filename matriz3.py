#Suma de matrices
""" Leer 3 matrices 3 x 3 y sumar en una matriz"""
matriz = []
matrizA = []
for i in range(3):
    matrizA.append([])
    for j in range(3):
        matrizA[i].append( int(input(f"Ingrese los valores de la primera matriz ")))

matrizB = []
for i in range(3):
    matrizB.append([])
    for j in range(3):
        matrizB[i].append( int(input(f"Ingrese los valores de la segunda matriz ")))

matrizC = []
for i in range(3):
    matrizC.append([])
    for j in range(3):
        matrizC[i].append( int(input(f"Ingrese los valores de la ultima matriz ")))

matrizi = []
matrizj = []

matrizi = (matrizA[i] + matrizB[i] + matrizC[i])
matrizj = (matrizA[j] + matrizB[j] + matrizC[j])
        
print("El resultado de sumar las 3 matrices, es: ", matrizi, matrizj )

