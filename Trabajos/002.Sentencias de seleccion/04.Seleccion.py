#4. Escribe un programa que recoja dividendo y divisor, y realice su división

dividendo = float(input("Ingresa el dividendo: "))
divisor = float(input("Ingresa el divisor: "))

if divisor != 0:
    resultado = dividendo / divisor
    print(f"El resultado de la división es: {resultado}")
else:
    print("Error: El divisor no puede ser cero.")
