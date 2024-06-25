text = "This is my text"

test = text.upper() #mayusculas
print(test)
print("-----------------------")
test2 = text.lower() #minusculas
print(test2)
print("-----------------------")
test3 = text.title()
print(test3) #letras iniciales en mayuscula
print("-----------------------")
test4 = text.split() #separa en una lista tomando el espacio como separador
print(test4)          #en el parametro se puede escoger la letra que se tome como separador
print("-----------------------")
a = "Lern"
b = "Python"
c = "is"
d = "awesome"
e = " ".join([a,b,c,d])
print(e)
print("-----------------------")
test5 = text.find("z") #como no existe en vez de darnos un error nos da un -1
print(test5)
print("-----------------------")
test6 = text.replace("t","o") #reemplaza la 't' por 'o'
print(test6)
