# 9. Escribe un programa que recoja un año e indique si se trata de un año bisiesto o no. Un año es bisiesto si cumple estas condiciones:
    # a. El año es divisible por 4.
    # b. Si además el año es divisible por 100, debe ser también divisible por 400.

anio = int(input("Ingresa un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"{anio} es bisiesto.")
else:
    print(f"{anio} no es bisiesto.")
