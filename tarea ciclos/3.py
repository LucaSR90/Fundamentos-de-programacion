#3. Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído

number = int(input("Elige un numero: "))
lise = []

for x in range(2,number):
    if number/x %1 == 0:
        lise.append(x)
print(f"Los divisores exactos entre 1 y {number} son {lise}")