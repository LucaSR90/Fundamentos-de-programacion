#13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.

number = int(input("Elige un numero: "))
lise = []

for x in range(2,number):
    if (x/5) %1 == 0:
        lise.append(x)
print(f"Los multiplos de 5 entre los numeros comprendidos entre 1 y {number} son {lise}")