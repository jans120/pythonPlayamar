# 5. Escribe un programa que calcule el precio de entrada a un museo a partir de la edad del visitante, teniendo en cuenta que:
#     a. Menores de 5 años entran gratis.
#     b. Niños entre 5 años y 18 (sin llegar a los 18) pagan 3€.
#     c. Mayores de edad hasta los 65 (sin llegar a los 65) pagan 6€.
#     d. Jubilados entran gratis.

edad = int(input("Ingresa la edad del visitante: "))

if edad < 5:
    print("Entrada gratuita.")
elif 5 <= edad < 18:
    print("El precio de la entrada es: 3€")
elif 18 <= edad < 65:
    print("El precio de la entrada es: 6€")
else:
    print("Entrada gratuita para jubilados.")

