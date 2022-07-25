'''
Function which has no name is known as Lambda function, also known as Anonymous function
Lambda fn can take many num of args but have only one expression
syntax: Lambda aarguments : expression
'''

print("--------")
print("Passing one arg")
x=lambda a: a*4
print(x(3))

print("--------")
print("Passing two args")
x=lambda a,b: a*b
print(x(3,4))

print("--------")
print("Passing multiple args")
x=lambda a,b,c: a+b*c
print(x(3,4,5))

print("--------")
print("Function example comp with lambda")
'''x=lambda a: a*4 
print(x(3))'''

#lambda we can achieve by 2 lines, whereas function needs 4 lines to achieve this
def fun(a):
    a=a+5
    return a
print(fun(5))