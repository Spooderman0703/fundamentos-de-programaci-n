# Alejandro Mariño Munguía. AL07285359. 23/08/2026.


numero_visitantes = int(input("¿Cuál es el número de visitantes?: "))

#Todas estas variables con valor en 0, son para que se les asigne un valor, que se definirá de acuerdo a todas ->
# -> las condiciones que serán establecidas en las siguientes partes del código.

total_acumulado = 0
tt = 0
descuento = 0
adultos_visitantes = 0
menores_visitantes = 0
menores_bebes = 0
adultos_mayores = 0
profesores = 0
estudiantes = 0

#En la siguiente línea, se define hasta que punto el ciclo "for" va a correr, utilizando el valor de "numero_visitantes" que fué definido en la primer pregunta.
for i in range(1, numero_visitantes+1):
    edad_visitante = float(input("¿Qué edad tiene el visitante?: "))
    tipo_visitante = str(input("¿Cuál es el tipo de visitante (adulto_mayor, profesor, estudiante o n/a)?: "))

    #A partir de aquí, se definen los descuentos respecto a la edad del visitante y el tipo de visitante que es.

    #Si el visitante tiene más de 18 años, su boleto puede ser candidato a uno de dos descuentos.
    if edad_visitante >= 18:
        adultos_visitantes += 1
        precio_boleto = 45
        #Si es de tipo "profesor", se hace un descuento al boleto del 10%.
        if tipo_visitante == ("profesor"):
            descuento = 0.1
            tt = precio_boleto - (45 * descuento)
            profesores += 1
            print(f"El precio original de este boleto es de: ${precio_boleto}, su descuento fue de ${45 * descuento}, y el boleto quedó en: ${tt}")
        #Si es de tipo "adulto_mayor", se hace un descuento al boleto del 12%.
        elif tipo_visitante == ("adulto_mayor") and edad_visitante >= 60:
            descuento = 0.12
            tt = precio_boleto - (45 * descuento)
            adultos_mayores += 1
            print(f"El precio original de este boleto es de: ${precio_boleto}, su descuento fue de ${45 * descuento}, y el boleto quedó en: ${tt}")
        #Si no cumple con ninguna de las condiciones, el costo del boleto seguirá siendo equivalente a su edad ingresada, sin descuentos.
        else:
            tt = precio_boleto
            print(f"El precio de este boleto fue de: ${precio_boleto}")

    #Si el visitante tiene entre 17 y 3 años, su boleto puede ser candidato a un único descuento.
    elif edad_visitante <= 17 and edad_visitante > 3:
        menores_visitantes+= 1
        precio_boleto = 30
        #Si es de tipo "estudiante", se hace un descuento al boleto del 10%.
        if tipo_visitante == ("estudiante"):
            descuento = 0.1
            tt = precio_boleto - (30 * descuento)
            estudiantes += 1
            print(f"El precio original de este boleto es de: ${precio_boleto}, su descuento fue de ${30 * descuento}, y el boleto quedó en: ${tt}")
        #Si no cumple con la condición, el costo del boleto será correspondiente a la edad ingresada, sin descuentos.
        else:   
            tt = precio_boleto
            print(f"El precio de este boleto fue de: ${precio_boleto}")

    #Si el visitante tiene entre 3 y 0 años, su boleto será gratis y se mostrará un mensaje que dice el valor del boleto.
    elif edad_visitante <= 3 and edad_visitante > 0:
        menores_bebes+= 1
        precio_boleto = 0
        print("Este boleto es gratis.")
        continue

    total_acumulado += tt

#En este último segmento del código, se muestran mensajes como el número de visitantes totales, el desglose del número de->
#-> tipos de visitantes y el total acumulado de todos los boletos de acuerdo a sus posibles descuentos aplicados.
print(f"\nNúmero de visitantes : {i}")
print(f"\nNúmero de mayores de edad: {adultos_visitantes}")
print (f"Número de menores de edad (3 a 17 años): {menores_visitantes}")
print (f"Número de menores de 3 años: {menores_bebes }")

print (f"\nNúmero de adultos mayores (60 años en adelante): {adultos_mayores}")
print (f"Número de profesores: {profesores}")
print (f"Número de estudiantes: {estudiantes}")

print(f"\nEl total acumulado de boletos: ${total_acumulado}")




