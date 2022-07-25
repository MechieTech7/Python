name= "Lokesh"
id = 1849
percentile = 98.72

#Approach1
print(name,id,percentile)

#Approach2
print("Name is :",name)
print("id is:",id)
print("Percent is",percentile)

#Approach3(%operator)
#(%s - string// %d - integer// %f,%g - float)
print("Name:%s Id:%d Percent:%g"%(name,id,percentile))

#Approach4({}operator)
print("Name:{} Id:{} Percent:{}".format(name,id,percentile))

#Approach5(Index)
print("Name:{0} Id:{1} Percent:{2}".format(name,id,percentile))