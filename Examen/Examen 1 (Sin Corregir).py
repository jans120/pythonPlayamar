# Juan David olivera
# 23/10/2024



def remplazarVocales():

    frase = input("Introduce una frase: ")
    vocales = "aeiouAEIOU"
    fraseReemplazada = ''.join('*' if letra in vocales else letra for letra in frase)
    print(fraseReemplazada)    

     
def numeroMayor():
    cantidad = int(input("¿Cuántos números vas a introducir? "))
    numeros = []
    for i in range(cantidad):
        numero = int(input(f"Introduce el número {i + 1}: "))
        if i > 0 and numero <= numeros[-1]:
            print("El número no es mayor que el anterior.")
            numeros.append(numero)

    print("Números introducidos:", numeros)



def palabraLarga():
    frase = input("introduce la frase: ")
    palabra = frase.split
    palabraLarga = palabra[0]
    i = 1
    for i in palabra:
        if palabra[i] > palabra[i-1]:
            palagraLarga = i
    print(palabraLarga)



def rectanguloInpar():
    try:
        filas = int(input("\nIntroduce el numero de filas: "))
        columnas = int(input("Introduce el numero de columnas: "))
        impares = [i for i in range(99, 0, -2)]

        if filas*columnas>len(impares):
            print(f"No hay suficientes numeros impares para llenar el rectangulo")
            return
        
        print("n\Rectangulo de numeros impares:")
        
        for i in range(filas):
            for j in range(columnas):
                print(f"{impares[i*columnas+j]:2d}", end=" ")
            print()
    
    except ValueError:
        print("Entrada invalida. Por favor, introduce datos validos.")

def contarCaracteres():
    palabra = input("introduce la palabra: ")
    for i in palabra:
        print()
        # no se hacer este me estoy liando


def mostrar_menu():
        print("\nMENÚ DE OPCIONES")
        print("MENÚ DE OPCIONES")
        print("a) Reemplazar vocales de una frase ")
        print("b) Mensaje cuando el numero introducido no sea mayor que el primero")
        print("c) Encontrar la primera palabra más larga")
        print("d) Mostrar rectángulo con números impares entre 0 y 100")
        print("e) Contar la aparición de cada carácter en una palabra")
        print("h) Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").lower()
        if opcion == 'a':
            remplazarVocales()
        elif opcion == 'b':
            numeroMayor()
        elif opcion == 'c':
            palabraLarga() 
        elif opcion == 'd':
            rectanguloInpar()
        elif opcion == 'e':
            contarCaracteres()
        elif opcion == 'h':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")
        
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()