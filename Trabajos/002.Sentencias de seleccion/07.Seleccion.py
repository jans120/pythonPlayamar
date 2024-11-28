# 7. Escribe un programa que recoja la hora del día y devuelva un saludo

hora = int(input("Ingresa la hora del día (0-23): "))

if 7 <= hora < 12:
    print("Buenos días")
elif 12 <= hora < 20:
    print("Buenas tardes")
else:
    print("Buenas noches")


