import re
s = "Ma@na#12$"
print(re.sub('[^a-zA-Z0-9]', '', s))
