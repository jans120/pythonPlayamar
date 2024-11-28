# Juan David Olivera
# 27/11/2024

'''NOMBRE Y APELLIDOS:
Desarrolla un programa en Python que gestione un sistema de biblioteca.No hace falta que comentes cada cosa que realices pero sí lo que consideres debería saber otro compañero tuyo, para cuando te vayas de vacaciones y tu compañero debe manipular tu código. Este programa debe cumplir los siguientes requisitos:

1.Define una clase base Material que tenga atributos comunes a todos los materiales de la biblioteca, como:
id (único para cada material)
título
autor
año de publicación 

2.Crea dos clases que hereden de Material:

Libro: Incluye atributos adicionales como género (debe seleccionarse entre una lista predefinida: "Ficción", "No Ficción", "Terror", "Ciencia") y número de páginas (debe ser mayor a 0).

Revista: Incluye atributos adicionales como número de edición y mes de publicación (debe seleccionarse entre los meses válidos: "Enero", "Febrero", ..., "Diciembre")

3.Utiliza un diccionario para almacenar los materiales, donde la clave sea el id y el valor sea un objeto de tipo Libro o Revista.

4.Mantén una lista de todos los id existentes para verificar que no se repitan al agregar nuevos materiales.

5. Generar Estadísticas:debe devolver todos estos valores
Total de materiales registrados.
Número de libros y revistas.
Promedio de páginas para los libros.
Ayuda: se puede usar la siguiente función: Ej: isinstance(m, Libro)--> devuelve true si el objeto m es de tipo Libro

6.Implementa un menú que permita al usuario realizar las siguientes acciones:
Agregar Material: Permite al usuario agregar un nuevo Libro o Revista.
Listar Materiales: Muestra una lista de todos los materiales registrados con sus detalles. Elije la forma de presentación más adecuada para que el usuario lo vea claro.
Buscar Material por ID: Permite al usuario buscar un material específico por su id.
Eliminar Material: Elimina un material específico usando su id.
Generar Estadísticas
Salir: Termina la ejecución del programa.'''

# creacion de la clase madre Material
class Material:
    def __init__(self, id, titulo, autor, anyo):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.anyo = anyo

# creo la lista de los generos en MINUSCULAS 
generoList = ["ficcion", "no ficcion", "terror", "ciencia"]

class Libro(Material):
    def __init__(self, id, titulo, autor, anyo, genero, numPag):
        super().__init__(id, titulo, autor, anyo)
        if genero in generoList:
            self.genero = genero
        else:
            print("Genero invalido")
            self.genero = "ficcion"

        if numPag >= 0:
            self.numPag = numPag
        else:
            print("NumPag invalido")
            self.numPag = 0
    def __str__(self):
        return f"Libro: titulo: {self.titulo}, autor: {self.autor}, anyo: {self.anyo}, genero: {self.genero}, numPag: {self.numPag}"

# creo la lista de los meses en MINUSCULAS 
mesesList = ["enero", "febrero", "marzo", "abrir","mayo","junio","julio","agosto","septiembre","obtubre","noviembre","diciembre"]

class Revista(Material):
    def __init__(self, id, titulo, autor, anyo, numEdi, mes):
        super().__init__(id, titulo, autor, anyo)
        self.numEdi = numEdi
        if mes in mesesList:
            self.mes = mes
        else:
            print("Mes no valido se asiganara ENERO")
    
    def __str__(self):
        return f"Revista: titulo: {self.titulo}, autor: {self.autor}, anyo: {self.anyo}, numEdi: {self.numEdi}, mes: {self.mes}"

# creo dos ejemplo y lo anyado a diccionario
libro = Libro("1","ejemplo","autor",1999,"ficcion",25)
libro2 = Libro("2","ejemplo2","autor",1999,"ficcion",60)

diccionario = {"1" : libro,
               "2" : libro2}

# Al crear el ejemplo tengo que anyadir su id a la lista
idList = ["1", "2"]

# metodo que crea todas las estadisticas
def estadisticas():
    print("total materiales ingresados: ", len(idList))

    contarLibros = 0
    contarRevistas = 0
    promedio = 0
    for clave, valor in sorted(diccionario.items()):
        if isinstance(valor, Libro):
            contarLibros += 1
            promedio = valor.numPag
        if isinstance(valor, Revista):
            contarRevistas += 1
    print("Hay ", contarLibros, " libros y ", contarRevistas, " revistas")

    promedio = promedio/contarLibros
    print("El promedio de paginas es: ", promedio)

# metodo para agregar material en el cual controlo si es un int y si estan en las listas, esto lo controlo 2 veces
def agregrarMaterial():
    id = input("Dime el id: ")
    id = id.lower()

    if id in idList:
        print("El id ya esta en uso")
    else:
        titulo = input("Dime el titulo: ")
        autor = input("Dime el autor: ")
        filtro = True
        while filtro:
            try:
                anyio = int(input("Dime el anyo de publicacion: "))
                if anyio > 0:
                    filtro = False
                else:
                    print("El numero debe ser mayor de 0")
            except ValueError:
                print("inserte un numero porfavor")

        filtro1 = True
        while filtro1:
            obcion = input("Es un Libro o Revista?: ")
            if obcion.lower() == "libro":
                filtro2 = True
                genero = input("Dime el genero del libro: ")
                while filtro2:
                    if genero in generoList:
                        filtro2 = False
                    else:
                        print("introduce un genero valido: ")
                filtro3 = True
                while filtro3:
                    try:
                        numPag = int(input("Dime el numero de paginas del libro: "))
                        if numPag > 0:
                            filtro3 = False
                        else:
                            print("El numero debe ser mayor de 0")
                    except ValueError:
                        print("inserte un numero porfavor")
                libro = Libro(id,titulo,autor,anyio,genero.lower(),numPag)
                diccionario[id] = libro
                filtro1 = False
            elif obcion.lower() == "revista":
                filtro4 = True
                while filtro4:
                    try:
                        numEdi = int(input("Dime el num de edicion: "))
                        if numEdi > 0:
                            filtro4 = False
                        else:
                            print("El numero debe ser mayor de 0")
                    except ValueError:
                        print("inserte un numero porfavor")
                filtro5 = True
                while filtro5:
                    mes = input("Dime el mes de publicacion: ")
                    if mes in mesesList:
                        filtro5 = False
                    else:
                        print("introduce un mes valido")
                revista = Revista(id,titulo,autor,anyio,numEdi,mes.lower())
                diccionario[id] = revista
                filtro1 = False
            else:
                print("Porfavor escriba libro o revista")

        idList.append(id)

def listaMateriales():

    for clave, valor in sorted(diccionario.items()):
        print(clave, valor)

def buscar():
    id = input("Que id quiere buscar?: ")
    id.upper()
    if id in diccionario:
        eliminar = input("Material encontrado:")
        print(id, diccionario.get(id))

def eliminarMaterial():
    id = input("Que id quiere eliminar?: ")
    id.upper()
    if id in diccionario:
        eliminar = input("Material encontrado, desea eliminarlo? Puse Y:")
        if eliminar.lower() == "y":
            diccionario.pop(id, "por si acaso")
            print("Eliminado con exito")

        else:
            print("volviendo...")

def menu():
    while True:
        print("""MENÚ DE OPCIONES
a) Agregar Material
b) Listar Materiales
c) Buscar Material por ID
d) Eliminar Material
e) Generar Estadisticas
f) salir
""")

        opcion = input("Selecciona una opcion: ").lower()
        print("\n")

        if opcion == 'a':
            agregrarMaterial()
        elif opcion == 'b':
            listaMateriales()
        elif opcion == 'c':
            buscar()
        elif opcion == 'd':
            eliminarMaterial()
        elif opcion == 'e':
            estadisticas()
        elif opcion == 'f':
            print("\nSaliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción correcta.")
        print("\n")

if __name__ == "__main__":
    menu()
