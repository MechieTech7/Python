'''
**kwargs is used to represent the key and value and pass arguments to keys
* key
* value
'''
print("--------")
print("Pass arguments to function")
def passing(a,b,c):
    print(a,b,c)

a={'a':'Msd','b':'vk','c':'Bazzy'}
passing(**a)

print("--------")
print("Receive arguments to function")
def receiving(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

receiving(name='ms',num='7')