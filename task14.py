class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"{self.name} - {self.age} yosh")

student1 = Student("Ali", 15)
student2 = Student("Vali", 17)
student3 = Student("Jasur", 16)
student4 = Student("Aziz", 18)
student5 = Student("Dilnoza", 14)

students = [student1, student2, student3, student4, student5]

oldest = students[0]
for s in students:
    if s.age > oldest.age:
        oldest = s

print("Eng katta yoshdagi talaba:")
oldest.show_info()
