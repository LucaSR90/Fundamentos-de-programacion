#12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.

number = int(input("Elige un numero de 3 digitos: "))
sfac = number
factorial = number
if number>=100 and number<=999:
    while factorial > 0:
        sfac = factorial %10
        factorial //=10
        if sfac == 1:
            break
    if sfac == 1:
        print("Este numero de 3 digitos si tiene el numero 1")
    else:
        print("Este numero de 3 digitos no contiene ningun 1")
else:
    print("No es un numero de 3 digitos")