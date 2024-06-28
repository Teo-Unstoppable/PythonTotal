from random import shuffle
# Lista inicial
palitos = ["-","--","---","----"]

# Mezclar palitos
def mezclar(lista_palitos):
    shuffle(lista_palitos)
    return lista_palitos

# Pedir intento
def probar_suerte():
    intento = ""
    while intento not in ["1","2","3","4"]:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

# Comprobar intento
def chequear_intentos(lista_palitos,intento):
    if lista_palitos[intento - 1] == "-":
        print("A lavar los platos")
    else:
        print("Te has salvado")
    print(f"Te ha tocado '{lista_palitos[intento - 1]}'")

palitos_mezclados = mezclar(palitos)
intento = probar_suerte()
chequear_intentos(palitos_mezclados,intento)

