# 9.Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenándolos en otra lista

lisa = []
lise = []
y = 1

for x in range (1,11):
    num = int(input(f"Digita el numero {x}: "))
    lisa.append(num)
    for w in range(1,num+1):
        y*=w
    lise.append(y)
    y = 1
print (lisa)
print("En la siguiente lista se encuentra los factoriales de los numeros anteriores")
print(lise)
