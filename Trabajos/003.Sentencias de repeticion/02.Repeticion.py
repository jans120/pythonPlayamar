# 2. Escribe un programa que recoja un número y calcule su factorial.

numero = int(input("Ingresa un número: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print(f"El factorial de {numero} es: {factorial}")
