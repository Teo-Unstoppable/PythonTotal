names = ["Jonh","Mathew","Jesus"]
ages = [25,21,33]
combined = list(zip(names,ages))
print(combined)

for name,age in combined:
    print(f"{name} is {age} years old")