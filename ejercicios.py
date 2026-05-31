def calcular_total(gastos):
    total = 0
    for g in gastos:
        total = total + g
    return(total)

presupuesto = (30,000)
gastos_mes = [250, 80, 1200, 45, 300]
resultado = calcular_total(gastos_mes)


print(f"Gastaste ${resultado} este mes")
print(f"Te queda ${presupuesto - resultado}")
        
