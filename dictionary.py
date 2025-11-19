d = {"name": "Alice", "age": 20}
print(d.keys())  


d = {"name": "Alice", "age": 20}
print(d.values())  



d = {"name": "Alice", "age": 20}
print(d.items())  



d = {"name": "Alice"}
print(d.get("name"))       
print(d.get("age", "NA"))   



d = {"name": "Alice", "age": 20}
d.update({"age": 21, "city": "Delhi"})
print(d)



d = {"name": "Alice", "age": 20}
d.pop("age")
print(d)   



d = {"a": 1, "b": 2}
d.popitem()
print(d)   



d = {"a": 1, "b": 2}
d.clear()
print(d)  




d1 = {"x": 10, "y": 20}
d2 = d1.copy()
print(d2)



d = {"name": "Alice"}
d.setdefault("age", 20)
print(d) 
