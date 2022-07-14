class Computer:

    def __init__(self, cpu, ram): # special method to initialize variables
      #  print("In init") # called for every object
        self.cpu = cpu
        self.ram = cpu

    def config(self): # -> Method defines behaviour 
        print("Config is :", self.cpu, self.ram)
    
# a = '8'
# print(type(a))

com1 = Computer('i5', 16)

# print(type(com1))

com2 = Computer('i7', 8)

# calling method passing objects
# Computer.config(com1)
# Computer.config(com2)

# calling methods from objects
com1.config()
com2.config()