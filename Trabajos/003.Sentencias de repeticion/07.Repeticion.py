# 7. Escribe un programa que recoja una cadena de texto por teclado y una letra a buscar. Luego debe buscar dicha letra por la cadena y al finalizar debe indicar el número de veces que se repite la letra en el texto.

texto = input("Ingresa una cadena de texto: ")
letra = input("Ingresa la letra a buscar: ")

contador = texto.count(letra)
print(f"La letra '{letra}' se repite {contador} veces en el texto.")
