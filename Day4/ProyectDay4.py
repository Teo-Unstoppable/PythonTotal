"""
La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado.
"""
from random import randint

secret_number = randint(1, 101)
attempts = 1
lives = 8

name = input("Enter the username: ")
print(f"Ok,{name} I have thought of a number between 1 and 100, and you have only eight tries to guess what you think the number is.")

num = int(input("Put a number please: "))
while lives > 1:
    if num > 101:
        num = int(input("Invalid number, enter another number: "))
        lives -= 1
        attempts += 1
    elif num == secret_number:
        print(f"Won,{name} the secret number was {secret_number}\nNumber of attemps: {attempts}.")
        break
    elif num > secret_number:
        lives -= 1
        attempts += 1
        num = int(input("The secret number is smaller, enter another number:  "))
    elif num < secret_number:
        lives -= 1
        attempts += 1
        num = int(input("The secret number is greater, enter another number:  "))
if attempts == 8:
    print(f"You lost the secret number it was: {secret_number}\nNumber of attemps: {attempts}.")










