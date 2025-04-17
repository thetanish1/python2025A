info = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande"
    },

    {
        "firstName":"amol",
        "lastName":"rao"
    },
    {   
        "firstName":"amit",
        "lastName":"bhure"
    }

]

for item in info:
    print(item.get('firstName')+" "+item.get('lastName'))
    item['city'] = "pune"

print(info)