"""
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']
"""
def letras_unicas(palabra):

    set_letras = set()

    for letter in palabra:
        set_letras.add(letter)

    lista_letras = []

    for letra in set_letras:
        lista_letras.append(letra)
    lista_letras.sort()

    return lista_letras

print(letras_unicas("entretenido"))
