#2.Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de del arreglo está el mayor número par leído.
lisa = []
lise = []

for x in range (1,11):
    number = int(input(f"Digita el numero {x}: "))
    lisa.append(number)
    if number/2%1 == 0:
        lise.append(number)
max = lisa.index(max(lise))

print(f" El numero mas alto par introducido esta en la posicion numero {max+1}")