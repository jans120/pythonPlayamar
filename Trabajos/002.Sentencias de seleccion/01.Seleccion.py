#1. Escribe un programa que recoja un número e indique si se trata de un número par o impar.

numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

