#17. Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5

lise = []
number = 1
count5 = 0
counta = 0

while number!=0:
    number = int(input("Elige numeros: "))
    lise.append(number)
    counta += 1
    ori = number
    number%=10
    if number == 5:
        count5 += 1
    number=ori
prom5 = counta/count5
print(f"El promedio de los numeros terminados en 5 entre los {counta} numeros digitados, es {prom5}")
print(lise)