from random import choice

lista_palabras = ["murcielago", "avion", "computador", "paloma"]


#
def escoger_palabra(lista):
    palabra_secreta = choice(lista)
    print(palabra_secreta)
    return palabra_secreta


def esconder_palabra(palabra):
    lista = []
    for letter in palabra:
        lista.append("-")
    return lista


def pedir_letra(letra):
    while letra not in "abcdefghijklnmopqrstuvwxyz":
        letra = (input("Escribe una letra: "))
    return letra


def chequear_letra(letra, palabra_secreta, lista):
    lista_letras_malas = []

    for indice,caracter in enumerate(palabra_secreta):
        if letra in palabra_secreta:
            if caracter == letra:
                lista[indice] = letra
            print(x)
        else:
            lista_letras_malas.append(letra)

    print(f"malas {lista_letras_malas}")
    print(lista)


letra = input("Escribe una letra: ")
palabra = escoger_palabra(lista_palabras)
print(esconder_palabra(palabra))
guiones = esconder_palabra(palabra)
x = (pedir_letra(letra))
chequear_letra(x, palabra, guiones)
