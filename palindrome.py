x=input()
if (x==x[::-1]):
    print("palindrome")
else:
    print("not a palindrome")

#without [::-1]
y=int(input())
og=y #store y in og
rev=0

while (y!=0): 
    r=y%10              #1221%10= 1
    rev=rev*10+r        #1
    y//=10               #1221//10=122  // integer division

if og==rev:
    print("palindrome")
else:
    print("not a palindrome")