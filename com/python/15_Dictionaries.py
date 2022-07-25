""""
-->Dictionary is python is similar to java maps
-->key value pairs
-->add/remove/modify using keys
-->mutable
-->Created using {}
-->Keys must be unique, values can be same
-->separated by commas
"""

print("----------")
print("Creation of dictionary")
Cricketers={'7': 'Dhoni', "18": "Vk"}
print(Cricketers)

print("----------")
print("Retrieving,Removal and adding")
print(Cricketers["7"]) #Retrives value from respective key
Cricketers['32']="Mccullum" #Adds pair to the existing dictionary when name is called
print(Cricketers)
Cricketers['32']="Bazyy" #Replaces with the newly added value
print(Cricketers)
del Cricketers['32'] #deletes the pair in the dictionary
print(Cricketers)
print(len(Cricketers)) #Returns size of dictionary

print("----------")
print("Looping pairs in dictionary")
for x in Cricketers:
    print(x,";",Cricketers[x])

print("----------")
print("Equality tests")
#Use only ==, != operators
#Cnt use <,> operators
newCricketers={"54":"Cherry","17":"AbD"}
print(Cricketers == newCricketers)
print(Cricketers != newCricketers)


print("----------")
print("DictionaryMethods")
#popitem(),clear(),keys(),values(),get(key),pop(key)
print(newCricketers.popitem()) #Randomly selcts and removes element
print(newCricketers)
newCricketers.clear() #deletes everything inside dictionary
print(newCricketers)
print(Cricketers.keys()) #Gets keys from the dictionary, comes in tuple format
print(Cricketers.values()) #Gets Values from the dictionary, comes in tuple format
print(Cricketers.get('7')) #Gets value of respective key

print(Cricketers.pop('18')) #Popitem differs from pop by seleacting a key
print(Cricketers)