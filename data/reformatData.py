import json


f1 = open("life_expectancy_cleansed.csv", "r")
lines = f1.readlines()

dictionary ={

    "countries":{
        "mexico":[],
        "canada":[],
        "us":[]
    },
    "years":[]

}

# Create the dictionary here

f1.close()

#Save the json object to a file
f2 = open("life_expectancy.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()
