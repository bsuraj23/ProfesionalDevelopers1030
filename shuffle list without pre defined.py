my_list = [1, 2, 3, 4, 5]
new_list = []

while my_list:
    element = my_list.pop(0)
    new_list.insert(len(new_list) // 2, element)

print(new_list)
