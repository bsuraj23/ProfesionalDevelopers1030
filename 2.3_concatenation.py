# String Concatenation (Joining)
# Concatenation means joining two or more string together to form one complete string.

First = "Rishi"
Last = "Kumar"
Full_Name = First + "" + Last # add two Values 
print(Full_Name)

text = "hi! "
print(text*3)  # Repeat using *

# 1. Using + Operator
# you can join string directly using the + operator

first_name = "Rishi " # if you want space each word you can space Rishi after one space
last_name = "kumar"
full_name = first_name + "" + last_name
print(full_name)

# joining multiple strings
a = "python"
b = "is"
c = "fun"
sentance = a + " " + b + " " + c + "!" # "" adds a space between the two strings
print(sentance)

# Using join() Method
# you can use the join() method to combine a list (or tuple) of string

words = ["I", "Love", "Python"]
sentance = " ".join(words)
print(sentance)

letters = ["a", "b", "c", "d"]
joined = "-".join(letters) # if you inside - it will print 
print(joined)

# Using f-string (Fast & modern way)
# you can embed variables inside string using f-string (python 3.6+)

name = "Rishi"
age = 22
intro = f"my name is {name} and i am {age} years old."
print(intro)

language = "python"
version = 3.11
print(f"i am learning {language} version {version}.")

# Using formate() Method
# you can also use formate() to join string dynamically
name = "Rishi"
course = "Python"
text = "Hello {}, welcome to the {} course.".format(name, course)
print(text)