#2. Escribe un programa que recoja un número por teclado y muestre el día de la semana que es (1 = Lunes, 2 = Martes...). En caso de introducir un número incorrecto, mostrará el mensaje “Día de la semana incorrecto”.

dia = int(input("Ingresa un número del 1 al 7: "))
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("Día de la semana incorrecto.")
