# 1.List
# A list is an ordered, changeable (mutable) collection of items
# It can hold different data tpes -- strings, numbers, booleans, even other lists.

fruits = ["apple", "banana", "cherry"]
print(fruits)

# append (adds one item at end)

fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)

# insert(i, x) adds item at specific index

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "mango")

# remove(x) Removes first matching value 

fruits = ["apple", "banana", "cherry", "mango"]
fruits.remove("banana")
print(fruits)

# sort (Sort the list) sorts in ascending order
numbers = [5,1,5,3,2,0]
numbers.sort()
print(numbers)

# reverse() Reverses order /in descending order
numbers = [1,3,6,2,5,1]
numbers.reverse()
print(numbers)

# pop() removes last element

fruits = ["apple", "banana", "cherry", "mango"]
removed_item = fruits.pop()   # removes last element
print("Updated list:", fruits)
print("Removed item:", removed_item)

# pop() remove specifi item or element
fruits = ["apple", "banana", "cherry", "mango"]
removed_item = fruits.pop(2) # removed element (1) or (2)
print("updated list:", fruits)
print("Removed item:", removed_item)
