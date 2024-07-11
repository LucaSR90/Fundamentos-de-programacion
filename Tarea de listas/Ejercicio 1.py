#1.Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído"

lisa = []
for x in range (1,11):
    lisa.append(int(input(f"Digita el numero {x}: ")))
max = lisa.index(max(lisa))
print(f" El numero mas alto introducido esta en la posicion numero {max+1}")