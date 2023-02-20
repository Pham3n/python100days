#Nesting Dictionaries

# travellog = {
#     "South Africa" : {
#         "cities" : ["Cape Town", "Durban", "Johannersburg"],
#         "totalvisits" : 23
#         },
#     "Kenya" : {
#         "cities" : ["Nairobi"],
#         "totalvisits" : 1
#         }
# }

travellog = [
        {"country" : "South Africa",
        "cities" : ["Cape Town", "Durban", "Johannersburg"],
        "totalvisits" : 23
        },
        {"country" : "Kenya" ,
        "cities" : ["Nairobi"],
        "totalvisits" : 1
        }
    ]
def travel(travellog, country, totalvisits, cities):
    
    travellog += [{"country" : country, "cities" : cities, "totalvisits" : totalvisits }]
    i = 0

    while i < len(travellog) :
        print(travellog[i])
        i += 1
    print(" ")

travel(travellog, "Russia", 2, ["Moscow", "Saint Petersburg"])

travel(travellog, "Brazil", 1, ["Rio de Janero"])

print(travellog)


