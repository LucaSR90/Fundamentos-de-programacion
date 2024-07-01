#16. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.

number1 = int(input("Elige que cantidad de multiplos para 2?: "))
number2 = int(input("Elige que cantidad de multiplos para 5?: "))
z = 0
h = 0
for x in range(1,number1+1):
    x*=2
    z+=x

for y in range(1,number2+1):
    y*=5
    h+=y

z /=number1
h /=number2
if z>h:
    print(f"El promedio de los digitos de 2 que es {z} es mayor que el promedio de 5 que es  {h}")
else:
    print(f"El promedio de los digitos de 5 que es {h} es mayor que el promedio de 2 que es  {z}")