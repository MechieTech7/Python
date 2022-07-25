'''
Args can be used to pass multiple values when reuired.
*args (not args followed by * we can mention anything) can be used.
'''
print("--------")
print("Receive arguments")
def add(*args):
    s=0
    for i in args:
        s+=i #s=s+i
        print("Sum of values passed:" , s)

add(1,2,3) #we can pass as many values.

print("--------")
print("Pass arguments to function")
def passing(a,b,c):
    print(a,b,c)
args=[1,3,5] #List creation
passing(*args)
#Abv example works when arguments must be same as params passed
