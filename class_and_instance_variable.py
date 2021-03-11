# instance variables are different for different objects
# that is they can be assigned different values for different objects
# and if we change one object it is not going to change the other object

# but if we want a variable in such a way that if we change it's value then
# it should be changed for all other variables then these type of variables are called class varibles

# if we have a variable inside the init then it becomes the instance variable
# but if we have variable outside the init but inside the class then it becomes the class variable

class Car:
    # here wheels is the class variable and it is same for all the objects that are created based on this class
    wheels = 4

    def __init__(self):
        # these are the instance variables
        self.mileage = 10
        self.company = "BMW"


car1 = Car()
car2 = Car()

print("mileage of car 1 is ", car1.mileage, " and company is ", car1.company, " and it has ", car1.wheels, " wheels")
print("mileage of car 2 is ", car2.mileage, " and company is ", car2.company, " and it has ", car2.wheels, " wheels")
# we call also call the wheels by using the class itself
print("checking wheels value using the class name", Car.wheels)
print()

# if we want to change class variable of only one object then we can do it in following way
car1.wheels = 10
print("car1 wheels changed to ", car1.wheels)
print("wheels value in Car class", Car.wheels)

# but if we want to change for all the objects then we have to use class name to do it
Car.wheels = 20
# note that even after using the class name the output of car1.wheels is still 10
print()
print("after changing wheels value using the class name")
print("car1 wheel value is not changed", car1.wheels)
print("but car2 wheels changed",car2.wheels)

# but if we create a new object of class car and say it car3 then its wheel value will be changed
car3 = Car()
print("similarily after creating the new object car3 its value too changed",car3.wheels)

Car.company = "check"
print()
print("after changing the instance value using class name")
print("name of company called using the class is changed", Car.company)
print("but the object value is still the same")
print(car1.company)
print(car2.company)
print(car3.company)

# observe here that if we try to change the value of instance variable using the class name
# then it not going to effect the other object value
# even after changing the company to check the value of car1,car2 and car3 is still BMW