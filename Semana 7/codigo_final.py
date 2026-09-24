# Librerías utilizadas:
import time

# Requerimiento 2: Bienvenida dinámica.
def bienvenida(nombre_usuario):
    mensaje = "\nEstimado " + nombre_usuario + ", bienvenido al sistema oficial."    
    return mensaje

# Requerimiento 1: Identificación de usuario.
def id_usuario():
    nom_usuario = "alexxmm07"
    contr_usuario = 700203

    while True:
        name = input("Ingresa tu nombre de usuario: ")

        try:
            password = int(input("Ingresa tu contraseña (numérica): "))
        except ValueError:
            print("\n¡Error! : La contraseña debe contener únicamente valores numéricos.\n")
            continue

        if name == nom_usuario and password == contr_usuario:
            print("\nAcceso permitido.")
            # Requerimiento 2: Bienvenida dinámica.
            print(bienvenida(name))
            break
        else:
            print("\nAcceso denegado. Intenta de nuevo.\n")

# Requerimiento 3: Pantalla de Carga.
def pantalla_de_carga(segundos=5):
    duracion = min(segundos, 5) 
    
    print("\nIniciando el programa, por favor espere...")
    for i in range(duracion, 0, -1):
        print(f"\nCargando... [{i}s restantes]", end="\r")
        time.sleep(1)
    
    print("\n\n¡Sistema cargado con éxito! Dando paso al menú principal.\n")

# Requerimiento 6: Captura de fecha estructurada.
def capturar_fecha():
    print("\n--- REGISTRO DE FECHA DE OPERACIÓN ---")
    while True:
        try:
            dia = int(input("Ingresa el día (1-31): "))
            mes = int(input("Ingresa el mes (1-12): "))
            anio = int(input("Ingresa el año: "))

            if not (1 <= dia <= 31):
                print("Día fuera de rango. Debe ser entre 1 y 31.\n")
                continue
            if not (1 <= mes <= 12):
                print("Mes fuera de rango. Debe ser entre 1 y 12.\n")
                continue
            if anio < 2000 or anio > 2100:
                print("Año inválido. Ingrese un año de 4 dígitos válido.\n")
                continue

            fecha = (dia, mes, anio)
            print(f"Fecha registrada correctamente: {fecha[0]}/{fecha[1]}/{fecha[2]}\n")
            return fecha

        except ValueError:
            print("¡Error!: Todos los datos de la fecha deben ser números enteros.\n")

# Requerimiento 4: Menú como Matriz.
def mostrar_menu_principal(matriz):
    print("\n--- MENU PRINCIPAL ---")
    for opcion_matriz in matriz:
        print(f"{opcion_matriz[0]}. {opcion_matriz[1]}")

    while True:
        try:
            opcion = int(input("Selecciona una opción: "))
            return opcion
        except ValueError:
            print("Ingresaste un valor inválido. Intenta de nuevo.")
            continue

# Sub-función de cálculo para determinar precio base por tipo de vehículo y tipo de limpieza.
def obtener_precio_base(tipo_vehiculo, tipo_limpieza=1):
    if tipo_vehiculo == 1:
        return 70
    elif tipo_vehiculo == 2:
        return 120 if tipo_limpieza == 1 else 180
    elif tipo_vehiculo == 3:
        return 170 if tipo_limpieza == 1 else 250
    return 0

# Sub-función de cálculo para determinar costo de servicios extra de acueurdo al tipo de vehículo.
def obtener_costo_extras(tipo_vehiculo, servicio_extra):
    if servicio_extra == 3:
        return 0
    if tipo_vehiculo == 1:
        return 50 if servicio_extra == 1 else 75
    else:
        return 65 if servicio_extra == 1 else 100

# Sub-función de cálculo para determinar precio final, IVA aplicado y un posible descuento adicional.
def calcular_totales_transaccion(precio_base, costo_extras, tiene_inapam):
    subtotal = precio_base + costo_extras

    if tiene_inapam.lower() == "si":
        descuento_porcentaje = 0.20
    elif subtotal >= 300:
        descuento_porcentaje = 0.10
    else:
        descuento_porcentaje = 0.0

    monto_descuento = subtotal * descuento_porcentaje
    subtotal_con_descuento = subtotal - monto_descuento
    monto_iva = subtotal_con_descuento * 0.16
    total_final = subtotal_con_descuento + monto_iva

    return (subtotal, monto_descuento, monto_iva, total_final)

# Función orquestradora de registro de ventas.
def registrar_cliente_consumo(fecha_actual):

    print("\n--- REGISTRO DE CONSUMO DE CLIENTE ---")

    try:
        tipo_vehiculo = int(input("Tipo de vehículo (1. Motocicleta, 2. Sedán, 3. SUV/Camioneta): "))
        if tipo_vehiculo not in [1, 2, 3]:
            print("Opción de vehículo fuera de rango.")
            return
    except ValueError:
        print("Opción inválida. Debe ingresar un número.")
        return

    tipo_limpieza = 1
    if tipo_vehiculo in [2, 3]:
        try:
            tipo_limpieza = int(input("Tipo de limpieza (1. Básica, 2. Profunda): "))
        except ValueError:
            print("Opción inválida. Debe ingresar un número.")
            return
    else:
        print("Las motocicletas aplican únicamente para limpieza básica.")

    try:
        extras = int(input("Servicios extras (1. Encerado, 2. Lavado de motor, 3. Ninguno): "))
    except ValueError:
        print("Opción inválida. Debe ingresar un número.")
        return

    try:
        tiene_inapam = input("¿El cliente tiene credencial de INAPAM? (si/no): ").strip()
    except ValueError:
        print('Opción inválida. Debe ingresar "si"/"no".')
        return
    
    precio_base = obtener_precio_base(tipo_vehiculo, tipo_limpieza)
    costo_extras = obtener_costo_extras(tipo_vehiculo, extras)
    
    subtotal, descuento, iva, total = calcular_totales_transaccion(precio_base, costo_extras, tiene_inapam)

# Sub-menú para "Gestión de Operaciones"
def menu_operaciones(fecha_actual):
    while True:
        print("\n--- MENU DE OPERADOR ALEX QUICKWASH ---")
        print("1. Registrar cliente y consumo.")
        print("2. Reporte final del día.")
        print("3. Regresar al Menú Principal.")
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("\n¡Error! : Ingresa un opción válida.\n")
            continue

        if opcion == 1:
            print(f"\n[Registrando venta para la fecha: {fecha_actual[0]}/{fecha_actual[1]}/{fecha_actual[2]}]")
            registrar_cliente_consumo(fecha_actual)

        elif opcion == 2:
            # mostrar_reporte_dia()
            pass
        elif opcion == 3:
            print("\nRegresando al menú principal...")
            break
        else:
            print("\nOpción fuera de rango. Intenta de nuevo.\n")

# Bloque fundamental para inicio de sistema.
def ejecutar_sistema(fecha_actual):
    matriz_menu = [
        [1, "Gestión de Operaciones"],
        [2, "Gestión de Archivos"],
        [3, "Salir"]
    ]

    while True:
        opcion_principal = mostrar_menu_principal(matriz_menu)
        if opcion_principal == 1:
            menu_operaciones(fecha_actual)
        elif opcion_principal == 2:
            menu_archivos()
        elif opcion_principal == 3:
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecución y Convocación de funciones.
id_usuario()
pantalla_de_carga(5)
fecha_sistema = capturar_fecha()
ejecutar_sistema(fecha_sistema)
