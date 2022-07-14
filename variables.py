class Car:

    # variables defined here are class variables which are common for all objects, also called static variables
    wheels = 4  

    def __init__(self): # variables defined in this method are instance variable as value changes for diff objects
        self.mil = 10
        self.com = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8

c1.wheels = 2

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)