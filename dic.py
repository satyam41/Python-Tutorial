# dict is mutable means it is changeable.

# dict is made with the help of keys and values pair.

myDict = {
    # keys : values
    "Satyam" : 7857555,
    "Krishna" : 7474441,
    "Anuj" : 445441,
}

print(myDict)
# [1,2,3,4,5]
print(myDict["Krishna"])

print(myDict.keys())
print(myDict.values())

myDict.pop("Krishna")
print(myDict)

myDict["Anuj"] = 14141112
print(myDict)

myDict["Ram"] = 45466658
print(myDict)
