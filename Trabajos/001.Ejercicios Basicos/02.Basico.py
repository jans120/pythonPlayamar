# 2. Escribe un programa que recoja dos números enteros por teclado y muestre los siguientes resultados: suma, resta, multiplicación, división real, división entera, resto de la división entera y potencia.

a = int(input("Inserta el primer número: "))
b = int(input("Inserta el segundo número: "))


print("Suma: " + str(a + b))
print("Resta: " + str(a - b))
print("Multiplicación: " + str(a * b))
print("División Real: " + str(a / b))
print("División Entera: " + str(a // b))
print("Resto División Entera: " + str(a % b))
print("Potencia: " + str(a ** b))