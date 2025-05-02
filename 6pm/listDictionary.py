
students = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":28,
        "rollNo":34,
        "skills":["python","javascript","html","css"]   ,
        "city":"pune"
    },
    {
        "firstName":"amol",
        "lastName":"dani",
        "age":28,
        "rollNo":33,
        "skills":["python","javascript","html","css"]  ,
        "city":"mumbai"

    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":34,
        "rollNo":32,
        "skills":["python","javascript"]  ,
        "city":"jaipur"
    },
    {
        "firstName":"amit",
        "lastName":"bhure",
        "age":31,
        "rollNo":22,
        "skills":["python","javascript"]  ,
        "city":"jaipur"
    }


]

# print all user firstName ...
for x in students:
    print(x['firstName'])

# print firstName:numberofSkills
# chinmay:4

for x in students:
    print(x['firstName'])
    print(len(x['skills']))

# city - jaipur and skills - python
for x in students:
    if(x['city'] == "pune" and "python" in x['skills']):
        print(x["firstName"])


# add chat Gpt skills to all users 
for x in students:
    x["skills"].append("Chat Gpt")
print(students)

# add of people above
for x in students:
    if x['age'] > 30:
        print(x['firstName'])

# add language:"hindi" to all students 
for x in students:
    x['language'] =  "hindi"

# name of students with 'a'

for x in students:
    if x['firstName'].startswith("a"):
        print(x['firstName'])


total = 0

for x in students:
    total = total + x['age']
print(total/len(students))