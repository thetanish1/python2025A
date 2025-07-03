# list
#          fn        ln       rn ag
info = ["chinmay","deshpande",23,55]

# descriptive
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":55
}
print(info)
print(type(info))


# program 2
vehicle = {
    # property : value
    # key   : value
    "color":"blue",
    "type":"sedane",
    "companyName":"BWM"
}
print(vehicle)
# does dictionary stores the value by index ?
#print(vehicle[0])
# retrive 
print(vehicle['color'])
print(vehicle.get('color'))


vehicle = {
    "color":"blue",
    "type":"sedane",
    "companyName":"BWM"
}
print("color" in vehicle)
print("Color" in vehicle)

# how many key and values 
print(len(vehicle))
# update 
vehicle['color'] = "red"
print(vehicle)
# dictionary does not store duplicate values 

info = {
    "fullName":"chinmay deshpande",
    "age":34,
    "age":45
}
print(info)



# program 2

vehicle = {
    "color":"blue",
    "type":"sedane",
    "companyName":"BWM"
}

for x in vehicle:
    print(x,vehicle[x])

for x in vehicle.keys():
    print(x)

for x in vehicle.values():
    print(x)

for k,v in vehicle.items():
    print(k,v)

r = dict.fromkeys(['key1','key2','key3','key4'],0)
print(r)


# program 3


vehicle = {
    "color":"blue",
    "type":"sedane",
    "companyName":"BWM"
}

# vehicle.pop('color')
# vehicle.popitem()
# vehicle.clear()
# print(vehicle)

vehicle.update({"city":"pune"})
print(vehicle)

e = vehicle.setdefault('city','nagpur')
print(e)

vehicle.setdefault('wheel','4')
print(vehicle)
