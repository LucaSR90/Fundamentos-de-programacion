def es_palindromo():
    palabra = input("Introduce una palabra o frase: ")
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

if __name__ == "__main__":
    print(es_palindromo())
