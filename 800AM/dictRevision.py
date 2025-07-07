#       
info = ["chinmay","deshpande",34,55]
print(info)
print(type(info))

# dict 
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":55
}
print(info)
print(type(info))
# does dict stores the value by index ?? - NO
#print(info[0])
# Does dictionary allows to store duplicate values  ?? - No
info = {
    # property :value
    #  key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":55,
    "rollNo":66
}
print(info)
# Does particular key and value exist ?
print("Age" in info)
# total number keys and values 
print(len(info))
# update any property in key or value 
info['firstName'] = "ram"
print(info)
# adding the firstProperty 
info['city'] = "pune"
print(info)
# looping through dictionary 
info = {
    # property :value
    #  key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":55,
}
for x in info:
    print(x,info[x])
for x in info.keys():
    print(x)
for x in info.values():
    print(x)
for x in info.items():
    print(x)

# program 3
info = {
    # property :value
    #  key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":55,
}   
print(info)
e = info.get('firstName')
print(e)
f = info['firstName']
print(f)

info.popitem()
print(info)

info.pop('lastName')
print(info)

# info.clear()
# print(info)

#del info
#print(info)

info.update({"city":"pune","language":"marathi"})
print(info)
e = dict.fromkeys(["keyOne","keyTwo","keyThree"],7)
print(e)
f = info.setdefault('pincode','411028')
print(f)

vehicle = {
    "color":"red",
    "type":"sedane"
}
vehicle2 = vehicle
vehicle['color'] = "blue"
print(vehicle)
print(vehicle2)
# str - complete