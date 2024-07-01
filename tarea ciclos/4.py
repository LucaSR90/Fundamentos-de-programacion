#4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.

number1 = int(input("Elige el 1er numero: "))
number2 = int(input("Elige el 2ndo numero: "))
lise = []
for x in range(number1+1,number2):
        lise.append(x)
for y in range(number2+1,number1):
        lise.append(y)
print(f"Los numberos comprendidos entre {number1} y {number2} son {lise}")