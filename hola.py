print("Ejercicio 2")

number = float(input())

if number > 0:
    print(f"{number} es positivo")
elif number < 0:
    print(f"{number} es negativo")
else:
    print(f"{number} es cero")

if number % 2 == 0:
    print(f"{number} es par")
else:
    print(f"{number} es impar")