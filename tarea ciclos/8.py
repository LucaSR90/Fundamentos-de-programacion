#8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200.

lise = []
for x in range(21,200):
    if (x/2) %1 == 0:
        lise.append(x)
print(f"Los numeros pares comprendidos entre 20 y 200 son {lise}") 