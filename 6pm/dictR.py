
info = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}
print(info)
print(type(info))

# stores the value by index ?
#print(info[0])

# retrive
print(info['lastName'])
print(info.get('lastName'))

# update 
info['firstName'] = "tanmay"
print(info)
info.update({'city':"pune"})
print(info)

#delete 
#del info
# info.popitem()
# info.pop("city")

# total properties 
# len(info)
# info.clear()

vehicle = {
    "color":"blue",
    "type":"sedane"
}

e = vehicle.setdefault("type","pune")
print(vehicle)
print(e)

w = dict.fromkeys(['one','two','three'])
print(w)



vehicle = {
    "color":"blue",
    "type":"sedane"
}

for item in vehicle:
    print(item,vehicle[item])


for item in vehicle.keys():
    print(item)

for item in vehicle.values():
    print(item)

for x,y in vehicle.items():
    print(x,y)

print(vehicle)
# vehicle2 = vehicle
# vehicle['color']= "red"
# print(vehicle)
# print(vehicle2)

v2 = vehicle.copy()
v2['color'] = "green"
print(v2)
print(vehicle)
print(v2)