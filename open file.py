f = open("C:/Users/YourName/Desktop/test.txt", "w")
f.write("Hello File")
f.close()

f = open("C:/Users/YourName/Desktop/test.txt", "r")
print(f.read())
f.close()
