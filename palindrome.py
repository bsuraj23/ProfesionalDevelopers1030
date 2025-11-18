# Check if a given string is a palindrome

text = input("Enter a word or number: ")

reverse = ""
for i in text:
    reverse = i + reverse  

if text == reverse:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")