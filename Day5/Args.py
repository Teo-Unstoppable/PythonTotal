def addition(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(addition(1,2,3,4))

def addition(*args):
    return sum(args)
