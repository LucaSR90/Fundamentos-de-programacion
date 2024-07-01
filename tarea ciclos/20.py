#20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.

number = int(input("Elige un numero: "))
ammount = number
y = 1
z = 0
while ammount > 2:
    for x in range(1,ammount):
        y*=x
    z+=y
    y=1
    ammount-=1
print(f"La sumatoria de los factoriales de los numeros comprendidos entre 1 y {number} es {z}")