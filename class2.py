class Computer:
    
    def __init__(self):
        self.name = "Parth"
        self.age  = 28

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()  # heap memory stores objects
c1.age = 30
c2 = Computer()

# print(id(c1))
# print(id(c2))

c1.name = "Patel"

if c1.compare(c2):
    print("They are same...")
else:
    print("They are different")

#c1.update()

print(c1.name, c1.age)
print(c2.name, c2.age)