# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

if __name__ == "__main__":
    # Llamada 1: Usando el descuento predeterminado (10%)
    monto_compra_1 = 500
    descuento_1 = calcular_descuento(monto_compra_1)
    monto_final_1 = monto_compra_1 - descuento_1

    print(f"Compra 1:")
    print(f"Monto total: ${monto_compra_1:.2f}")
    print(f"Descuento aplicado (10%): ${descuento_1:.2f}")
    print(f"Monto final a pagar: ${monto_final_1:.2f}\n")

    # Llamada 2: Usando un descuento personalizado (20%)
    monto_compra_2 = 800
    porcentaje_descuento_2 = 20
    descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
    monto_final_2 = monto_compra_2 - descuento_2

    print(f"Compra 2:")
    print(f"Monto total: ${monto_compra_2:.2f}")
    print(f"Descuento aplicado ({porcentaje_descuento_2}%): ${descuento_2:.2f}")
    print(f"Monto final a pagar: ${monto_final_2:.2f}")