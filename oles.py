name = 'Ajay Kumar'
vowels = 'aeiouAEIOU'
a=''
for i  in name:
    if i not in vowels:
        a += i
print(a)        