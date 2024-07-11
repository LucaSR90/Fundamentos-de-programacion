#3.Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.
lisa = []
lise = []
z = 1
w=0
for x in range (1,11):
    number = int(input(f"Digita el numero {x}: "))
    lisa.append(number)
    while z<=number:
        if number%z ==0:
            w+=1
        z+=1 
    if w == 2:
        lise.append(number)
    z = 1
    w = 0
max = lisa.index(max(lise))

print(f" El numero mas alto primo introducido esta en la posicion numero {max+1}")
print(lisa)