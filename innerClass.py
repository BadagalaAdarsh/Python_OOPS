class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollNo = rollno
        self.laptop = self.Laptop()

    def show(self):
        print('hai')
        print(self.name, self.rollNo)
        self.laptop.show()

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.processor = "i5"
            self.ram = 8

        def show(self):
            print('bye')
            print(self.brand, self.processor, self.ram)


student1 = Student("adarsh",12)
print(student1.show())

student2 = Student.Laptop()
student2.show()
