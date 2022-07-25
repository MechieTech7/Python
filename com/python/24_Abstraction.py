'''
-->Abstract classes are the clasees that contains one or more abstract methods
-->Abstract methods may or may not contains implementation
-->We cannot directly create object for abstract class, we can achieve it via subclass
-->Know requirements, we dont know implements
-->ABC Predefined abstract class in Python
'''

print("----------")
print("Simple example")
from abc import ABC,abstractmethod
class A(ABC):
       @abstractmethod
       def abs(self):
        None

class D(A):
    def abs(self):
        print("check")
ob=D()
ob.abs()

print("----------")
print("Simple example")
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        None

class Tiger(Animal):
    def eat(self):
        print("Hunts")
class Cow(Animal):
    def eat(self):
        print("Grass")
t=Tiger()
t.eat()
c=Cow()
c.eat()

print("----------")
print("Complex example,2 abs methods")
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def abs1(self):
        None
    @abstractmethod
    def abs2(self):
        pass
class B(A):
    def abs1(self):
        print("1st methood retrieved")
class C(B):
    def abs2(self):
        print("2nd abs retrieved")
obj=C()
obj.abs1()
obj.abs2()

print("----------")
print("Constructor abstraction example")
from abc import ABC,abstractmethod
class A(ABC):
    def __init__(self,value):
        self.value=value
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def sub(self):
        pass
class B(A):
    def add(self):
        print(self.value+25)
    def sub(self):
        print(self.value - 34)
oc=B(100)
oc.add()
oc.sub()