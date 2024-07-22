import os

def saludar():
    nombre = input("Introduce tu nombre: ")
    return f"Hola, {nombre}!"

def sumar():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    return a + b

def area_rectangulo():
    base = float(input("Introduce la base del rectángulo: "))
    altura = float(input("Introduce la altura del rectángulo: "))
    return base * altura

def es_par_o_impar():
    numero = int(input("Introduce un número: "))
    return "Par" if numero % 2 == 0 else "Impar"

def celsius_a_fahrenheit():
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    return (celsius * 9/5) + 32

def max_de_tres():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    c = float(input("Introduce el tercer número: "))
    return max(a, b, c)

def es_palindromo():
    palabra = input("Introduce una palabra o frase: ")
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calcular_factorial():
    n = int(input("Introduce un número: "))
    return factorial(n)

def contar_vocales():
    texto = input("Introduce un texto: ")
    vocales = "aeiouAEIOU"
    return sum(1 for char in texto if char in vocales)

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos():
    hasta = int(input("Introduce el número hasta el cual buscar números primos: "))
    return [num for num in range(2, hasta+1) if es_primo(num)]

def mostrar_menu():
    print("Elige una función:")
    print("1. Saludar")
    print("2. Sumar")
    print("3. Área de un Rectángulo")
    print("4. Número Par o Impar")
    print("5. Conversión de Grados Celsius a Fahrenheit")
    print("6. Máximo de Tres Números")
    print("7. Palíndromo")
    print("8. Factorial")
    print("9. Contar Vocales")
    print("10. Números Primos")
    print("0. Salir")

funciones = {
    1: saludar,
    2: sumar,
    3: area_rectangulo,
    4: es_par_o_impar,
    5: celsius_a_fahrenheit,
    6: max_de_tres,
    7: es_palindromo,
    8: calcular_factorial,
    9: contar_vocales,
    10: numeros_primos
}

while True:
    mostrar_menu()
    opcion = int(input("Introduce el número de la función que deseas ejecutar: "))
    if opcion == 0:
        print("Saliendo del programa.")
        break
    elif opcion in funciones:
        resultado = funciones[opcion]()
        print(f"Resultado: {resultado}\n")
        input("Presiona cualquier tecla para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Opción no válida, por favor elige un número del 0 al 10.\n")
