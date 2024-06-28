def addition(**kwargs):
    total = 0
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        total += value
    return total


print(addition(x=2, y=3, z=4))

print("-----------------------")

def test(num1, num2, *args, **kwargs):
    print(f'{num1} + {num2} = {num1 + num2}')

    for arg in args:
        print(arg)


    for key, value in kwargs.items():
        print(f'{key}: {value}')

test(45,52,34,233,24,x="one",y="two",z="three")

print("-----------------------")

def test(num1, num2, *args, **kwargs):
    print(f'{num1} + {num2} = {num1 + num2}')

    for arg in args:
        print(arg)


    for key, value in kwargs.items():
        print(f'{key}: {value}')

args = [1,2,3,4,5]
kwargs = {'x':'one','y':'two','z':'three'}
test(45,52,*args,**kwargs)

