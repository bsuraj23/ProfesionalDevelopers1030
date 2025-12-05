from datetime import date

dob = date(2003, 5, 10)
today = date.today()

print((today - dob).days)
