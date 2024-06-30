archivo = open("Prueba.txt","a")# si ponemos "w" en vez de a se borra todo el contenido y escribimos de cero
archivo.write("\nSoy el nuevo texto")
archivo.writelines(["\nhola", "mundo","aqui","estoy"])





archivo.close()