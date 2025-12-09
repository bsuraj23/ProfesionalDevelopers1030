x = "hello"
print(type(x))

k = "25"
k = 25
k = 25.5
print(type(k))


dic = {"name":"ayub", "age":25}
print(dic["name"])
print(dic["age"])

d = {"name":"asif", "age":27, "village":"kuppam"}
print(d["village"])
print(d["age"])
print(d["name"])

a = ['apple', 'banana', 'mango']
a.append("pubg king")
a.insert(1, "boss")
a.remove("mango")
print(a)

s = {254, "ayub", 123.45}
s.add(123)
print(s)
s.remove(123.45)
print(s)

a = {0, 9, 8, 7, "akram", 6, 5, 4, 3, 2, 1}
print(a)



name = "ayub ali"
age = 25
hobbies = ["playing games", "listining music", "using mobile phone"]
marks = {"maths":75, "telugu":85, "english":45}
print(name, age, hobbies, marks)
print(age)
print(hobbies)
print(marks)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
obj = Car("bmw", "m4")
print(obj.brand)
print(obj.model)            

class Oneplus:
    def __init__(self, series, year):
        self.series = series
        self.year = year
obj = Oneplus("8pro", "2018")
print(obj.series)
print(obj.year) 
                       