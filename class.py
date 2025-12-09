class Student:
    school_name = "ABC School"   # Class variable

    @classmethod
    def get_school(cls):
        return f"School Name: {cls.school_name}"

# Calling class method using class name
print(Student.get_school())