'''
Class - Logical entity, contains variables and methods
Objects - Physucal entity, number of objects reqd to create class
'''
print("-----------")
print("Creating basic class and objects which includes methods")
class MyClass:
    def met(self): #self is declared to know that this method can be accessed by the class
        pass
    def met2(self,name):
        print("Name is:"+ name)
#Function declared outside class known as function
#Function declared inside class known as method
oc=MyClass() #objectcreation is simple here
oc.met()
oc.met2("Lokesh")

print("-----------")
print("instance method & static method")
class MyClass:
    def meth1(self):
        print("instance variable")
    @staticmethod #staticmethod requires @annotation
    def meth2(name):
        print("static variable")
        print(name)
oc=MyClass()
oc.meth1()
MyClass.meth2("lok") #static variable with parameters

print("-----------")
print("Declaring Variables inside the class")
class MyClass:
    a,b= 10,20 #class variables
    def sum(self):
        print(self.a + self.b)
    def mul(self):
        print(self.a*self.b)
oc=MyClass()
oc.sum()
oc.mul()

print("-----------")
print("LOCAL, GLOBAL and CLASS Variables")
a,b = 12,13
class MyClass:
    i,j= 23, 45
    def loc(self,e,f):
        print(e+f) #accessing local variables
        print(self.j+self.i) #accessing local variables
        print(a + b) #accessing global variables
oc=MyClass()
oc.loc(2,3)

print("-----------")
print("LOCAL, GLOBAL and CLASS Variables with same name")
a,b= 10,15
class MyClass:
    a,b=15,20
    def var(self,a,b):
        print(a+b) #access class var
        print(self.a+self.b) #access local variables
        print(globals()['a']+globals()['b']) #access global var

oc=MyClass()
oc.var(12,20)

print("-----------")
print("Creating Multiple objects for one class")
class MyClass:
    def many(self):
        print("Many objects creation")
oc1=MyClass() #named object
oc1.many()
oc2=MyClass()
oc2.many()
#MyClass.many() #NAMELESS OBJECT


print("-----------")
print("check memory location of object")
class MyClass:
    def memory(self):
        print("Many objects creation")
oc1=MyClass() #named object
oc2=MyClass()
oc3=oc2
print(id(oc2))
print(oc3 is oc2)
print(oc3 is not oc1)
print(oc3 is oc1)
print(id(oc3))