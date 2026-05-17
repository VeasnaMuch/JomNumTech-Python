students = {
                "name": "Veasna",
                "score": 90,
                "gender": "male",
                "field": "IT",
                "level": 11
}

print(type(students))
print(students["name"])
print(students)

nobject = dict({
    "name": "nemo"
})

print(nobject)
nobject["major"] = "mathematic"
print(nobject)

for key, value in nobject.items():
    print(key, value)

newDict = dict({})
newDict["index"] = "2004"
newDict["Name"] = ("2", "4", "6") #tuple
newDict["Subject"] = {"math", "physic", "chimi"} #set
print(newDict)