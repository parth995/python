class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
     #   self.lap = self.Laptop(self)  #laptop object is created for inner class inside student class

    def show(self):
        print(self.name, self.rollno)
       # self.lap.show()

    class Laptop:

        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
    
        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = Student('Parth', 2)
s2 = Student('Patel', 3)

s3 = Student.Laptop('HP', 'i7', 8)
s4 = Student.Laptop('Dell', 'i5', 12)

# print(s1.name, s1.rollno)
# print(s2.name, s2.rollno)

print("$" * 100)

# s1.show()
# s2.show()

# lap1 = s1.lap
# lap2 = s1.lap

# print(lap1)
# print(lap2)

s1.show()
s2.show()
s3.show()
s4.show()