#Immutable,"",''
str1="Declaration 1"
str2='Declaration 2'

#id returns the memeory of the variable stored
print(id(str2))

#functions + *

str2 = str1 + "To be done"
print(str2)
print(str1*2)

print("-------------------")
print("Slicing Strings")
#Slicing[]
str= 'HiTeamWelcome'
print(str[0:7])
print(str[:9]) #defaultly taken first index value
print(str[0:]) #defaultly taken last index value
print(str[0:-1]) #defaultly removes last index when its given


print("-------------------")
#ord(),char() functions
#ord()--> gives ascii code of char
#char--> gives ascii char of value
str='e'
print(ord(str))
str=101
print(chr(str))

print("-------------------")
print("len,max,min")
#len,max,min
'''
len--> returns length of string
max--> returns max ascii value contains in string
min--> returns min ascii value contains in string
'''
str="abcde"
print(len(str))
print(max(str))
print(min(str))

print("-------------------")
print("in and not in operators")
#in and notin operator
"""in--> returns true if it exists in the string else returns false
not in --> returns false if it exists in string else returns true
"""
str="HiTeam"
print("Team"in str)
print("Team"not in str)


print("-------------------")
print("String Comparision")
#<,>,<=,>=,==,!=
#it will compare strings according to ascii value of the strings we declared
print('Loki'=="Loki")
print('LOKesh'>'LOkesh')
print('Lok'<"Loki")
print("Lok"!='LokI')
print("lok"<='lok')
print("lok">="loki")


print("-------------------")
print("For loop in String")
str = "Loki"
for i in str:
    print(i) #prints char
    print(str) #prints string

print("-------------------")
print("Testing string")
'''
isalnum --> returns true if str is alphanumeric
isaplha --> returns true if str contains only alphabets
isdigit --> returns true if str contains only digits
islower --> returns true if str contains only lowercase
isupper --> returns true if str contains only uppercase
isidentifier --> returns true if str contains valid identifier
isspaces --> returns true if str contains whitespaces
lower --> returns str  lowercase
upper --> returns str uppercaze
swapcase --> upper to lower and vicevers
capitalize --> first letter caps
title --> capitals first letter of every word in string
replace --> replace chars which reqd
'''
str='ABC;12'
str1="loki";
print(str.isalnum())
print(str1.isalpha())
print(str.isidentifier())
print(str.isdigit())
print(str1.upper())
print(str.lower())
print(str.isspace())

print("-------------------")
print("Searching for Substrings")
'''
endswith,startswith,count,finds,rfinds
'''
str='ABAAC'
print(str.endswith("c"))
print(str.startswith("A"))
print(str.count("A"))
print(str.find("a"))
print(str.rfind("C"))
