"""
La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
letras a su elección y a partir de ese momento nuestro código va a procesar esa información
para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:
1. Primero: ¿cuántas veces aparece cada una de las letras que eligió? Para lograr esto, te
recomiendo almacenar esas letras en una lista y luego usar algún método propio de string
que nos permita contar cuantas veces aparece un sub string dentro del string. Algo que
debes tener en cuenta es que al buscar las letras pueden haber mayúsculas y minúsculas
y esto va a afectar el resultado. Lo que deberías hacer para asegurarte de que se
encuentren absolutamente todas las letras es pasar, tanto el texto original como las
letras a buscar, a minúsculas.
2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto. Y
para lograr esta parte, recuerda que hay un método de string que permite transformarlo
en una lista y que luego hay una función que permite averiguar el largo de una lista.
3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última. Aquí
claramente echaremos mano de la indexación.
4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de
las palabras. ¿Acaso hay algún método que permita invertir el orden de una lista, y otro
que permita unir esos elementos con espacios intermedios? Piénsalo.
5. Y por último: el sistema nos va a decir si la palabra “Python” se encuentra dentro del
texto. Esta parte puede ser algo complicada de imaginársela, pero te voy a dar una pista:
puedes usar booleanos para hacer tu averiguación y un diccionario para encontrar la
manera de expresarle al usuario tu respuesta.
"""
text = input("Put your text: ").lower()
letter_1 = input("Put first letter: ").lower()
letter_2 = input("Put second letter: ").lower()
letter_3 = input("Put third letter: ").lower()

first_letter = text[0]
last_letter = text[-1]

list_text = text.split()
count_words = len(list_text)
list_text.reverse()
reverse_text = " ".join(list_text)

print("\n")
print("NUMBER OF LETTERS")
print(f"The letter {letter_1} is '{text.count(letter_1)}' times in the text.")
print(f"The letter {letter_2} is '{text.count(letter_2)}' times in the text.")
print(f"The letter {letter_3} is '{text.count(letter_3)}' times in the text.")
print("\n")
print("START AND END LETTERS")
print(f"The first letter is '{first_letter}'")
print(f"The last letter is '{last_letter}'")
print("\n")
print("INVERTED TEXT")
print(f"The reverse text is '{reverse_text}'")
print("\n")
print("NUMBER OF WORDS")
print(f"The total number of words is {count_words}.")
if "python".lower() in text:
    print("Python is in the text")
else:
    print("Python isn't in the text")