#3. Escribe un programa que lea tres números y que muestre los números mayor y menor.

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))
numero3 = float(input("Ingresa el tercer número: "))

mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
