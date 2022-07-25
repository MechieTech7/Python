'''
Classes can inherit functionality of other classes
if a obj is created from a class, that inherits from super class obj contain both methods of class and suoer class
Types: single,multulevel,hybrid,hierarchial,multiple
'''
print("----------")
print("Single level inheritance")
class A:
    def met1(self):
        print("Superclass")
class B(A):
    def met2(self):
        print("subclass")
objcr=B()
objcr.met1()
objcr.met2()

print("----------")
print("multi level inheritance")
class A:
    x,y=1,2
    def m1(self):
        print(self.y+self.x)
class B(A):
    a,b =2,3
    def m2(self):
        print(self.a*self.b)
class C(B):
    e,f=5,6
    def m3(self):
        print(self.e + self.f)
c=C()
c.m3()
c.m2()
c.m1()

print("----------")
print("HIERACRCHIAL inheritance")
class A:
    x,y=1,2
    def m1(self):
        print(self.y+self.x)
class B(A):
    a,b =2,3
    def m2(self):
        print(self.a*self.b)
class C(A):
    e,f=5,6
    def m3(self):
        print(self.e + self.f)
oc=C()
c.m1()
c.m3()
oc2=B()
oc2.m2()

print("----------")
print("multiple inheritance")
class A:
    x,y=1,2
    def m1(self):
        print(self.y+self.x)
class B:
    a,b =2,3
    def m2(self):
        print(self.a*self.b)
class C(B,A):
    e,f=5,6
    def m3(self):
        print(self.e + self.f)
c=C()
c.m1()