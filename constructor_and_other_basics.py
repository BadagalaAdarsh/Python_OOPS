
class Computer:

    def __init__(self):
        self.name = 'adarsh'
        self.age = 20

    def compare(self, otherObject):

        if self.age == otherObject.age:
            return True
        else:
            return False



computer1 = Computer()
computer2 = Computer()

print(computer1.name)
print(computer2.name)

computer1.age = 30

print()

# computer1.name = 'anusha'
#
# print(computer1.name)
# print(computer2.name)

if computer1.compare(computer2):
    print("They are same")

else:
    print("They are different")

