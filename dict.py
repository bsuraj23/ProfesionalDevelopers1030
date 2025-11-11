diction={}
print(dict)
student={
    1:["Han",34.5],
    2:"Nvee","Chen":{"age":20,"height":5.8},     #nested dictionary
    0: "Ceaser"
}
print(student)
print(student[0])
print(student["Chen"]["age"])
print(student[1][0])
print(student.get(2))
print(student.keys()) #gives list of keys
print(student.values()) #gives list of values
print(student.items()) #gives list of key and value pairs


