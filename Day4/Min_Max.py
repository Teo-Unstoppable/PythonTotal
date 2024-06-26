list_numbers = [135,23,343,42,5,68,765,8,95,105]
print(f"The numbers are {list_numbers}")
print(f"The maximum is {max(list_numbers)}")
print(f"The minimum is {min(list_numbers)}")
print("------------------------------------------------")
name = "Mathew"
print(f"{name} has a length of {len(name)}")
print(f"The first letter in alphabetical order is '{min(name.lower())}'")
print(f"The last letter in alphabetical order is '{max(name.lower())}'")
print("-------------------------------------------------")
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
print(edad_minima)
print(ultimo_nombre)
