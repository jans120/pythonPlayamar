# 3. Escribe un programa que recoja números por teclado hasta que se introduzca el valor cero. A continuación, debe mostrar el número de valores introducidos, el valor mínimo introducido, el máximo, la suma de todos ellos y su media aritmética (todos los cálculos sin contar el cero)

contador = 0
suma = 0
valores = []

while True:
    numero = float(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    valores.append(numero)
    contador += 1
    suma += numero

if contador > 0:
    minimo = min(valores)
    maximo = max(valores)
    media = suma / contador
    print(f"Números introducidos: {contador}")
    print(f"Valor mínimo: {minimo}")
    print(f"Valor máximo: {maximo}")
    print(f"Suma total: {suma}")
    print(f"Media aritmética: {media}")
else:
    print("No se introdujeron valores.")
