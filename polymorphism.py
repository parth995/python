# poly -> Many
# Morph -> Form

# Types:
# - duck typing
# - operator overloading
# - method overloading
# - method overriding

class PyCharm:

    def execute(self):
        print('compiling....')
        print('Runnnig....')

class MyEditor:

    def execute(self):
        
        print("Spell check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:

    def code(self, ide):
        ide.execute()

ide = MyEditor()     

lap1 = Laptop()
lap1.code(ide)