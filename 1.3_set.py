# 1.>> Set >>
# Defination: a set is an unordered, unidexed, mutable collection of unique elements.
# Duplicates are automatically removed

numbers = {1,2,3,3,4,5,6,6,6,1}
print(numbers) # removed duplicate values 

# add(x) → Adds a new element to the set
numbers = {1,2,3}
numbers.add(4) # → Adds a new element to the set
print(numbers)

# remove(x) → Removes a specific element
numbers = {1,2,3,4}
numbers.remove(3) # → Removes 3 number
print(numbers)

# discard(x) → Removes element if it exists (no error)
numbers = {1,2,3}
numbers.discard(2)  # if it already exists it'll remove from set
numbers.discard(10) # no error even if not found
print(numbers)

# pop() → Removes a random element 
numbers = {10, 20, 30, 40, 50}
removed_item = numbers.pop()
print("Removed:", removed_item)
print("Remaining:", numbers)

# union() → Combines two sets (no duplicates)
a = {1,2,3}
b = {3,4,5}
combined = a.union(b)
print(combined)

# intersection() → Elements common in both sets

a = {12,3,4,5}
b = {3,4,5,9}
common = a.intersection(b) # display common both sets
print(common)

# difference() → Elements in one set but not in the other

a = {1,2,3,4,5}
b = {3,6,7,0}
only_in_a = a.difference(b)
print(only_in_a)