def multiplication_table(n):

    for i in range(1, 11):
        result = n * i
        print(f"{n} x {i} = {result}")

n = int(input("Ingresa el numero de tu tabla de multiplicar: "))
multiplication_table(n)
