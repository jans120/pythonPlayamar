# 10.Escribe un programa que recoja un número y muestre un triángulo formado por secuencias decrecientes de números impares. Por ejemplo, si se introduce el 5 se debe mostrar:
    # 1
    # 3 1
    # 5 3 1
    # 7 5 3 1
    # 9 7 5 3 1

numero = int(input("Introduzca un número: "))
impar = 1

for i in range(numero):
    impares = ""
    for j in range(impar, 0, -2):
        impares += str(j) + " "
    print(impares + " ")
    impar += 2
