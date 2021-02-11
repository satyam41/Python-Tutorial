# {}, mutable, keys:values, datatype.

myDict = {
    # keys:values
    "Anuj" : 4574448,
    "Shubh": 747444,
    "Satyam":4414444,
}

print(myDict)

print(myDict.keys())
print(myDict.values())

myDict["Shubh"] = 4777488
print(myDict)

# l = [1,2,3,4,5]
# l.append(6)

myDict["Ram"] = 445474474
print(myDict)

myDict.popitem()
print(myDict)

myDict.pop("Anuj")
print(myDict)

