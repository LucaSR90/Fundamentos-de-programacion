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

if __name__ == "__main__":
    print(numeros_primos())
