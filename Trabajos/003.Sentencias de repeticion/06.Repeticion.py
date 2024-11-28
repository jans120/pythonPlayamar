# 6. Escribe un programa que recoja un número de filas y columnas, y muestre una tabla con tantas filas y columnas como indicadas, numerando las celdas de izquierda a derecha y de arriba abajo. Por ejemplo, si se introducen 2 filas y 3 columnas, se debe mostrar:
    # 1 2 3
    # 4 5 6

filas = int(input("Ingresa el número de filas: "))
columnas = int(input("Ingresa el número de columnas: "))
contador = 1

for i in range(filas):
    for j in range(columnas):
        print(contador, end=' ')
        contador += 1
    print()  # Salto de línea después de cada fila
