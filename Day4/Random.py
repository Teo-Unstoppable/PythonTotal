from random import randint
from random import uniform
from random import choice
from random import shuffle
from random import random

r_andom = randint(1,100)
print(r_andom)
print("-----------------")
r_andom = round(uniform(1,100),2)
print(r_andom)
print("-----------------")
colors = ["red","blue","green","yellow","orange","brown","pink","purple"]
random_color = choice(colors)
print(random_color)
print("-----------------")
r_shuffle = list(range(1,21))
shuffle(r_shuffle)
print(r_shuffle)
print("-----------------")
r_andom = random()
print(r_andom)
