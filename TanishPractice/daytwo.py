# elasticsearch = [
#     {
#         "_id": 1,
#         "name": "Elasticsearch Beginner's Guide",
#         "price": 29.99,
#         "category": "Books",
#     },
#     {"_id": 2, "name": "Learning Elasticsearch", "price": 39.99, "category": "Books"},
#     {"_id": 3, "name": "Mastering Elasticsearch", "price": 49.99, "category": "Books"},
#     {"_id": 4, "name": "Elasticsearch in Action", "price": 34.99, "category": "Books"},
#     {
#         "_id": 5,
#         "name": "Advanced Elasticsearch Techniques",
#         "price": 44.99,
#         "category": "Books",
#     },
#     {
#         "_id": 6,
#         "name": "The Definitive Guide to Elasticsearch",
#         "price": 59.99,
#         "category": "Books",
#     },
#     {
#         "_id": 7,
#         "name": "The Ddyetyerticsearch",
#         "price": 30.99,
#         "category": "Bootruks",
#     },
# ]

# for x in elasticsearch:
#     print(x['_id'])

# for x in elasticsearch:
#     print(f'name:{x['name']}:{x['price']}')

# for x in elasticsearch:
#     if 'Elasticsearch' in x['name']:
#         print(x['_id'])

# for x in elasticsearch:
#     if x['price'] >40:
#         print(x['name'])

# for x in elasticsearch:
#     if x['price'] >29 and x["price"] < 49.99:
#         print(x['name'],x['price'])


vehicles = {
    "property": "sunroof",
    "color": "red", 
    "type": "SUV",
    "companyname": "Toyota"
    }
    

# print(vehicles)
print(len(vehicles))

for x in vehicles.keys():
    print(x)

for x in vehicles.values():
    print(x)

for x in vehicles.items():
    print(x)

