'''
It is used to make resusble pieces of code
Set of statements we can execute multiple times at running without writing multiple times
'''

print("-----------")
print("Creating Function")
def myfunc():
    pass #Pass is used to skip body of function
myfunc() #null fun

def sumfunc(start,end):
    result = 0
    for i in range(start,end+1): #end always comes with+1 to meet values
        result= result+i
    return result #use return when u need to obtain result via variable
   # print(result)
s = sumfunc(10,20) #passing arguments
print(s)

print("-----------")
print("Conditioned Function")
def sum(start,end):
    if(start>end):
        print("End is always higher")
        return
    result = 0 #unbound local error
    for i in range(start,end+1):
        result = result+i
    return result
s=sum(20,21)
print(s)

'''
Global and Local variables
Global--> That can be acceses inside and outside the functions, not bounded
Local--> Accessed inside the function
'''
global_variable= 23

def fnc():
    local_variable=34
    print(global_variable)#created outside the function, but able to call (GlobalVar)
    print(local_variable)
fnc()
#print(local_variable)

print("-----------")
print("same name for global and local")
#if we give same name for both local and global variable and tries to call inside the function, local variable will print.
a=15
def fu():
    a=12
    print(a)
fu()

print(a)

print("-----------")
print("same name for global and local, but need to print global")
a=15
def ft():
    global a #as we named variable as global , need to split and assign values
    a= 12
    print(a)
ft()

print(a)

print("-----------")
print("Passing arguments methods")
'''
-->Args with def values
-->Args with keywords
-->Args with mixed(def and keywords)
'''
#passing arguments with def values(positional)
def arg(a,b=14):
    print(a,b)
arg(12)
arg(12,25)

#passings args with named params(kw)
def namedparams(name,greeting):
    print(greeting +" "+ name)
namedparams('Loki','Hi') #positional
namedparams(name="Loke",greeting="Hello") #keywords

#mixed args params
def mixed(a,b,c):
    print(a,b,c)
mixed(10,20,30)
mixed(10,b=20,c=40)
mixed(10,20,c=50)
#mixed(a=10,30,50) keyword params will be written last is a restriction

print("-----------")
print("Returns mukltiple values")
#When fn returns mukltiple values, treated as tuples

def mul(a,b):
    if a>b:
        return a,b
    else:
        return b,a
s=mul(100,200)
print(s)
print(type(s))
