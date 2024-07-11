#10.Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.

lisa = []
lise = []
tms = 0
y = 0
for x in range (1,11):
    num = int(input(f"Digita el numero {x}: "))
    lisa.append(num)
number = int(input("Elige otro numero: "))

while tms <len(lisa):
    if number/lisa[y] %1 ==0:
        lise.append(lisa[y])
    y+=1
    tms+=1
print(f"Los divisores exactos de {number} en la lista, son {lise}")
print (f"La lista introducida fue {lisa}")