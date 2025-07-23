#listA  = ["chinmay","deshpande",34,56]


# dict 
info = {
    # key:value
    # property:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":56
}
print(info)
print(type(info))

# program 2
# does it stores the value by index ? - No
info = {
    # key:value
    # property:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":56
}
#print(info[0])
print(info['firstName'])
print(info.get('lastName'))

# program 3
# particular property exist ????
vehicle  = {
    "color":'blue',
    "type":'sedane'
}
print("color" in vehicle)
print("Color" in vehicle)

# update 
# program 4
vehicle  = {
    "color":'blue',
    "type":'sedane'
}
print(vehicle)
vehicle['color'] = "red"
print(vehicle)

vehicle.clear()
print(vehicle)

# program 5
# does list store duplicate values - 
numbers  = [11,22,33,44,55,66,77,11]
print(numbers)

# does dict allows to store duplicate values 
vehicle  = {
    "color":'blue',
    "type":'sedane',
    "color":"red",
    "regNo":123
}
print(vehicle)
# total number of properties in dict
print(len(vehicle))

#del vehicle
print(vehicle)
vehicle.pop('type')
print(vehicle)
vehicle.popitem()
print(vehicle)

# program 7

tiger = {
    "color":"red",
    "city":"bengal"
}

print(tiger['color']) # red
tiger['color'] = "white"
print(tiger)
tiger['count'] = 3
print(tiger)

# create , retrive , update , delete
# element/property exist , doesStoreValueByValue , duplicate,clear, duplicate


# loop

# program 8

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34,
    "rollNo":56
}

for x in info:
    #print(x)
    print(info[x])


vehicle = {
    "color":"red",
    "regNo":123 
}

for x in vehicle:
    print(x)
    print(vehicle[x])

for key in vehicle.keys():
    print(key)

for val in vehicle.values():
    print(val)

for x,y in vehicle.items():
    print(x,y)