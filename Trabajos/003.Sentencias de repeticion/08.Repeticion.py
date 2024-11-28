# 8. Escribe un programa que recoja un número y calcule si es primo.

numero = int(input("Ingresa un número: "))
es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")
