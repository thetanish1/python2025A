#          fn          ln      
info = ["chinmay","deshpande",23,45]
print(info)
print(type(info))

# dict 

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":44,
    "age":45
}
print(info)
print(type(info))

# does dict stores the value by index ? - No
#print(info[0])

# does dictionary allows to store the duplicate key
#print(info)

# retrive 
info = {
    #  key:'value'
    #  property:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":44,
    "age":45
}

# retrive
print(info['firstName'])
print(info['lastName'])
print(info.get('firstName'))

# update
info['firstName'] = "tanmay"
print(info)

#add
info['city'] = "pune"
print(info)

# total how properties 
print(len(info))

# particular properties exist or not 
print("city" in info)
print("City" in info)

# loop 

# range X
# while X

# for each 

info = {
    #  key:'value'
    #  property:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":44,
    "age":45
}

for x in info:
    print(x,info[x])

for x in info.keys():
    print(x)

for x in info.values():
    print(x)

for x in info.items():
    print(x)


# program 2

vehicle = {
    "color":"red",
    "type":"sedane",
    "regNo":123
}
# print(vehicle)
# print(vehicle["color"])
#vehicle.clear()
print(vehicle)

vehicle.update({'logo':"circle","startType":"audi"})
print(vehicle)