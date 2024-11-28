#Ejercicios basicos 

valor = int(input("Que ejercicio quieres resolver?"))
match valor:

    case 1:
        valor = input("Introduce un valor")
        print("El valor introducido es: " + valor + " y es de tipo " , type(valor)) 

    case 2:
        a = int(input("Inserta el primer valor"))
        b = int(input("Inserta el segundo valor"))
        print("Suma: " + str(a+b) + " Resta: " +str(a-b) + " Multiplicación: " +str(a*b) )
        print("División real: " + str(a/b) + " División entera " +str(a%b) + " Potencia: " + str(a**b))

    case 3:
        nombre = input("Cual es tu nombre?")
        apellidos = input("Y tus apellidos?")
        print("Bienvenido " +nombre + " " + apellidos)

    case 4:
        a = int(input("Inserte el primer valor"))
        b = int(input("Inserte el segundo valor"))
        c = int(input("Inserte el tercer valor"))
        media = (a +b +c) / 3
        print("La media de los 3 numeros es: " + str(media))

    case 5:
        valor = int(input("Ingrese el numero a saber su valor absoluto"))
        valor_absoluto = abs(valor)
        print("El valor absoluto de " +str(valor) + " es " + str(valor_absoluto))

    case 6:
        a = int(input("1 trimestre"))
        a_total = a * 0.2
        b = int(input("2 trimestre"))
        b_total = b * 0.35
        c = int(input("3 trimestre"))
        c_total = c * 0.45

        total = a_total + b_total + c_total
        print("La nota total es " + str(total))

    case 7:
        numero = int(input("Qué numero quieres ver en su estado binario"))
        numero_bin = bin(numero)
        print("El numero " +numero+ " en binario es " +numero_bin)

    case 8:
        texto = input("Dime un texto o palabra")
        print(texto * 5)

    case 9:
        texto = input("Dime una palabra para darte su longitud")
        longitud = len(texto)
        print(texto + " tiene una longitud de " + str(longitud))

    case 10:
        edad = int(input("Cual es tu edad"))
        print("Tu edad en 5 años será " + str((edad +5)) + " en 10 años será " + str((edad + 10)) + " y en 15 años " + str((edad + 15)) )

    case _:
        print("Valor no existente, vuelve a ejecutar el programa")


