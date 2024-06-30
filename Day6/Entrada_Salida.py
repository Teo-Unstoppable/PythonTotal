mi_archivo = open("Prueba.txt")

"""print(mi_archivo.read())"""

print("----------------")

"""una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea)
una_linea = mi_archivo.readline()
print(una_linea.upper())"""

print("----------------")

"""for linea in mi_archivo:
    print(f"Aqui dice: {linea}")"""

print("-----------------")

todas = mi_archivo.readlines()
print(todas)









mi_archivo.close()
