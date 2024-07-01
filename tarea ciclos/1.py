#1. Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído.m

number = int(input("Elige un numero:"))
lise = []
for x in range(2,number):
    lise.append(x)
print(f"Los numeros comprendidos entre 1 y {number} son {lise}")