def celsius_a_fahrenheit():
    celsius = float(input("Introduce la temperatura en grados Celsius: "))
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    print(celsius_a_fahrenheit())
