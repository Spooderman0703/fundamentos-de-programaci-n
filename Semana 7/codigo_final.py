# Librerías utilizadas:
import time
import os
import pdb

# Ruta absoluta del directorio donde está el código principal.
ruta_proyecto = os.path.dirname(os.path.abspath(__file__))

# Requerimiento 5: Control de Inactividad del Usuario.
def inactividad(ultimo_acceso, limite_segundos=600):

    tiempo_actual = time.time()

    if (tiempo_actual - ultimo_acceso) >= limite_segundos:
        print(" ¡ALERTA DE SEGURIDAD! Inactividad detectada (10 min).")
        
        respuesta = input("¿Desea continuar en el sistema? (si/no): ").strip().lower()
        if respuesta != "si":
            return False  
            
    return True  

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

# Sub-función de cálculo para determinar costo de servicios extra de acuerdo al tipo de vehículo.
def obtener_costo_extras(tipo_vehiculo, servicio_extra):
    if servicio_extra == 3:
        return 0
    if tipo_vehiculo == 1:
        return 50 if servicio_extra == 1 else 75
    else:
        return 65 if servicio_extra == 1 else 100

# Requerimiento 9. Depuración técnica 
# Sub-función de cálculo para determinar precio final, IVA aplicado y un posible descuento adicional.
def calcular_totales_transaccion(precio_base, costo_extras, tiene_inapam):
    subtotal = precio_base + costo_extras

    if tiene_inapam.lower() == "si":
        descuento_porcentaje = 0.20
    elif subtotal >= 300:
        descuento_porcentaje = 0.10
    else:
        descuento_porcentaje = 0.0

    pdb.set_trace()

    monto_descuento = subtotal * descuento_porcentaje
    subtotal_con_descuento = subtotal - monto_descuento
    monto_iva = subtotal_con_descuento * 0.16
    total_final = subtotal_con_descuento + monto_iva

    return (subtotal, monto_descuento, monto_iva, total_final)

# Función para la obtención del último folio generado por tickets.
def ultimo_folio():

    ruta_archivo = os.path.join(ruta_proyecto, "ventas_acumuladas.txt")

    # Requerimiento 8. Control de Excepciones del Sistema.
    try:
        archivo = open(ruta_archivo, "r")
        lineas = archivo.readlines()
        archivo.close()
        return len(lineas)
    except FileNotFoundError:
        return 0

# Requerimiento 7. Persistencia en Archivos de texto.
# Función para generación de tickets individuales mediante archivo de texto.
def ticket_individual(fecha_actual, id_venta, tipo_vehiculo, tipo_limpieza, costo_extras, subtotal, descuento, iva, total):
    
    string_fecha = f"{fecha_actual[0]}/{fecha_actual[1]}/{fecha_actual[2]}"
    nombre_archivo = f"ticket_{id_venta}.txt"
    ruta_completa = os.path.join(ruta_proyecto, nombre_archivo)

    try:
        archivo = open(ruta_completa, "w")
        
        archivo.write("========================================\n")
        archivo.write("       ALEX QUICKWASH - TICKET          \n")
        archivo.write("========================================\n")
        archivo.write(f"Fecha de Operacion: {string_fecha}\n")
        archivo.write(f"Folio de Venta: #{id_venta}\n")
        archivo.write("----------------------------------------\n")
        archivo.write(f"Tipo de Vehiculo: {tipo_vehiculo}\n")
        archivo.write(f"Tipo de Limpieza: {tipo_limpieza}\n")
        archivo.write(f"Costo Servicios Extra: ${costo_extras:.2f}\n")
        archivo.write(f"Subtotal: ${subtotal:.2f}\n")
        archivo.write(f"Descuento Aplicado: -${descuento:.2f}\n")
        archivo.write(f"IVA (16%): +${iva:.2f}\n")
        archivo.write("----------------------------------------\n")
        archivo.write(f"TOTAL PAGADO: ${total:.2f}\n")
        archivo.write("========================================\n")
        
        archivo.close()
        print(f"[Sistema]: Ticket individual guardado exitosamente como '{nombre_archivo}'.")

    except PermissionError:
        print(f"¡Error de Permisos!: No se pudo crear el archivo {nombre_archivo}.")

# Función para anexar venta individual a reporte final.
def reporte_general(fecha_actual, id_venta, tipo_vehiculo, subtotal, descuento, iva, total):
    string_fecha = f"{fecha_actual[0]}/{fecha_actual[1]}/{fecha_actual[2]}"
    ruta_archivo = os.path.join(ruta_proyecto, "ventas_acumuladas.txt")

    # Requerimiento 8. Control de Excepciones del Sistema.
    try:
        archivo = open(ruta_archivo, "a")
        registro = f"FECHA: {string_fecha} | FOLIO: #{id_venta} | VEHICULO: {tipo_vehiculo} | SUBTOTAL: ${subtotal:.2f} | DESC: -${descuento:.2f} | IVA: +${iva:.2f} | TOTAL: ${total:.2f}\n"        
        archivo.write(registro)
        archivo.close()
            
    except PermissionError:
        print("¡Error de Permisos!: No se pudo actualizar la bitácora general de ventas.")

# Función orquestradora de registro de ventas.
def registrar_cliente_consumo(fecha_actual, contador_ventas):

    print("\n--- REGISTRO DE CONSUMO DE CLIENTE ---")

    try:
        tipo_vehiculo = int(input("Tipo de vehículo (1. Motocicleta, 2. Sedán, 3. SUV/Camioneta): "))
        if tipo_vehiculo not in [1, 2, 3]:
            print("Opción de vehículo fuera de rango.")
            return contador_ventas
    except ValueError:
        print("Opción inválida. Debe ingresar un número.")
        return contador_ventas

    tipo_limpieza = 1
    str_limpieza = "Básica"

    if tipo_vehiculo in [2, 3]:
        try:
            tipo_limpieza = int(input("Tipo de limpieza (1. Básica, 2. Profunda): "))
            if tipo_limpieza == 2:
                str_limpieza = "Profunda"
            elif tipo_limpieza != 1:
                print("Opción de limpieza fuera de rango.")
                return contador_ventas
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
            return contador_ventas
    else:
        print("Las motocicletas aplican únicamente para limpieza básica.")

    nombres_vehiculo = {1: "Motocicleta", 2: "Sedán", 3: "SUV/Camioneta"}
    str_vehiculo = nombres_vehiculo[tipo_vehiculo]

    try:
        extras = int(input("Servicios extras (1. Encerado, 2. Lavado de motor, 3. Ninguno): "))
        if extras not in [1, 2, 3]:
            print("Opción de servicio extra fuera de rango.")
            return contador_ventas
    except ValueError:
        print("Entrada inválida. Debe ingresar un número.")
        return contador_ventas

    try:
        tiene_inapam = input("¿El cliente tiene credencial de INAPAM? (si/no): ").strip()
    except ValueError:
        print('Opción inválida. Debe ingresar "si"/"no".')
        return
    
    precio_base = obtener_precio_base(tipo_vehiculo, tipo_limpieza)
    costo_extras = obtener_costo_extras(tipo_vehiculo, extras)
    
    subtotal, descuento, iva, total = calcular_totales_transaccion(precio_base, costo_extras, tiene_inapam)

    folio_actual = contador_ventas + 1

    ticket_individual(fecha_actual, folio_actual, str_vehiculo, str_limpieza, costo_extras, subtotal, descuento, iva, total)
    reporte_general(fecha_actual, folio_actual, str_vehiculo, subtotal, descuento, iva, total)
    print("¡Venta registrada exitosamente!")

    return folio_actual

# Sub-menú para "Gestión de Operaciones"
def menu_operaciones(fecha_actual):

    contador_ventas = ultimo_folio()

    while True:
        print("\n--- MENU DE OPERADOR ALEX QUICKWASH ---")
        print("1. Registrar cliente y consumo.")
        print("2. Regresar al Menú Principal.")
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("\n¡Error! : Ingresa un opción válida.\n")
            continue

        if opcion == 1:
            contador_ventas = registrar_cliente_consumo(fecha_actual, contador_ventas)
        elif opcion == 2:
            print("\nRegresando al menú principal...")
            break
        else:
            print("\nOpción fuera de rango. Intenta de nuevo.\n")

# Sub-función para mostrar catálogo de archivos .txt existentes
def catalogo_archivos():
    archivos_en_carpeta = os.listdir(ruta_proyecto)
    archivos_txt = [f for f in archivos_en_carpeta if f.endswith(".txt")]
    
    diccionario_archivos = {}
    
    print("\n--- CATALOGO DE ARCHIVOS DISPONIBLES (.txt) ---")
    if not archivos_txt:
        print("No se encontraron archivos de texto en el sistema.\n")
        return diccionario_archivos

    for indice, nombre_archivo in enumerate(archivos_txt, start=1):
        diccionario_archivos[indice] = nombre_archivo
        print(f"{indice}. {nombre_archivo}")

    return diccionario_archivos

# Sub-función para mostrar archivo seleccionado
def desplegar_archivo():
    elementos = os.listdir(ruta_proyecto)
    archivos_txt = [f for f in elementos if f.endswith(".txt")]
    
    if not archivos_txt:
        print("\n¡Error!: No existen archivos .txt disponibles para lectura en el sistema.\n")
        return

    diccionario_archivos = {i: archivo for i, archivo in enumerate(archivos_txt, start=1)}

    try:
        opcion = int(input("\nIngresa el número del archivo que deseas abrir: "))

        if opcion in diccionario_archivos:
            nombre_seleccionado = diccionario_archivos[opcion]
            ruta_completa = os.path.join(ruta_proyecto, nombre_seleccionado)

            archivo = open(ruta_completa, "r")
            contenido = archivo.read()
            archivo.close()

            print("\n" + "="*45)
            print(f"      DESPLIEGUE DE: {nombre_seleccionado}")
            print("="*45)
            print(contenido)
            print("="*45 + "\n")
        else:
            print(f"\n¡Error!: El número {opcion} no corresponde a ningún archivo válido.\n")

    except ValueError:
        print("\n¡Error!: Debes ingresar únicamente un número entero.\n")
    except FileNotFoundError:
        print("\n¡Error!: El archivo seleccionado no existe en el disco.\n")
    except PermissionError:
        print("\n¡Error!: No tienes permisos para leer este archivo.\n")

# Función para generar un reporte final acorde a número de tickets y datos individuales.
def resumen_ventas():
    
    ruta_archivo = os.path.join(ruta_proyecto, "ventas_acumuladas.txt")

    try:
        archivo = open(ruta_archivo, "r")
        lineas = archivo.readlines()
        archivo.close()

        if not lineas:
            print("\n[Sistema]: La bitácora de ventas acumuladas está vacía.\n")
            return

        print("\n" + "="*70)
        print("         ALEX QUICKWASH - REPORTE CONSOLIDADO DE VENTAS")
        print("="*70)

        total_ingresos = 0.0
        total_descuentos = 0.0
        total_iva = 0.0
        conteo_tickets = len(lineas)

        for linea in lineas:
            print(linea.strip())
            
            try:
                partes = linea.split("|")
                subtotal_str = partes[3].split("$")[1]
                desc_str = partes[4].split("$")[1]
                iva_str = partes[5].split("$")[1]
                total_str = partes[6].split("$")[1]

                total_descuentos += float(desc_str)
                total_iva += float(iva_str)
                total_ingresos += float(total_str)
            except (IndexError, ValueError):
                continue

        promedio_ticket = total_ingresos / conteo_tickets if conteo_tickets > 0 else 0.0

        print("-" * 70)
        print(f" Total de Servicios Realizados:  {conteo_tickets}")
        print(f" Total Descuentos Otorgados:    -${total_descuentos:.2f}")
        print(f" Total IVA Recaudado (16%):     +${total_iva:.2f}")
        print(f" Ticket Promedio por Cliente:    ${promedio_ticket:.2f}")
        print("-" * 70)
        print(f" INGRESOS TOTALES ACUMULADOS:    ${total_ingresos:.2f}")
        print("="*70 + "\n")

    except FileNotFoundError:
        print("\n¡Error!: Aún no existe el archivo 'ventas_acumuladas.txt'. Registre una venta primero.\n")
    except PermissionError:
        print("\n¡Error!: No tiene permisos para acceder a la bitácora general.\n")

# Sub-menú para "Gestión de Archivos"
def menu_archivos():
    while True:
        print("\n--- GESTION DE ARCHIVOS Y REPORTES ---")
        print("1. Desplegar archivos .txt del catálogo.")
        print("2. Desplegar contenido de archivo seleccionado.")
        print("3. Generar resumen de ventas.")
        print("4. Regresar al Menú Principal.")
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("\n¡Error!: Ingresa un número válido.\n")
            continue

        if opcion == 1:
            catalogo_archivos()
        elif opcion == 2:
            desplegar_archivo()
        elif opcion == 3:
            resumen_ventas()
        elif opcion == 4:
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

    ultimo_acceso = time.time()

    while True:
        opcion_principal = mostrar_menu_principal(matriz_menu)

        if not inactividad(ultimo_acceso):
            print("Cerrando sistema por inactividad...")
            break

        ultimo_acceso = time.time()

        if opcion_principal == 1:
            menu_operaciones(fecha_actual)
            ultimo_acceso = time.time()
        elif opcion_principal == 2:
            menu_archivos()
            ultimo_acceso = time.time()
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
