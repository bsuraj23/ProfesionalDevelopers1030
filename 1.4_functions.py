# Defining and calling a function
def say_hello(name):
    print("Hello,", name)

say_hello("Rishi")

# Return statement
def add(a, b):
    return a + b
result = add(10, 20)
print("sum:", result)

# Default Parameter
def greet(name="User"):
    print("Hello,", name)

greet()
greet("Rishi")

# Keyword Argumenets

def info(name, age):
    print(name, "is", age, "years old")

info(age=22, name="Rishi")

# Arbitary Arguments (args)
# Used when you don't know how many arguments will be passed

def total(*numbers):
    print("Total:", sum(numbers))

total(10,20,30,40)

# *args collects all extra positional arguments into a tuple.

#Arbitrary keyword arguments
# Used for variable-length keyword arguments.

def student_info(**data):
    print("student data:", data)
student_info(name="Rishi", age=22, course="python")

