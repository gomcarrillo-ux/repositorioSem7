matriz = []
for i in range(2):
    matriz.append([])
    for j in range(2):
        matriz[i].append( int(input(f"Ingrese los valores de su matriz ")))

for i in matriz: 
    print(i)