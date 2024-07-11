#5.Leer 10 números enteros, almacenarlos en una lista y  determinar en qué posición se encuentra el número primo  con mayor cantidad de dígitos pares.

lisa = []
elise = []
lise = 0
times = 1
z = 1
w=0
for x in range (1,11):
    number = int(input(f"Digita el numero {x}: "))
    reset = number
    lisa.append(number)
    while number>=10:
        number//=10
        times+=1
    while z<=number:
        if number%z ==0:
            w+=1
        z+=1 
    number = reset
    if w == 2:
        while times>0:
            red = number%10
            times-=1
            number//=10
            if red % 2 == 0:
                lise+=1
              
    elise.append(lise)
    lise = 0
    z = 1
    w = 0
    times = 1 

print(f" El numero primo con mayor cantidad de digitos pares se ecuentra en la posicion {elise.index(max(elise))+1} siendo el numero {lisa[(elise.index(max(elise)))]}")
print(f"La lista digitada fue: {lisa}")