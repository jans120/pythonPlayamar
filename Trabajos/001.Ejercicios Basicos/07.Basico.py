#7. Escribe un programa que recoja un número y muestre su representación en código binario.

numero = int(input("Qué numero quieres ver en su estado binario"))
numero_bin = bin(numero)
print("El numero " +numero+ " en binario es " +numero_bin)