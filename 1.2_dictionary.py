# 1. Dictionary (dict)
# Defination: a dictionary in python is a collection of key-value pairs.
# Each key must be unique, and it maps to a specific value.

student = {"Name": "Rishi", "age": 22, "course": "python"}
print(student)

# Note : access using key like

student = {"Name": "Sravya", "age": 21, "course": "Python"}
print(student["Name"]) # Getting Name 
print(student["age"]) # Getting age 
print(student["course"]) # Getting Course 

# dict.key() Return all keys

student = {"name": "Bhanu_Prakash", "age": 24, "gender": "male", "Hight": 5.6}
print(student.keys()) # Return all keys

# dict.values() -- Returns all values
student = {"name": "Ayub", "score": "80%", "grade": "B-Grade"}
print(student.values()) # gives you all the values from the dictionary

# dic.items() -- Returns all key-value pairs
student = {"name": "Rishi", "age": 22, "location": "kurnool"}
print(student.items()) # return each key and value

# dict.get(key) -- Safely get a value
student = {"name": "Rishi", "age": 22, "location": "kurnool"}
print(student.get("name")) # Existing key
print(student.get("score")) # non-existing key

# dict.update({...})--Update existing data or add new one
student = {"name": "Rishi", "age": 22, "location": "kurnool"}
student.update({"age": 23}) # updated values
print(student)

# Explanation: 
# If the key exists → value gets updated
# If key doesn’t exist → new key-value pair added

# dict.pop(key) --Removes a key-value pair

student = {'name': 'Rishi', 'age': 23, 'course': 'Python', 'city': 'Hyderabad'}
removed_value = student.pop("course") # remove key and value (pair)
print("Removed:", removed_value)
print("After removing:", student) 

# dict.clear() -- Removes all items

student = {'name': 'Rishi', 'age': 23, 'course': 'Python', 'city': 'Hyderabad'}
student.clear()
print(student)

