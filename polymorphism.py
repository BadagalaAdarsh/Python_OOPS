# there are four ways of implementing the polymorphism in python
# first one is duck typing
# operator overloading
# method overloading
# method over riding

# we use duck typing to tell that all the variables or objects in python are dynamic

class PyCharm:

    def execute(self):
        print("compiling the code in pycharm.........")
        print('executing the code in pycharm..........')


class Anaconda:

    def execute(self):
        print("compiling the code in anaconda..........")
        print("executing the code in anaconda..........")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = PyCharm()

laptop1 = Laptop()
laptop1.code(ide)

print()

ide = Anaconda()
laptop1.code(ide) # as you can see here the type of ide which is of user defined type is not fixed to pycharm
# we can change it to whatever type we want provided they have the same method in this case execute method
# it is because in the laptop class we are calling the execute method so no matter what type is the ide
# it should consist the method execute so that it can be called
