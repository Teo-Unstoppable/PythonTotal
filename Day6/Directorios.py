import os
"""ruta = os.getcwd() #trae la ruta actual
ruta_2 = os.chdir("C:\\Users\\mateo\\OneDrive\\Documentos\\Programacion\\Python") #midifica el directorio alctual
ruta_3 = os.mkdir("C:\\Users\\mateo\\OneDrive\\Documentos\\Programacion\\Python\\Prueba") #crea una carpeta
archivo = open("otro_archivo.txt","a")"""

ruta = "C:\\Users\\mateo\\OneDrive\\Documentos\\Programacion\\Python"

elemento = os.path.dirname(ruta)
print(elemento)






