diccionario = {    
    "ANA": "555-123-4567",
    "CARLOS": "555-234-5678",
    "BEA": "555-345-6789",
    "DAVID": "555-456-7890",
    "ELENA": "555-567-8901",
    "FRANCISCO": "555-678-9012",
    "GABRIELA": "555-789-0123",
    "HECTOR": "555-890-1234",
    "ISA": "555-901-2345",
    "JAVI": "555-012-3456"}

def mostrarTelefonos():
    # Con este forma se puede copiar (devuelve una tupla)
    # mostrar = sorted(diccionario.items())

    # se puede mostrar sin guardar con un for
    for clave, valor in diccionario.items():
        print(clave, valor)

def mostrarOrden():
    # Con este forma se puede ordenar
    # ordenado = sorted(diccionario.items())

    # se pueden ordenar directamente en el for
    for clave, valor in sorted(diccionario.items()):
        print(clave, valor)

def anyadir():
    nombre = input("Dime el nombre: ")
    telefono = input("Dime el telefono: ")

    diccionario[nombre.upper()] = telefono

    # Mostrar el diccionario actualizado
    mostrarOrden()

def modificar():
    contacto = input("Que contacto quiere modificar?: ")
    contacto.upper()
    if contacto in diccionario:
        num = input("Introduce el numero: ")
        diccionario[contacto] = num
        mostrarOrden()
    else:
        print("No existe el contacto")

def buscarNum():
    num = input("Dime el numero a buscar: ")

    for nombre, telefono in diccionario.items():
        if telefono == num:
            print(f"El número {num} pertenece a {nombre}.")
            return
    

    # AUNQUE HE ENCONTRADO UN METODO INTERESANTE
    #  invertir el diccionario, es decir -> num : nombre

    # diccionario_invertido = dict(zip(diccionario.values(), diccionario.keys()))
    
    # Esto hace que podamos directamente buscar por el num ya que los hemos invertido

    # print(diccionario.get(num))

def eliminarContacto():
    contacto = input("Introduce el nombre: ")
    contacto = contacto.upper()
    if contacto in diccionario:
        filtroEliminado = diccionario.pop(contacto, "POR SI ACASO")
        print("Eliminado con exito")
        mostrarOrden()
    else:
        print("El contacto no existe")


def borrar():
    verificar = input("PARA ELIMINAR LOS CONTACTOS PULSE Y: ")
    if verificar.upper() == "Y":
        diccionario.clear()
        print("Se ha borrado con exito")
    else:
        print("Cancelando...")


def menu():
    while True:
        print("""MENÚ DE OPCIONES
a) Listado de teléfonos, usando el orden por defecto.
b) Listado de teléfonos por orden alfabético.
c) Añadir un nuevo contacto.
d) Modificar el teléfono de un contacto.
e) Buscar un número de teléfono.
f) Eliminar un contacto.
g) Borrar el listín telefónico.
h) Salir""")

        opcion = input("Selecciona una opcion: ").lower()
        print("\n")

        if opcion == 'a':
            mostrarTelefonos()
        elif opcion == 'b':
            mostrarOrden()
        elif opcion == 'c':
            anyadir()
        elif opcion == 'd':
            modificar()
        elif opcion == 'e':
            buscarNum()
        elif opcion == 'f':
            eliminarContacto()
        elif opcion == 'g':
            borrar()
        elif opcion == 'h':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción correcta.")
        print("\n")

if __name__ == "__main__":
    menu()