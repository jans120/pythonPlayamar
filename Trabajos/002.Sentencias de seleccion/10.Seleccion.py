# 10.Escribe un programa que a partir de información de un donante determine si puede donar sangre. Las condiciones para donar son:
    # a. No se debe donar en ayunas.
    # b. Edad: Comprendida entre los 18 y 65 años.
    # c. Peso: Superior a 50kg.
    # d. Tensión arterial: dentro de límites adecuados para la extracción.
        # i. Tensión diastólica (baja): entre 50mm Hg y 100 mm Hg
        # ii. Tensión sistólica (alta): entre 90mm y 180mm Hg
    # e. Pulso (frecuencia cardiaca): entre 50 y 110 pulsaciones
    # f. Valores de hemoglobina:
        # i. En hombres: superior a 13,5 gramos por litro
        # ii. En mujeres: superior a 12,5 gramos por litro.
    # g. Plaquetas: más de 150.000 cc
    # h. Proteínas totales: más de 6 gr/dl.

edad = int(input("Ingresa tu edad: "))
peso = float(input("Ingresa tu peso (kg): "))
tension_diastolica = float(input("Ingresa la tensión diastólica (mm Hg): "))
tension_sistolica = float(input("Ingresa la tensión sistólica (mm Hg): "))
pulso = int(input("Ingresa la frecuencia cardiaca (pulsaciones): "))
hemoglobina = float(input("Ingresa los gramos de hemoglobina por litro: "))
plaquetas = int(input("Ingresa el número de plaquetas (cc): "))
proteinas = float(input("Ingresa las proteínas totales (gr/dl): "))

if edad < 18 or edad > 65:
    print("No puede donar sangre: Edad fuera de rango.")
elif peso <= 50:
    print("No puede donar sangre: Peso insuficiente.")
elif tension_diastolica < 50 or tension_diastolica > 100:
    print("No puede donar sangre: Tensión diastólica fuera de límites.")
elif tension_sistolica < 90 or tension_sistolica > 180:
    print("No puede donar sangre: Tensión sistólica fuera de límites.")
elif pulso < 50 or pulso > 110:
    print("No puede donar sangre: Pulso fuera de límites.")
elif (hemoglobina < 13.5 and hemoglobina < 12.5) or plaquetas <= 150000 or proteinas <= 6:
    print("No puede donar sangre: Valores de hemoglobina, plaquetas o proteínas fuera de límites.")
else:
    print("Puede donar sangre.")
