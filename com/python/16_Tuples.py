'''
Tuples cannot add/remove/replace
Tuple is immutable
Tuple starts with ()
'''

print("----------")
print("Tuple Creation")
tup1=(2,4,7)
tup2=([2,2,3,3,3])
tup3=tuple("abc") #it will automatically split into  multiple chars
print(tup3)
print(tup2)
print(tup1)

print("----------")
print("Tuples Functions")
#max,min,length,sum
print(max(tup1)) #returns maximum value in a sequence
print(min(tup1)) #returns minimum value in a sequence
print(len(tup1)) #returns length of a tulip
print(sum(tup1)) #returns sum of tulip

print("----------")
print("Tuples Iteration")
for i in tup1:
    print(i, end=" ")

print("----------")
print("Slicing Tuples")
print(tup1[0:2])
print(tup1[:2])
print(tup1[0:])

print("----------")
print("In and Not in operator")
print(2 in tup1)
print(54 not in tup1)
print(45 in tup1)