def contar_vocales():
    texto = input("Introduce un texto: ")
    vocales = "aeiouAEIOU"
    return sum(1 for char in texto if char in vocales)

if __name__ == "__main__":
    print(contar_vocales())
