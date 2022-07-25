import a

c=a.Car()
c.m2()

import b
d=b.Bike()
d.m1()

from a import Car
c=Car()
c.m2()
from b import Bike
d=Bike()
d.m1()

print(dir(b))