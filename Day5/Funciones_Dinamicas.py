def three_digit_number(number):
    return number in range(100,1000)


result = three_digit_number(564)
print(result)
from random import shuffle
def three_digit_number(list):
    num_list = []
    for number in list:
        if number in range(100,1000):
            num_list.append(number)
    shuffle(num_list)
    return num_list


num_list = list(range(1,200,7))
result = three_digit_number(num_list)
print(result)