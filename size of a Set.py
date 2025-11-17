#size of a Set 

# Method 1
import sys
# sample Sets
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), (2, "Tiger"), (3, "Fox")}
# print the sizes of sample Sets
print("Size of Set1:", sys.getsizeof(Set1), "bytes")
print("Size of Set2:", sys.getsizeof(Set2), "bytes")
print("Size of Set3:", sys.getsizeof(Set3), "bytes")

# Method 2
print("method 2")
print("Size of Set1:", Set1.__sizeof__(), "bytes")
print("Size of Set2:", Set2.__sizeof__(), "bytes")
print("Size of Set3:", Set3.__sizeof__(), "bytes")