# 4. Escribe un programa que recoja un número y muestre un triángulo. Por ejemplo, si se ha introducido el valor 5, se debe mostrar:
    # *
    # **
    # ***
    # ****
    # *****

numero = int(input("Ingresa un número: "))
for i in range(1, numero + 1):
    print('*' * i)

