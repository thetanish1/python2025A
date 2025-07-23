# retrive , update add , delete , elementRepreset

info = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":35,
        "city":"pune",
        "skills":["python","js"]
    },

    {
        "firstName":"amol",
        "lastName":"rao",
        "age":34,
        "city":"mumbai",
        "skills":["python","js","sql","excel"]
    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":26,
        "city":"pune",
        "skills":["python","js","cypress","sql","selenium"]

    }
    ,
    {
        "firstName":"poorva",
        "lastName":"vyas",
        "age":25,
        "city":"nagpur",
        "skills":["python","django","sql"]
    }
]

#print(type(info))
print(info[0])

# print firstName from dictionary
for x in info:
    print(x['firstName'])

# name : 3

firstName = "chinmay"
lastName = "deshpande" 

# my firstName is chinmay and lastName is deshpande
print(f'my firstName is {firstName} and lastName is {lastName}')


for x in info:
    print(f'{x['firstName']}:{len(x['skills'])}  ')


# age above 30
for x in info:
    if x['age'] > 30:
        print(x['firstName'])

for x in info:
    if "sql" in x["skills"]:
        print(x['firstName'])

for x in info:
    if "sql" in x["skills"] and x['city'] == 'pune':
        print(x['firstName'])


for x in info:
    x['skills'].append("html")
print(info)

total = 0
for x in info:
    total = total + x['age']
    #        0    +    35 ----> 35
    #        35   +    34 ----> 69
    #        69   +    26 --->  95
    #        95   +    25 --->  120

total/len(info)   