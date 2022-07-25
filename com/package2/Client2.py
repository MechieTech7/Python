#Accessing different classes from different modules of diff package
import sys
sys.path.append("C:\\Users\\lokesh.chandramurthy\\PycharmProjects\\LearnPython\\com\\package1")
from Employee import Emp
e=Emp(7,'Msd',2011)
e.details()

sys.path.append("C:\\Users\\lokesh.chandramurthy\\PycharmProjects\\LearnPython\\com\\package3")
from Student import Stu
s=Stu(32,"Bazzy",22)
s.details()