'''Constructor is used to initialise we dont want to call separately while calling methods
___init___ keyword
'''


class MyClass:  # Paraenthses will be optional
    def method1(self):
        print("Im a method")

    def __init__(self): #init and int will make mess
        print("Constructor")

obj = MyClass()
obj.method1()

print("-----------")
print("Accessing local to class variables")

class MyClass:
    def sum(self,var1,var2):
        print(var1) #local variables
        print(var2)
        self.var1 = var1 #setting to class variables
        self.var2 = var2
    def cls(self):
        print(self.var1+self.var2)
oc=MyClass()
oc.sum(10,24)
oc.cls()

print("-----------")
print("Accessing local to class variables with constructor passing params")

class MyClass:
    def __init__(self,var1,var2):
        print(var1) #local variables
        print(var2)
        self.var1 = var1 #setting to class variables
        self.var2 = var2
    def cls(self):
        print(self.var1+self.var2)
oc=MyClass(10,25)
oc.cls()

print("-----------")
print("Calling current class method in another method ")

class MyClass:
    def met1(self):
        print("call")
        self.met2(23)
    def met2(self,s):
        print("Bye",s)
oc=MyClass()
oc.met1()


print("-----------")
print("Constructor with arguments")

class MyClass:
  name= "Msd"
  def __init__(self,name):
       print(name) #access loc var
       print(self.name) #access class var when self exists

oc=MyClass("Loki")

print("-----------")
print("Useful Example")

class Emp:
    def __init__(self,empId,empName,empSal):
        self.empId = empId
        self.empName = empName
        self.empSal = empSal
    def details(self):
        print("Empid:%d EmpName=%s EmpSal=%g"%(self.empId,self.empName,self.empSal))
        print("Empid:() EmpName:() EmpSal:() ".format(self.empId,self.empName,self.empSal))

    '''def __str__(self):
        return ("Empid:() EmpName:() EmpSal:() ".format(self.empId,self.empName,self.empSal))'''
oc=Emp(7,"Msd",2011)
oc.details()

print("-----------")
print("__STR__")

class MyClass:
    pass
c=MyClass()
print(c)

class MyClass:
    def __str__(self):
        return "String"
oc=MyClass()
print(oc)

#del ref variable



