def suma_lista(valores):
    total = 0
    for i in valores:
        total += i
    return total

def gestionar_tuplas(numeros):
    print("\n--- SUBMENÚ TUPLAS ---")
    print("1. Ver elementos.")
    print("2. Ver tercer elemento.")
    print("3. Agregar elementos, ordenar, mostrar y sumar valores de nueva tupla.")
    print("4. Sumar elementos de tupla original.")
    
    sub_opcion = int(input("Selecciona una opción: "))
    
    if sub_opcion == 1:
        print(f"Los elementos son: {numeros}")
    elif sub_opcion == 2:
        print(f"El tercer elemento es: {numeros[2]}")
    elif sub_opcion == 3:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        nueva_tupla = numeros + (num1, num2)
        lista_ordenada = sorted(list(nueva_tupla), reverse=True)
        print(f"Nueva lista ordenada: {lista_ordenada}")
        print(f"Suma de la nueva tupla: {suma_lista(lista_ordenada)}")
    elif sub_opcion == 4:
        print(f"La suma total de la tupla orignial es: {suma_lista(numeros)}")

def buscar_telefono(contactos, nombre):
    return contactos.get(nombre, None)

def gestionar_diccionarios(contactos):

    print("\n--- SUBMENÚ DICCIONARIOS ---")
    print("1. Mostrar elementos de diccionario/directorio.")
    print("2. Añadir nuevo contacto (nombre y número telefónico).")
    print("3. Mostrar todos los nombres del directorio.")    
    print("4. Buscar nombre y mostrar número telefónico.")
    
    sub_opcion = int(input("Selecciona una opción: "))
    
    if sub_opcion == 1:
        print(f"Directorio actual: {contactos}")
    elif sub_opcion == 2:
        nuevo_nombre = input("Ingresa el nombre del contacto: ")
        nuevo_num_tel = int(input("Ingresa su número telefónico: "))
        contactos[nuevo_nombre] = nuevo_num_tel
        print(f"Se agregó al directorio el contacto {nuevo_nombre}, con su número {nuevo_num_tel}")
    elif sub_opcion == 3:
        print("Los contactos registrados del directorio base son: ")
        for n in contactos.keys():
            print(n, end=", ")
    elif sub_opcion == 4:
        buscar_nombre = input("Ingresa el nombre del contacto que buscas: ")
        telefono = buscar_telefono(contactos, buscar_nombre)

        if telefono:
            print(f"Número de {buscar_nombre} encontrado. Su número es: {telefono}")
        else:
            print("Contacto y número no encontrados.")

def calcular_operaciones():
    try:
        num1 = int(input("Ingresa el primer número entero: "))
        num2 = int(input("Ingresa el segundo número entero: "))
        suma = num1 + num2
        print(f"La suma de {num1} y {num2} es: {suma}")
        division = num1 / num2
        print(f"La división de {num1} entre {num2} es: {division:}")

    except ValueError:
        print("Error: Ingresaste valores inválidos.")
        
    except ZeroDivisionError:
        print("Error: No es posible una división entre 0.")
        
def gestionar_excepciones():
    print("\n--- SUBMENÚ EXCEPCIONES ---")
    print("1. Ejecutar pruebas de ingreso y división de números.")
    print("2. Regresar al menú principal.")
    
    sub_opcion = int(input("Selecciona una opción: "))
    
    if sub_opcion == 1:
        calcular_operaciones()
    elif sub_opcion == 2:
        print()

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def gestionar_strings():
    mensaje = "Arriba el Real Madrid y abajo el Barça"

    print("\n--- SUBMENÚ STRINGS ---")
    print("1. Mostrar longitud del mensaje.")
    print("2. Convertir mensaje a mayúsculas.")
    print("3. Reemplazo de palabra.")
    print("4. Cantidad de palabras totales.")
    print("5. Mostrar mensaje actual.")

    sub_opcion = int(input("Selecciona una opción: "))

    if sub_opcion == 1:
        print(f"Longitud del texto (caracteres): {len(mensaje)}")

    elif sub_opcion == 2:
        print(f"Mensaje en mayúsculas: {mensaje.upper()}")

    elif sub_opcion == 3:
        palabra_origen = input("Palabra que deseas buscar: ")
        palabra_nueva = input("Palabra por la que deseas reemplazar: ")

        if palabra_origen in mensaje:
            mensaje_modificado = mensaje.replace(palabra_origen, palabra_nueva)
            print(f"Mensaje actualizado: {mensaje_modificado}")
        else:
            print(f"La palabra '{palabra_origen}' no se encontró.")

    elif sub_opcion == 4:
        total_palabras = contar_palabras(mensaje)
        print(f"El mensaje contiene {total_palabras} palabras.")

    elif sub_opcion == 5:
        print(f"Mensaje actual: \"{mensaje}\"\n")



def menu_principal():
    numeros = (1234, 4567, 7890, 1357, 2468)
    contactos = {
        "Dano" : 4461319445,
        "Iris" : 4428100553,
        "Ulises" : 4427510326
    }
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Tuplas\n2. Diccionarios\n3. Excepciones\n4. Strings\n5. Finalizar")
        opcion = int(input("Selecciona una opción (1 - 5): "))
        
        if opcion == 1:
            gestionar_tuplas(numeros)
        elif opcion == 2:
            gestionar_diccionarios(contactos)
        elif opcion == 3:
            gestionar_excepciones()
        elif opcion == 4:
            gestionar_strings()
        elif opcion == 5:
            print("Programa finalizado.")
            break
        else:
            print("Opción invalida, intenta de nuevo.")

menu_principal()