def numeros():
    numeros_lista = []
    
    while True:
        num = int(input("Introduce un número (0 para terminar): "))
        if num == 0:
            break
        numeros_lista.append(num)

    print("Secuencia en el orden en que se introdujeron:")
    print(" ".join(map(str, numeros_lista)))

    print("Secuencia en orden creciente:")
    print(" ".join(map(str, sorted(numeros_lista))))

    print("Secuencia en orden decreciente:")
    print(" ".join(map(str, sorted(numeros_lista, reverse=True))))

def textos():
    textos_lista = []
    
    while True:
        texto = input("Introduce un texto (dejar vacío para terminar): ")
        if texto == "":
            break
        textos_lista.append(texto)

    print("Secuencia en el orden en que se introdujeron:")
    print(", ".join(textos_lista))

    print("Secuencia en orden alfabético:")
    print(", ".join(sorted(textos_lista)))

    print("Secuencia en orden alfabético inverso:")
    print(", ".join(sorted(textos_lista, reverse=True)))

def palindromo(s):
    s = s.replace(" ", "").lower()  # Ignorar espacios y minúsculas
    return s == s[::-1]

def verificar_palindromo():
    texto = input("Introduce un texto para comprobar si es un palíndromo: ")
    if palindromo(texto):
        print("El texto es un palíndromo.")
    else:
        print("El texto no es un palíndromo.")

def verificar_palindromo_comparacion():
    texto1 = input("Introduce el primer texto: ")
    texto2 = input("Introduce el segundo texto: ")
    
    modo = input("¿Considerar mayúsculas/minúsculas? (s/n): ").lower()
    
    if modo == 'n':
        texto1 = texto1.lower()
        texto2 = texto2.lower()
    
    if palindromo(texto1) and palindromo(texto2):
        if texto1 == texto2[::-1]:
            print("Uno es palíndromo del otro.")
        else:
            print("No son palíndromos entre sí.")
    else:
        print("Uno o ambos textos no son palíndromos.")

def main():
    while True:
        print("\nMENÚ DE OPCIONES")
        print("1) Números")
        print("2) Textos")
        print("3) Verificar palíndromo")
        print("4) Verificar palíndromo de otro texto")
        print("5) Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            numeros()
        elif opcion == '2':
            textos()
        elif opcion == '3':
            verificar_palindromo()
        elif opcion == '4':
            verificar_palindromo_comparacion()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()
