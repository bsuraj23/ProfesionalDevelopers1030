# 1. Instance method
# 2. Class Method
# 3. Static Method

#----------------------------------------------------------
# Instance method 
# > method that works with object data


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def show(self):   # instance method
        print(self.name, self.marks)

# # create an object and call the method
# # > you must create object ouside the class

# creating object
s1 = Student("Rishi", 90)

# calling instance method
s1.show()
#--------------------------------------------------------

# class method
# > method that works with class-level data, not object level
# > Identified by > has @classmethod decorator
# > first argument is cls (class refrence)

class Student:
    school_name = "Model school"

    @classmethod
    def change_school(cls, new_name): # This method changes the class variable for all objects.
        cls.school_name = new_name 
    
# creating objects

s1 = Student()
s2 = Student()

print(s1.school_name) # Model school
print(s2.school_name) # Model shcool

# changining school name using class method
Student.change_school("xyz International school")

print(s1.school_name)
print(s2.school_name)

# school_name belongs to class -> not object
# change_school() updates cls.school_name -> affects all objects
# so all students share the same schoolname

#-----------------------------------------------------------------

# static method
# method that does not use:
# self, class
# it is like a normal function inside class
# Identified -> @staticmethod decorator
# No self no class argument

class Student:

    @staticmethod
    def is_pass(mark):
        return mark >= 35
print(Student.is_pass(40))  # True

#----------------------------------------------------------

# Small Real life Scanario  (Bank Account)
class Bank:
    bank_name= "SBI"       # class variable

    def __init__(self, name, balance):
        self.name = name     # instance variable
        self.balance = balance

    # Instance Method
    def deposit(self, amount):
        self.balance += amount

    # class Method
    @classmethod
    def change_bank(cls, new_name):
        cls.bank_name = new_name
    
    # static Method
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0
    
# calling
 
b = Bank("Rishi", 5000000000)

# Instance Method
b.deposit(20000000)

# class Method
Bank.change_bank("HDFC")

# static Method
print(Bank.is_valid_amount(20000000))

    




