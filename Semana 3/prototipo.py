# Borrador de avance de proyecto.
# Avance enfocado en punto #1 del menú de operador, es decir, registro de clientes y su consumo.


while True:
    # Menú para operador.
    print("--- MENU DE OPERADOR ALEX QUICKWASH ---")
    print("1. Registrar cliente y consumo.")
    print("2. Reporte final del día. ")
    print("3. Salir.")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        print("--- MENU DE REGISTROS ---")
        #nombre_cliente = input("Nombre del cliente: ")     Cambiar esta línea por acumulador para registrar número de clientes.
        tipo_vehiculo = int(input("Tipo de vehículo (1. Motocicleta, 2. Sedán, 3. SUV/Camioneta): "))
        # Condicionales si el tipo de vehículo es "Motocicleta"
        if tipo_vehiculo == 1:
            print("Las motocicletas son solamente aplicables para la limpieza básica.")
            precio_base = 70
            # Servicios extra de una motocicleta.
            extras = int(input("Servicios extras (1. Encerado, 2. Lavado de motor, 3. Ninguno): "))
            if extras == 1:
                costo_extras = 50
            elif extras == 2:
                costo_extras = 75
            elif extras == 3:
                costo_extras = 0
                continue
            subtotal = precio_base + costo_extras
            tiene_inapam = input(print("¿El cliente tiene credencial de INAPAM? (si/no): "))
            if tiene_inapam == ("si"):
                descuento = .20
                subtotal = subtotal - (subtotal * descuento)
            elif tiene_inapam == ("no"):
                if (subtotal >= 300):
                    descuento = .10
                    subtotal = subtotal - (subtotal * descuento)
                elif (subtotal <300):
                    continue
            # Cáluclo y suma de IVA después del subtotal y un posible descuento.
            iva = .16
            total_cliente = subtotal - (subtotal * iva)

        # Condicionales si el tipo de vehículo es "Sedán"
        if tipo_vehiculo == 2:
            tipo_limpieza = int(input("Tipo de limpieza (1. Básica, 2. Profunda): "))
            if tipo_limpieza == 1:
                precio_base = 120
            elif tipo_limpieza == 2:
                precio_base = 180
            extras = int(input("Servicios extras (1. Encerado, 2. Lavado de motor, 3. Ninguno): "))
            if extras == 1:
                costo_extras = 65
            elif extras == 2:
                costo_extras = 100
            elif extras == 3:
                costo_extras = 0
                continue
            subtotal = precio_base + costo_extras
            tiene_inapam = input(print("¿El cliente tiene credencial de INAPAM? (si/no): "))
            if tiene_inapam == ("si"):
                descuento = .20
                subtotal = subtotal - (subtotal * descuento)
            elif tiene_inapam == ("no"):
                if (subtotal >= 300):
                    descuento = .10
                    subtotal = subtotal - (subtotal * descuento)
                elif (subtotal <300):
                    continue
                # Cáluclo y suma de IVA después del subtotal y un posible descuento.
                iva = .16
                total_cliente = subtotal - (subtotal * iva)

        # Condicionales si el tipo de vehículo es "SUV/Camioneta"
        if tipo_vehiculo == 3:
            tipo_limpieza = int(input("Tipo de limpieza (1. Básica, 2. Profunda): "))
            if tipo_limpieza == 1:
                precio_base = 170
            elif tipo_limpieza == 2:
                precio_base = 250
            extras = int(input("Servicios extras (1. Encerado, 2. Lavado de motor, 3. Ninguno): "))
            if extras == 1:
                costo_extras = 65
            elif extras == 2:
                costo_extras = 100
            elif extras == 3:
                costo_extras = 0
                continue
            subtotal = precio_base + costo_extras
            tiene_inapam = input(print("¿El cliente tiene credencial de INAPAM? (si/no): "))
            if tiene_inapam == ("si"):
                descuento = .20
                subtotal = subtotal - (subtotal * descuento)
            elif tiene_inapam == ("no"):
                if (subtotal >= 300):
                    descuento = .10
                    subtotal = subtotal - (subtotal * descuento)
                elif (subtotal <300):
                    continue
                # Cáluclo y suma de IVA después del subtotal y un posible descuento.
                iva = .16
                total_cliente = subtotal - (subtotal * iva)

    elif opcion == 2:
        print(f"Ventas acumuladas del dia: $")

    elif opcion == 3:
        print("Cerrando el sistema del dia.")
        break
    else:
        print("Opcion invalida.")