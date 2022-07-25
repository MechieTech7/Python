#Dynamically accepts ---> Python
a=1
b=2.5
c="String"
d='Str'
e=True

print(type(a))

#Parantheses made must in V3
print(a+b);
print(c);
print(d);
print(e);


#To pass multiple values to variables assigned in a single line
a,b,c = 10,2.5,'Easy'
print(a,b,c);

#If all values of variables are same, we can use like this
a=b=c=1
print(a,b,c)

#Replacing values between two variables
x=2
y=4.5

x,y=y,x
print(x,y)