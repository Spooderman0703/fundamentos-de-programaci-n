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


def menu_principal():
    numeros = (1234, 4567, 7890, 1357, 2468)
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Tuplas\n2. Diccionarios\n3. Excepciones\n4. Strings\n5. Finalizar")
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            gestionar_tuplas(numeros)
        elif opcion == 5:
            print("Saliendo del programa...")
            break

menu_principal()