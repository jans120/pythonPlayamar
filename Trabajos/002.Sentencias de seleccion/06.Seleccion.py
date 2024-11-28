# 6. Escribe un programa que muestre la nota final de un alumno a partir de su calificación numérica (valor decimal), teniendo en cuenta que:
    # a. Nota menor de 5 es suspenso.
    # b. Nota entre 5 y 6 (sin llegar) es suficiente.
    # c. Nota entre 6 y 7 (sin llegar) es bien.
    # d. Nota entre 7 y 9 (sin llegar) es notable.
    # e. Nota entre 9 y 10 (sin llegar) es sobresaliente.
    # f. Nota igual a 10 es matrícula de honor.
    # g. Cualquier otro valor numérico fuera de este rango es un error.

calificacion = float(input("Ingresa la calificación numérica: "))

if calificacion < 0 or calificacion > 10:
    print("Error: Calificación fuera de rango.")
elif calificacion == 10:
    print("Matrícula de honor.")
elif 9 <= calificacion < 10:
    print("Sobresaliente.")
elif 7 <= calificacion < 9:
    print("Notable.")
elif 6 <= calificacion < 7:
    print("Bien.")
elif 5 <= calificacion < 6:
    print("Suficiente.")
else:
    print("Suspenso.")
