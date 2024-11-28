#6. Escribe un programa que recoja las notas de las tres evaluaciones de un alumno. A continuación debe calcular y mostrar la nota final, teniendo en cuenta que la primera evaluación cuenta un 20% de la nota final, la segunda evaluación un 35% y la tercera evaluación un 45%.

a = int(input("1 trimestre"))
a_total = a * 0.2
b = int(input("2 trimestre"))
b_total = b * 0.35
c = int(input("3 trimestre"))
c_total = c * 0.45

total = a_total + b_total + c_total
print("La nota total es " + str(total))