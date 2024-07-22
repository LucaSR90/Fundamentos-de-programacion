def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_func():
    n = int(input("Introduce un número: "))
    return factorial(n)

if __name__ == "__main__":
    print(factorial_func())
