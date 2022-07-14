class A:   # super class
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B(A):     # child class getting inherting from A - also called as Sub Class
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class C(B):   # adds multi-level inheritance C->B->A
    def feature5(self): 
        print("Feature 5 working")

a1 = A()
print('$$$$$$')
a1.feature1()
a1.feature2()

b1 = B()
print('$$$$$$')
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

c1 = C()
print('$$$$$$')
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
