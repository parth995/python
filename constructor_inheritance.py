class A:   # super class

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B:     # child class getting inherting from A - also called as Sub Class

    def __init__(self):
       # super().__init__()  # calls init method of class A (super class)
        print("in B init")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(A,B):
    
    def __init__(self):
        super().__init__()   # simply this calls init method of A
        print("in C init")
    
    def feat(self):
        super().feature2()   

#a1 = A() # calls init constructor of A

#a1 = B() # calls init constructor of B if B has init defined

a1 = C()
a1.feat()