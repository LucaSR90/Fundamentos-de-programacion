#15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.
z = 0
for x in range(1,21):
    x*=3
    z+=x
print(f" Los sumatoria de los primeros 20 multiplos de 3 es {z}")