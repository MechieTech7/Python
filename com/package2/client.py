#gonna access modules from diff pack
import sys
sys.path.append("C:\\Users\\lokesh.chandramurthy\\PycharmProjects\\LearnPython\\com\\package1")
#Approach1
import module1
module1.display()
import module2
module2.show()

#Apprach2
from module1 import* #we dont want to call module name here by specify,but we can import all methods diesctly  by using*
from module2 import*

display()
show()