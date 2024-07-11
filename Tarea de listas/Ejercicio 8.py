# 8.Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.
lisa = []
lise = []
for x in range (1,11):
    num = int(input(f"Digita el numero {x}: "))
    lisa.append(num)
    if num<0:
        lise.append(num)
print(f" El la lista se encuentra {len(lise)} numeros negativos ")
print (lisa)