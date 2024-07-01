#6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.


number = int(input("Elige un numero de 3 digitos: "))
number1 = (number//100) %10
number2 = (number//10) %10
number3 = (number%10)
lise = []
lisa = []
elise = []

for x in range(2,number1):
    lise.append(x)
for x in range(2,number2):
    lisa.append(x)
for x in range(2,number3):
    elise.append(x)

print(f"Los numeros comprendidos entre 1 y {number1} es {lise}") 
print(f"Los numeros comprendidos entre 1 y {number2} es {lisa}")
print(f"Los numeros comprendidos entre 1 y {number3} es {elise}")