#Accessing modules from two different packages
import sys
sys.path.append("C:\\Users\\lokesh.chandramurthy\\PycharmProjects\\LearnPython\\com\\package3")
from mod1 import *
display()

sys.path.append("C:\\Users\\lokesh.chandramurthy\\PycharmProjects\\LearnPython\\com\\package3\\subpack")
from mod2 import *
show()