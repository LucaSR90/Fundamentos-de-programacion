#10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.

number = int(input("Elige un numero: "))
lise = 0
for x in range(2,number):
    lise = (lise + x)     
print(f"La sumatoria de los numeros comprendidos entre 1 y {number} es {lise}") 