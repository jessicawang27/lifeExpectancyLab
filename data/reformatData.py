import json


f1 = open("life_expectancy_cleansed.csv", "r")
lines = f1.readlines()

dictionary ={}

# print(lines)
nested_dict = {}
for i in range(len(lines)):
    line = lines[i].replace("\n","").replace("\ufeff","").split(",")
    
    if line[0] == 'Country Name':
        dictionary['years'] = line[1:]
    
    else:
        nested_dict[line[0]] = line[1:]
        dictionary['countries'] = nested_dict

f1.close()


#Save the json object to a file
f2 = open("life_expectancy.json", "w")
json.dump(dictionary, f2, indent = 4)


f2.close()



