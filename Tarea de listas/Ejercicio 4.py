#4.Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo

lisa = []
lise = 0
z = 1
w=0
for x in range (1,11):
    number = int(input(f"Digita el numero {x}: "))
    lisa.append(number)
    while number>=10:
        number//=10
    while z<=number:
        if number%z ==0:
            w+=1
        z+=1 
    if w == 2:
        lise+=1
    z = 1
    w = 0

print(f" Los cantidad de numeros de la lista que empiezan por numero primo son {lise}")
print(lisa)