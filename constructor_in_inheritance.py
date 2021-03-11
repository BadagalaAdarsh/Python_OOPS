# MRO --> Method Resolution Order
# it is nothing but when there is multiple inheritance the priority of calling the method is from left to right

class A:

    def __init__(self):
        print("Init of A")

    def feature1(self):
        print("feature 1 in A")


class B:
    def __init__(self):
        print("init in B")

    def feature1(self):
        print("feature 1 of B")


b = B()
b.feature1()
print()


class C(A):
    def __init__(self):
        super().__init__()
        print("Init of C")


c = C()
print()


class D(A, B):


    def __init__(self):
        self.name = "Adarsh"
        super().__init__() # we can use the super method to call the other instance methods of the super class too
        # just like java 
        print("init in D")

    def show(self):
        print(self.name)


d = D()
d.feature1()
d.show()
