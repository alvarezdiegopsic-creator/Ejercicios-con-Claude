print("Gestor de gastos personales")

credito_de_santander = 338.33
credito_de_banbajio = 141.23

ingreso_quincenal = float(input("Ingrese su ingreso quincenal: "))
gastos_del_día = float(input("Ingrese sus gastos del día: "))
gastos_de_transporte = float(input("Ingrese sus gastos de transporte: "))
meta_de_ahorro = float(input("Ingrese su meta de ahorro: "))

gastos_hormiga = 0.0
tuvo_gastos_hormiga = input("¿Tuvo gastos hormiga? (sí/no): ").strip().lower()
if tuvo_gastos_hormiga == "sí":
    gastos_hormiga = float(input("Ingrese el monto total de sus gastos hormiga: "))

total_gastos = gastos_del_día + gastos_de_transporte + gastos_hormiga + credito_de_santander + credito_de_banbajio
saldo_final = ingreso_quincenal - total_gastos
porcentaje = (saldo_final / ingreso_quincenal) * 100

if saldo_final <= 0:
    print("No estás ahorrando, ¡Reduce tus gastos!")
elif saldo_final <= 1000:
    print("Estás ahorrando, pero podrías mejorar. ¡Sigue así!")
else:
    print("¡Excelente! Estás ahorrando una buena cantidad.")

print(f"Dinero restante: ${saldo_final:.2f}")
print(f"Total gastado: ${total_gastos:.2f}")
print(f"Porcentaje restante: {porcentaje:.2f}%")