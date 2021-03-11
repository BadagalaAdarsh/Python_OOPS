# working on basics of the python OOP's concepts

class Computer:

    def __init__(self, cpu, ram):
        # this is the constructor in python
        # generally we use this for initializing the variables because thats what the
        # constructor does
        # main advantage or we can say that the behaviour of the constructor is that we need not call the
        # constructor or this method explicitly it gets called automatically every time we create a object
        # print("This is the constructor")
        self.cpu = cpu
        self.ram = ram

    def configuration(self):
        # print("Hello I am a Lenovo idea pad with i5 chipset and 8 Gigs of RAM")
        print("Your system configuration is ", self.cpu, " and ", self.ram, " ram ")


computer_1 = Computer('i5', 16)
# below is how you call the method inside a specific class using that class and passing the instance3
# of the class as a parameter
# Computer.configuration(computer_1)

# you can also call the same method in the following way
computer_1.configuration()

computer_2 = Computer('AMD Ryzer 5', 32)
computer_2.configuration()
