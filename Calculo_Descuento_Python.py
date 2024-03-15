# SEMANA 14
# Cálculo de Descuento en Compras

#Creación de la función
def calcular_descuento(monto_total, valor_porcen_descu=10):
  descuento = monto_total * valor_porcen_descu / 100
  return descuento


# Llamada a la función
llamada_funcion = calcular_descuento(10000)
print("El descuento es: ", llamada_funcion)

monto_total = float(input("Ingrese el monto total de las compras: "))
desc = 30
llamada_funcion = calcular_descuento(monto_total, desc)
print("Total de la compra: ", monto_total, "descuento del", desc, "% Descuento", llamada_funcion)


