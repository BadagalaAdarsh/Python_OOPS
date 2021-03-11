# all the operators that we generally use in programming language have built in methods working behind the screen
# like if we add two integers its going to call int.__add__ similarlay sub and so on

class Student:

    def __init__(self, mark1, mark2):
        self.mark1 = mark1
        self.mark2 = mark2

    def show(self):
        print(self.mark1, " ", self.mark2)

    def __add__(self, otherobject):
        mark1 = self.mark1 + otherobject.mark1
        mark2 = self.mark2 + otherobject.mark2

        student3 = Student(mark1, mark2)
        return student3

    def __gt__(self, other):
        student1Marks = self.mark1 + self.mark2
        student2Marks = self.mark1 + self.mark2

        if student1Marks > student2Marks:
            return True
        return False

    def __str__(self):
        # if we directly print the student i.e print(student1) we get error saying it is returning a non str type
        # to overcome this problem we need to convert it to string
        # this can be done by using the format method
        # "{} {} ". format(self.mark1, self.mark2)
        return self.mark1, self.mark2



student1 = Student(50, 60)
student2 = Student(60, 80)

student3 = student1 + student2

student3.show()

# other example of operator overloading

if student1 > student2:
    print("Student 1 has scored more marks")
else:
    print("Student 2 has scored more marks")

# whenever we want to print some thing behind the scene it is going to call the __str__ method
# if we directly try to print the object then it is going to print the address of that object
# if we want to print the values of the object then we have to override the __str__ method by writing our own definition

# note that print(student1) given error that str is returning the non string type
# to over come we can use the format method which {} {}. format(self.mark1, self.mark2)
print(student1.__str__())


