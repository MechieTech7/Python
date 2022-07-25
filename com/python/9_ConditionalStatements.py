a=10
if a<20:
    print("Correct one")
else:
    print("Check Again")


a=10
if a<True:
    print("Correct one")
else:
    print("Check Again")

#Odd r Even
Num1=int(input("Enter Number"))
if Num1%2 == 0:
    print("User input is Even")
else:
    print("User input is Odd")

#Multiple statements
if False:
    print("When its true, If block will execute")
    print("Statement 1")
    print("Statement 1")
else:
    print("Statement 2")
    print("When its False, else will execute")

#Single line execution

print("Trying if else in single line") if True else print("False come, I appear")

#Single line execution multiple statements {}

{print("Dhoni is Inspiration"),print("Capsy cool")} if False else {print("When it comes to nation"),print("everything comes next")}


#elif condition

a="Dhoni"

if a=="Kholi":
    print("You are Vk fan")
elif a=="Rohit":
    print("You are Sachin fan")
elif a=="Abd":
    print("You are RCB fan")
else:
    print("You are Mighty Mahi fan")

#else block is optional for elif statement
#but if conditions not going to be matched with elif / if blocks , it shows null.

