#6.Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos
lisa = []
for x in range (1,11):
    number = int(input(f"Digita el numero {x}: "))
    lisa.append(number)

mor3=list(filter(lambda n: len(str(n[1]))>3, enumerate(lisa)))

print("Los numeros que contienen mas de 3 digitos se ecuentran en:")
for y in mor3:
    print(f"En la posicion {y[0]+1} ")
