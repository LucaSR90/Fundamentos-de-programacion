#7.Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista

lisa = []
tot = 0
for x in range (1,11):
    num = int(input(f"Digita el numero {x}: "))
    lisa.append(num)
    tot+=num
prom = tot/len(lisa)
print(f" El promedio entero de los numeros introducidos en esta lista es {prom}")
print (lisa)