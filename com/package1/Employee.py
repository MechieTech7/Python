class Emp:
    def __init__(self,empId,empName,empSal):
        self.empId = empId
        self.empName = empName
        self.empSal = empSal
    def details(self):
        print("Empid:%d EmpName=%s EmpSal=%g"%(self.empId,self.empName,self.empSal))