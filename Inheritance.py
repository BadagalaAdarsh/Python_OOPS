# the main concept of inheritance is same as java
# that is accepting or acquiring the qualitiY

class A:

    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")


class B(A):

    def feature3(self):
        print("This is feature 3")

    def feature4(self):
        print("This is feature 4")


class C(B):

    def feature5(self):
        print("This is feature 5")

    def feature1(self):
        print("Hope it overrides feature 1")


class D:

    def method1(self):
        print("Method one of D")

class E:

    def method2(self):
        print("Method two of E")

class F(D,E):

    def method3(self):
        print("Method three of F")


a = A()
a.feature1()
a.feature2()

print()

b = B()
b.feature1()
b.feature2()
b.feature3()
b.feature4()

print()
c = C()
c.feature5()
c.feature1()

print()
f = F()
f.method1()
f.method2()
f.method3()