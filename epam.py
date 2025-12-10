a = [("home", 40), ("orange", 50), ("home", 50)]
b = [("orange", 20), ("egg", 30)]
dictt = {}
for key,value in a:
    dictt[key] = dictt.get(key, 0) + value
for key,value in b:
    dictt[key] = dictt.get(key, 0) + value
for key,value in dictt.items():        
    print(key , value)

