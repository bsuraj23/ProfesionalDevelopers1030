text = input("Enter text: ")
# Remove symbols and spaces, and make lowercase
cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
# Check if palindrome
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
