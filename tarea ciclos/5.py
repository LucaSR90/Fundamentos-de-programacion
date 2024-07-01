#5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.

number1 = int(input("Elige el 1er numero: "))
number2 = int(input("Elige el 2ndo numero: "))
lise = []
for x in range(number1+1,number2):
    if x %10 == 4:
        lise.append(x)
for x in range(number2+1,number1):
    if x %10 == 4:
        lise.append(x)
print(f"Los numeros que terminan en 4 comprendidos entre {number1} y {number2} son {lise}")