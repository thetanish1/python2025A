# info  = {
#     "firstName":"chinmay",
#     "lastName":"deshpande"
# }
# print(info)
# # is it dict ?
# print(type(info))

# # program 2
# # does  it stores the value by index ?
# #print(info[0])

# info2  = {
#     "firstName":"chinmay",
#     "lastName":"deshpande",
#     "firstName":"ram"
# }
# print(info2)

# # how many properties and values 
# print(len(info2))
# #particular key exist ?
# print("firstName" in info2)


# del info2
# print(info2)

# program 2

# CRUD 

# create  , retirve , update , delete , valueExist , duplicate
# storage , loop
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34
}
print(info['age'])
e = info.get('age')
print(e)

# program 2
print("hello")
#print(info['Age'])
print(info.get('Age'))
print("bye")

# program 3
info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34
}

info.pop('age')
print(info)
info.popitem()
print(info)


info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34
}
info.update({'city':"pune"})
print(info)
info.update({'city':"nagpur"})

# program 6

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34
}

for k in info:
    print(k,info[k])

for k in info.keys():
    print(k)

for v in info.values():
    print(v)

for k,v in info.items():
    print(k)
    print(v)


# program 7


info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34
    #"city":"nagpur"
}

e = info.setdefault('city','mumbai')
print(e)
print(info)

# program 8
e = dict.fromkeys(["keyOne","keyTwo","keyThree"],None)
print(e)

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34
    #"city":"nagpur"
}

info.clear()
print(info)



info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":34
}

# info2 = info
# info['firstName']  = "ram"
# print(info)
# print(info2)

info3 = info.copy()
info3['firstName'] = "one"
print(info)
print(info3)