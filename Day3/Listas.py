my_list = ['a','b','c']
print(my_list)
print("-----------------------")
my_list = ['a',"red",45]
print(my_list)
print(len(my_list))
test = my_list[1]
print(test)
print("-----------------------")
my_list2 = [1,2,3]
my_list3 = [4,5,6]
print(my_list2 + my_list3)
print("-----------------------")
my_list2[0] = "one"
print(my_list2)
print("-----------------------")
my_list3.append("seven")
print(my_list3)
print("-----------------------")
my_list3.pop() #elimina el ultimo por defecto
print(my_list3)
eliminated = my_list.pop(1)
print(eliminated)
print("-----------------------")
new_list = ["u","e","i","o","a"]
new_list.sort() #ordena
print(new_list)
new_list.reverse() #orden inverso
print(new_list)