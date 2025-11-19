# >> What is string indexing?
# String indexing means accessing each character in a string using its position number
# Each character in a string is stored at a specific index position, starting from 0 on the left.
text = "PYTHON"
# small sample  
# Character	 P	 Y	 T	 H	 O	 N
# Index (+)	 0	 1	 2	 3	 4	 5
# Index (–)	-6	-5	-4	-3	-2	-1

text = "PYTHON"
print(text[0]) # return (P)

text = "PYTHON"
print(text[3]) #return (H)

text = "PYTHON"
print(text[-1]) # return (N)

# Real-Life example -- checking file type from file name
# when you upload a file, you can check its extention using indexing

filename = "document.pdf"
print("Last character:", filename[-1]) # f
print("file extention:", filename[-3:]) # last 3 characters (pdf)
print("filename:", filename[:3]) # first 3 characters (doc)

# explaination: 
# filename[-1] → last character
# filename[-3:] → last 3 characters, file extention
# filename[:3] → first 3 character (doc)

# Getting country code from phone number
phone = "+91-630502015024"
print("country code:", phone[0:3]) # Display first 3 digits
print("county code:", phone[:3]) # both are same

# Masking Sensitive Information
card_number = "1234-5678-9012-3456"
masked = "1234-xxxx-xxxx-" + card_number[-4:] 
print("master card number:", masked) # masked digits like ATM 

# start    --> index where slice begins (included)
# end      --> index where slice ends (excluded)
# step     --> how many charcters to skip

text = "PYTHON"
print(text[1:5]) 
print(text[0:6:2])
print(text[::-1]) #  reverse string
print(text[::2])