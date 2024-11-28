import random
import math

def mostrar_menu():
    print("MENÚ DE OPCIONES")
    print("a) Mostrar un rombo.")
    print("b) Adivinar un número.")
    print("c) Resolver una ecuación de segundo grado.")
    print("d) Tabla de números.")
    print("e) Cálculo del número factorial de un número.")
    print("f) Cálculo de un número de la sucesión de Fibonacci.")
    print("g) Tabla de multiplicar.")
    print("h) Salir")

def mostrar_rombo():
    while True:
        try:
            n = int(input("Introduce un número impar: "))
            if n % 2 == 1:
                break
            else:
                print("El número debe ser impar. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, introduce un número entero.")

    for i in range(n):
        if i <= n // 2:
            print('*' * (2 * i + 1))
        else:
            print('*' * (2 * (n - i - 1) + 1))

def adivinar_numero():
    numero_aleatorio = random.randint(1, 100)
    intento = 0
    print("Adivina el número entre 1 y 100.")
    
    while True:
        try:
            intento = int(input("Introduce tu número: "))
            if intento < numero_aleatorio:
                print("Es mayor.")
            elif intento > numero_aleatorio:
                print("Es menor.")
            else:
                print("¡Correcto! Has adivinado el número.")
                break
        except ValueError:
            print("Por favor, introduce un número entero.")

def resolver_ecuacion_segundo_grado():
    try:
        a = float(input("Introduce el coeficiente a: "))
        b = float(input("Introduce el coeficiente b: "))
        c = float(input("Introduce el coeficiente c: "))
        
        discriminante = b**2 - 4*a*c
        if discriminante > 0:
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            print(f"Las soluciones son x1 = {x1} y x2 = {x2}.")
        elif discriminante == 0:
            x = -b / (2 * a)
            print(f"La solución única es x = {x}.")
        else:
            print("No hay soluciones reales.")
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")
    
def tabla_numeros():
    try:
        filas = int(input("Introduce el número de filas: "))
        columnas = int(input("Introduce el número de columnas: "))
        tabla = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]
        for fila in tabla:
            print(fila)
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

def calcular_factorial_usuario():
    while True:
        try:
            n = int(input("Introduce un número para calcular su factorial: "))
            if n < 0:
                print("El factorial no está definido para números negativos.")
            else:
                print(f"El factorial de {n} es {calcular_factorial(n)}.")
                break
        except ValueError:
            print("Por favor, introduce un número entero.")

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def calcular_fibonacci_usuario():
    while True:
        try:
            n = int(input("Introduce la posición en la sucesión de Fibonacci: "))
            if n < 0:
                print("Por favor, introduce un número entero no negativo.")
            else:
                print(f"El número de Fibonacci en la posición {n} es {fibonacci(n)}.")
                break
        except ValueError:
            print("Por favor, introduce un número entero.")

def tabla_multiplicar():
    while True:
        try:
            n = int(input("Introduce un número para mostrar su tabla de multiplicar: "))
            print(f"Tabla de multiplicar del {n}:")
            for i in range(1, 11):
                print(f"{n} x {i} = {n * i}")
            break
        except ValueError:
            print("Por favor, introduce un número entero.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").lower()
        
        if opcion == 'a':
            mostrar_rombo()
        elif opcion == 'b':
            adivinar_numero()
        elif opcion == 'c':
            resolver_ecuacion_segundo_grado()
        elif opcion == 'd':
            tabla_numeros()
        elif opcion == 'e':
            calcular_factorial_usuario()
        elif opcion == 'f':
            calcular_fibonacci_usuario()
        elif opcion == 'g':
            tabla_multiplicar()
        elif opcion == 'h':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")
        
        input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
