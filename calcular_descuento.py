def calcular_descuento(monto_total, porcentaje_descuento=0.12):
  descuento = monto_total * porcentaje_descuento
  return descuento


monto_compra1 = 150
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1
print("Monto del descuento 1:", descuento1)
print("Monto final a pagar después del descuento 1:", monto_final1)

monto_compra2 = 200
porcentaje_descuento2 = 0.15
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2
print("\nMonto del descuento 2:", descuento2)
print("Monto final a pagar después del descuento 2:", monto_final2)

