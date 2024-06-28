"""
Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.
"""

def devolver_distintos(num1,num2,num3):

    suma = num1 + num2 + num3
    lista = []
    lista.append(num1)
    lista.append(num2)
    lista.append(num3)
    lista.sort()

    if suma >= 15:
        return lista[-1]
    elif suma <= 10:
        return lista[0]
    elif 15 > suma > 10:
        return lista[1]

print(devolver_distintos(4,9,2))

