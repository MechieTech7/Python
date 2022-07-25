'''
-->Invoke parent class methods
-->Invoke parent class variables
-->Invoke parent class constructors
'''
print("---------")
print("Invokes parent classs methods")
class A:
    def met1(self):
        print("Superclass")
class B(A):
    def met2(self):
        print("subclass")
        super().met1() #calls method from superclass/parentclass
objcr=B()
#objcr.met1()
objcr.met2()

print("---------")
print("Invokes parent classs variables")
class A:
    a,b=12,24
class B(A):
    e,f=10,22

    def m1(self,x,y):
        print(x+y)
        print(self.e*self.f)
        print(self.a+self.b)
b=B()
b.m1(2,4)

print("---------")
print("Invokes parent classs variables with same names")
a,b = 1,2
class A:
    a,b = 3,4
class B(A):
    a,b = 5,6
    def var(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(super().a*super().b) #as variables name are same, will use super kw to access parent class variables
        print(globals()['a']*globals()['b'])
ob=B()
ob.var(7,8)

print("---------")
print("Invokes parent classs constructors")
class A:
    def __init__(self):
        print("parent con")
class B(A):
    def __init__(self):
        print("Child cons") #without super, it will print constructor initialised in child class alone
        super().__init__()
obj=B()
#obj.__init__()