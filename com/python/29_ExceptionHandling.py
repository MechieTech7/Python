'''
Error-->Syntax error/Logical error
Exception - abnormal condition disturbs normal flow of program
Errors- prgmming mistakes,, Exception- User input mistakes

Keywords--> try,except,else,finally
try--> try the logic
except--> block to be executed when exception occurs
else-->block will be executed when exception not occurs
Finally --> block will execute whether its a exception or not

Zerodivision error -->num divided by zero
Attribute error -->Attribute cant be defined but trying to find its length and perform actions
Type error --> Datatypes different
Many exceptions are there
'''

print("-----------")
print("Exception handling hierarchy")

print("Pgm is started")
try:
  print(10/0)
except ZeroDivisionError:
 print("Handled zd Exception")
except TypeError:
    print("Hanlded Te exception")
else:
    print("NO exception")
finally:
    print("No matter I come")

print("Program Completed")

print("-----------")
print("Raising an exception")

def enterage(age):
    if age < 0:
       raise ValueError("Use Positive Numbers")
    if age% 2== 0:
        print("Even age")
    else:
        print("odd age")

try:
 enterage(-1)
except ValueError:
    print("Use number greater than zero")

print("-----------")
print("printing an exception name")
try:
 name = loki
 print("name is"+ name)
except TypeError as n:
    print("error was:", n)
except NameError as T:
    print("Error was:" , T)
