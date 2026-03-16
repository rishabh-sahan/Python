# class Student:
#     subject = "Python"
#     college = "Apna College"
#     year = "3rd Year"

# stu1 = Student()
# stu2 = Student()
# print(stu1.subject, stu1.college, stu1.year)
# print(stu2.subject, stu2.college, stu2.year)
# print(type(stu1))

# class Student:
#     def __init__(self): # Default Constructor
#         print("Constructor called")

# class Student:
#     def __init__(self, name, cgpa): # Parameterized Constructor
#         self.name = name
#         self.cgpa = cgpa

#     def get_cgpa(self):
#         return self.cgpa
        
# stu1 = Student("Alice", 9.5)
# stu2 = Student("Bob", 8.7)
# stu3 = Student("Charlie", 9.2)

# print(stu1.name, stu1.cgpa)
# print(stu2.name, stu2.cgpa)
# print(stu3.name, stu3.cgpa)
# print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")

# class Student:
#     college_name = "Apna College" # Class Variable
#     PI = 3.1

#     def __init__(self, name, cgpa): # Instance Variables
#         self.name = name
#         self.cgpa = cgpa
#         self.PI = 3.14 # Local Variable

# stu1 = Student("Alice", 9.5)
# print(stu1.name)
# print(stu1.cgpa)
# print(stu1.college_name)
# print(stu1.PI)
# print(Student.PI)