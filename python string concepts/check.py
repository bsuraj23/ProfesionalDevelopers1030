s = "Darksiders2"
print("dar" in s)
print("rs2" in s)
print("2" in s)
print("     ")


str="God of war"
print(str.startswith("God"))
print(str.endswith("war"))
print("of " in str)
print("")

#comparision
A="CarlJohnson"
B="Trevor"
print(A==B)
print(A<B)
print(A>B)
print("")

#Counting
s="Froza Horizon"
print(s.count("H"))
print("")

#finding
S = "Red Dead Redemption"
print(S.find("Dead"))
print(S.find("Redemption"))
print("")

#format string

name = "yesh"
age = 22
height = 5.7
print("my name is {} and my age is {} and height is {}".format(name, age, height))
print("my name is {N} and my age is {A} and height is {H}".format(N=name, A=age, H=height))
print(f"my name is {name}, my age is {age}, height is {height}")
print("")

Number = 1224.567889
print("format number is {:.2f}".format(Number))
print("format number is {}".format(Number))
print("format number is {:.8f}".format(Number))