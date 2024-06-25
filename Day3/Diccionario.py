dictionary = {"c1":"valor","c2":"valor_2"}
print(dictionary)
print(type(dictionary))
print(dictionary["c1"])
print("-----------------------")
client = {"name":"Jonh","age":25}
print(client)
print(client["age"])
print("-----------------------")
dictionary = {"c1":"valor","c2":"valor_2","c3":{"name": "Jonh", "age": 25}}
print(dictionary["c3"])
print(dictionary["c3"]["name"])
print(dictionary["c3"]["name"].upper())
print("-----------------------")
dictionary["c4"] = 67
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())