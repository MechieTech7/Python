'''
It is restricting access to data and variables
Private methods and private variables
Wrapping up in a single unit
private variable with __
Private methods and private variables can be accessed only with in the class
'''

print("----------")
print("Private Variable Example")
class MyClass:
    __b=5 #private variable
    def m1(self):
        print(self.__b)
obj=MyClass()
obj.m1()
#print(MyClass.__b) cant access as it is private

print("----------")
print("Private Method Example")
class MyClass:
    def __priv(self):
        print("Private method")
    def pub(self):
        print("Public method")
        self.__priv()
obj=MyClass()
obj.pub()
#if i try to call private method directly from object, it will throw error

print("----------")
print("Modify Private Variable Example")
class MyClass:
    __b=5 #private variable
    def m1(self,a):
        self.__b = a
    def m2(self):
        print(self.__b)
obj=MyClass()
obj.m1(4)
obj.m2()