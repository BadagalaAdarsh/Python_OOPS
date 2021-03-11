
# python doesn't have method overloading
# but it can be done in different ways
# say we need to overload add method instead of writing add method twice with different no of arguments
# we can do it like
# def add(a= None, b = None, c = None):
#   if a!=b!=c!=None:
#       return a+b+c
#   elif a!=b!=None:
#       return a+b
#   else:
#       return a

# another way of doing this is using decorator ( specifically dispatcher)

'''
from multipledispatch import dispatch


@dispatch(int)
def func(x):
    return x * 2

@dispatch(float)
def func(x):
    return x / 2

# Driver code
print(func(2))
print(func(2.0)

'''

class A:

    def show(self):
        print("Show method of class A")

class B(A):
    def show(self):
        print("Show method of class B")

b = B()
b.show()