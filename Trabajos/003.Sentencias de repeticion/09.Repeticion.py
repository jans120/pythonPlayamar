# 9. Escribe un programa que recoja un número impar. Debe asegurarse de que sea impar, en caso de no serlo debe descartarlo y pedirlo de nuevo. Una vez tenga el número impar debe mostrar una pirámide de asteriscos cuya base es igual al número introducido. Por ejemplo, si se introduce el valor 7 se debe mostrar:
    # *
    # ***
    # *****
    # ******* <- base de la pirámide (7 asteriscos)

while True:
    numero = int(input("Ingresa un número impar: "))
    if numero % 2 != 0:
        break
    print("El número no es impar. Inténtalo de nuevo.")

for i in range(1, numero + 1, 2):
    print('*' * i)
