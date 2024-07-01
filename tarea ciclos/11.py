#11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.

number = int(input("Elige un numero: "))
number1 = (number//10) 
number2 = (number%10)
lise = []
if number>=10 and number<=99:
    for x in range(number1+1,number2):
        lise.append(x)
    for y in range(number2+1,number1):
        lise.append(y)  
    print(f"Los numeros comprendidos entre {number1} y {number2} son {lise}") 
else:
    print("No es un numero de 2 digitos")