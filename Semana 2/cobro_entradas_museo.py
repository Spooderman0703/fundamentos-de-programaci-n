# Alejandro Mariño Munguía. AL07285359. 23/08/2026.



numero_visitantes = int(input("¿Cuál es el número de visitantes?"))

total_acumulado = 0

tt = 0

descuento = 0

adultos_visitantes = 0
menores_visitantes = 0
menores_bebes = 0

adultos_mayores = 0
profesores = 0
estudiantes = 0

total=0

for i in range(1, numero_visitantes+1):
    edad_visitante = float(input("¿Qué edad tiene el visitante?: "))
    tipo_visitante = str(input("¿Cuál es el tipo de visitante (adulto_mayor, profesor, estudiante o n/a)?"))

    # print(f"Edad del visitante {i} : {edad_visitante}")

    total = float(total + edad_visitante)

    if edad_visitante >= 18:
        adultos_visitantes += 1
        precio_boleto = 45
        if tipo_visitante == ("profesor"):
            descuento = 0.1
            tt = precio_boleto - (45 * descuento)
            profesores += 1
            print(f"El precio original de este boleto es de: ${precio_boleto}, su descuento fue de ${45 * descuento}, y el boleto quedó en: ${tt}")
        elif tipo_visitante == ("adulto_mayor") and edad_visitante >= 60:
            descuento = 0.12
            tt = precio_boleto - (45 * descuento)
            adultos_mayores += 1
            print(f"El precio original de este boleto es de: ${precio_boleto}, su descuento fue de ${45 * descuento}, y el boleto quedó en: ${tt}")
        else:
            print(f"El precio de este boleto fue de: ${precio_boleto}")
        


    elif edad_visitante <= 17 and edad_visitante > 3:
        menores_visitantes+= 1
        precio_boleto = 30
        if tipo_visitante == ("estudiante"):
            descuento = 0.1
            tt = precio_boleto - (30 * descuento)
            estudiantes += 1
            print(f"El precio original de este boleto es de: ${precio_boleto}, su descuento fue de ${30 * descuento}, y el boleto quedó en: ${tt}")
        else:   
            print(f"El precio de este boleto fue de: ${precio_boleto}")

    elif edad_visitante <= 3 and edad_visitante > 0:
        menores_bebes+= 1
        precio_boleto = 0
        print("Este boleto es gratis.")
        continue

    total_acumulado += precio_boleto

    
        
total = total / i


print(f"\nNúmero de visitantes : {i}")
print(f"\nNúmero de mayores de edad: {adultos_visitantes}")
print (f"Número de menores de edad (3 a 17 años): {menores_visitantes}")
print (f"Número de menores de 3 años: {menores_bebes }")

print (f"\nNúmero de adultos mayores (60 años en adelante): {adultos_mayores}")
print (f"Número de profesores: {profesores}")
print (f"Número de estudiantes: {estudiantes}")


print(f"\nEl total acumulado de boletos: ${total_acumulado}")




