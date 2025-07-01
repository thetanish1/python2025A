
# info = [
#     {
#         "firstName":"chinmay",
#         "lastName":"deshpande",
#         "age":35,
#         "city":"pune",
#         "skills":["python","js"]
#     },

#     {
#         "firstName":"amol",
#         "lastName":"rao",
#         "age":34,
#         "city":"mumbai",
#         "skills":["python","js","sql","excel"]
#     },
#     {
#         "firstName":"sarika",
#         "lastName":"pansare",
#         "age":26,
#         "city":"pune",
#         "skills":["python","js","cypress","sql","selenium"]

#     }
#     ,
#     {
#         "firstName":"poorva",
#         "lastName":"vyas",
#         "age":25,
#         "city":"nagpur",
#         "skills":["python","django","sql"]

#     }


# ]

# # print firstName of all users .
# for x in info:
#     print(x['firstName'])

# # firstName:skills
# for x in info:
#     print(f'firstName:{x['firstName']}:{len(x['skills'])}')

# # number of user with sql skills 
# for x in info:
#     if "sql" in x["skills"]:
#         print(x['firstName'])

# # name of user above 30 years of age 
# for x in info:
#     if x['age'] > 30:
#         print(x['firstName'])

# # name of user with a city pune and age above 25
# print("--------------------------")
# for x in info:
#     if x['age'] > 25 and x['city'] == "pune":
#         print(x['firstName'])

# # name of user with skill python and city pune 
# for x in info:
#     if "python" in x['skills'] and x['city'] == "pune":
#         print(x['firstName'])

# # average age of all students 
# total = 0 
# for x in info:
#     #print(x['age'])
#     total = total + x['age']

# print(total/len(info))