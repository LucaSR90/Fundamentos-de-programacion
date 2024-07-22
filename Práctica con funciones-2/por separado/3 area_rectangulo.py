def es_par_o_impar():
    numero = int(input("Introduce un número: "))
    return "Par" if numero % 2 == 0 else "Impar"

if __name__ == "__main__":
    print(es_par_o_impar())
