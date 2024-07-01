#2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.
number = int(input("Elige un numero: "))
lise = []
for x in range(2,number):
    if x/2 %1 == 0:
        lise.append(x)
print(f"Los numeros pares comprendidos entre 1 y {number} son {lise}")