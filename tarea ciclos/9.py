#9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.

lise = []
for x in range(26,205):
    if x %10 == 6:
        lise.append(x)
print(f"La numeros terminados en 6 comprendidos entre 25 y 205 son {lise}") 