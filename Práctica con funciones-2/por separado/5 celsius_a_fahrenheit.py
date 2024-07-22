def max_de_tres():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    c = float(input("Introduce el tercer número: "))
    return max(a, b, c)

if __name__ == "__main__":
    print(max_de_tres())
