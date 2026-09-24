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

# Sub-menú para "Gestión de Operaciones"
def menu_operaciones():
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
            registrar_cliente_consumo()
        elif opcion == 2:
            mostrar_reporte_dia()
        elif opcion == 3:
            print("\nRegresando al menú principal...")
            break
        else:
            print("\nOpción fuera de rango. Intenta de nuevo.\n")

# Bloque fundamental para inicio de sistema.
def ejecutar_sistema():
    matriz_menu = [
        [1, "Gestión de Operaciones"],
        [2, "Gestión de Archivos"],
        [3, "Salir"]
    ]

    while True:
        opcion_principal = mostrar_menu_principal(matriz_menu)
        if opcion_principal == 1:
            menu_operaciones()
        elif opcion_principal == 2:
            menu_archivos()
        elif opcion_principal == 3:
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Convocación de Funciones.
id_usuario()
pantalla_de_carga(5)
ejecutar_sistema()
