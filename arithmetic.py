subjects="telugu+hindi+maths+science+english+social"
max_marks=600
telugu=int(input("enter the telugu marks:"))
print("telugu marks:", telugu)
english=int(input("enter the english marks:"))
print("engish marks:", english)
hindi=int(input("enter the hindi marks:"))
print("hindi marks:", hindi)
social=int(input("enter the social marks:"))
print("social marks:", social)
maths=int(input("enter the maths marks:"))
print("maths marks:", maths)
science=int(input("enter the science marks:"))
print("science marks:", science)
print("\n------result------")
total_marks = telugu+english+hindi+social+maths+science
print("total marks:")
average=total_marks/6
print("average:",(total_marks/6)) 
percentage=(total_marks/max_marks)*100
print("percentage:","%",(total_marks/max_marks)*100)
print("\n total marks of all subjects =", total_marks)
