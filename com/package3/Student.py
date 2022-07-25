class Stu:
    def __init__(self,stuId,stuName,stuAge):
        self.stuId = stuId
        self.stuName = stuName
        self.stuAge = stuAge
    def details(self):
        print("Stuid:%d StuName=%s StuAge=%g"%(self.stuId,self.stuName,self.stuAge))