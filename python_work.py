#slicing without using symbels

python="python language"
s=slice(1,7)
print(python[s])

#check if set and list accept dulicate and null values

list=[1,5,5, None,None]
set={1,5,5,None,None}
print("list:",list)
print("set:",set)
#list-accepts duplicates and multipule none values
#set-remove duplicates auctmotically,but accepts one none value


#diff betn discard and remove
v={22,330,55,66}
v.discard(55)
print("discard:",v)

#remove
v={22,33,44,55}
v.remove(44)
print("remove:",v)

#union,intersection,and difference
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)         
print("Intersection:", A & B)   
print("Difference:", A - B)    
print("Symmetric Difference:", A ^ B)  

#frozenset

normal_set = {1, 2, 3}
frozen = frozenset(normal_set)

print("Frozen Set:", frozen)
#a frozenset as a dictionary key or inside another set it is a immutable.


#Tuple count without using
t = (1, 2, 3, 2, 4, 2, 5)
num = 2
count = 0

for i in t:
    if i == num:
        count += 1

print(f"{num} appears {count} times")



#unpacking in tuple

t = (10, 20, 30)
a, b, c = t

print(a)  
print(b)  
print(c)  
