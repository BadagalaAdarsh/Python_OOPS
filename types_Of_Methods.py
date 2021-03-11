# there are basically three types of methods in the python language
# they are instance methods
# class methods
# static methods

class Student:
    school = "Bhashayam"

    def __init__(self, mark1, mark2, mark3):
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def average(self):
        return (self.mark3 + self.mark2 + self.mark1) / 3

    @classmethod
    def getSchoolName(cls):
        # if we directly try to call this method usign any method then it will rasie error
        # to overcome we need to use the something called decorators
        # they are denoted by the @ symbol
        # print(cls.mark3)
        # print(cls.mark2)
        # print(cls.mark1)
        return cls.school

    @classmethod
    def changeSchoolName(cls, name):
        cls.school = name


    @staticmethod
    def info():
        print("This is being print inside the static method of the student class")


student1 = Student(10, 20, 30)
student2 = Student(30, 10, 50)

print()
print("Average of first student is ", student1.average())
print("Average of second student is ", student2.average())
print()
# note that the class method can be called both by using the class and instance of the class
# both as the same effect on it as long as we pass the same arguments

student1.changeSchoolName("Narayana")
print(student1.school)


print(Student.getSchoolName())
print(student1.getSchoolName())
student2.school = "Chaitanya"

print(Student.school)
print(student1.school)
print(student2.school)
print()

student1.changeSchoolName("Satyam")

print(Student.school)
print(student1.school)
print(student2.school)
print()

student2.changeSchoolName("Adarsh")
print(Student.school)
print(student1.school)
print(student2.school)
print()

student2.school = "anusha"
print(Student.school)
print(student1.school)
print(student2.school)
print()

Student.info()
student1.info()
