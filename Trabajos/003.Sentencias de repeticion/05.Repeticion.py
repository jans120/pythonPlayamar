# 5. Escribe un programa que recoja un número por teclado y muestre los primeros cuadrados hasta llegar al número introducido. Por ejemplo, si se ha introducido el valor 5, se debe mostrar:
    # 1 4 9 16 25

numero = int(input("Ingresa un número: "))
for i in range(1, numero + 1):
    print(i ** 2, end=' ')
print()