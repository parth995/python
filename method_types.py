class Student:

    school = "SSGS"

    def __init__(self, m1, m2, m3):  # instance method
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):   # instance method as it involves objects
        total = (self.m1 + self.m2 + self.m3)/3
        return total

    def get_m1(self):  # accessor method - getters method
        return self.m1

    def set_m1(self, value):   # mutators method - setters method
        self.m1 = value

    @classmethod       # known as decorators and this declaration used to make method as class method type
    def getSchool(cls):   # use class variables - class method
        return cls.school

    @staticmethod    # known as decorators and used to perform operations when no instance or class method are used
    def info():
        print("This is student class....in abc module")


s1 = Student(10,15,15)
s2 = Student(20,25,25)

print(s1.avg())
print(s2.avg())

print(s1.m1)

s1.set_m1(50)

print(s1.m1)

print(Student.getSchool())