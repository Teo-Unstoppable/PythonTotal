names = ['John', 'Jane', 'Doe', 'Jack']
for name in names:
    print(f"Hello {name}!")

print("-----------------")
letters = ['a', 'b', 'c', 'd', 'e']
for letter in letters:
    number_of_letter = letters.index(letter) + 1
    print(f"{number_of_letter}. {letter.upper()}")
print("-----------------")
for name in names:
    if name.startswith("D"):
        print(f"Hello {name}")
print("-----------------")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
addition = 0
for number in numbers:
    addition += number
print(addition)
print("-----------------")
for a,b in [[1,2],[3,4],[5,6],[7,8]]:
    print(b)