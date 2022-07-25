"""Overloading and Overriding
same thing but different behaviour
"""
#Overrides -- same method name, one overrides the other
print("-------")
print("OverRiding")
class Bank():
    def rateofInterest(self):
        return 0
class ICICIBank(Bank):
    def rateofInterest(self):
        return 8
ob=ICICIBank()
print(ob.rateofInterest())


#Overloading -- multiple ways to execute the method
print("-------")
print("OverLoading")
class Loading():
    def cars(self,Brand='None'):
        if Brand=="TOYOTA":
            print("Fortuner")
        if Brand =="Volkswagen":
            print("Polo")
        if Brand =="None":
            print("Two wheelers")

oc=Loading()
oc.cars("Volkswagen")