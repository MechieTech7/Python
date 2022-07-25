'''
List is another sequence of datatypes defined by list class
allows add/delete or process elements
similar to arrays
'''
print("--------------")
print("List creation")
#Ways of creating list
list1= list()
print(list1)
list2=list(["Loke","Dhoni",7,"Hetergenics",75,98.32])
print(list2)
list3=list("Lokesh") #square brackets are not used to get separate char
print(list3)

print("--------------")
print("Accessing elements from list")
#Using index numbers with help of [] we can access
print(list2[0])

print("--------------")
print("Common operations in List")
#in,not in,+,len(),min(),max(),sum(),*,+
numList= list([1,2,3,4,5])
n2= list([2,3,4,5,8])
print(1 in numList)
print(6 not in numList)
print(max(numList))
print(min(numList))
print(sum(numList))
print(len(numList))
print(numList+n2) #concats two list seq
print(numList*2) #replicates

print("--------------")
print("List Slicing")
#First and Last index will be optional
print(numList[0:3])
print(n2[:4]) #Defaulty 0
print(n2[2:]) #Defaulty last index value

print("--------------")
print("For loop iteration in lists")
for i in numList:
    print(i)
    #print(i, end=" ")

print("--------------")
print("Commonly used operations in List")
#Append,Count,Extend,index,insert(index),remove,reverse,sort,pop
newList=[2,4,6,8]
newList1=[2,4]
newList.append(12) #Appends elements to the list
print(newList)
print(newList.count(12))#Count number of occurences
newList.extend(newList1) #extends to the list already created
print(newList)
print(newList.index(12))#returns index position if element
newList.insert(0,24) #adds element to the index postion
print(newList)
print(newList.pop(1)) #returns and removes element in index position
newList.remove(12) #removes the element when we pass value
print(newList)

newList.reverse() #it will rverse the list
print(newList)

newList.sort() #sort will sort elements in asc ord
print(newList)

print("--------------")
print("List Comprehenesion")
forList=[ x for x in range(10)] #range of 0-9
print(forList)
forList=[ x+1 for x in range(10)] #range of 1-10
print(forList)
forList=[ x for x in range(10) if x%2== 0] #range of 0-10 in even
print(forList)
