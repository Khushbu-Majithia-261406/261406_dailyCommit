def getlength(dict1):
    print(len(dict1))

def converttostring(dict1):
    print(str(dict1))

def gettype(dict1):
    print(type(dict1))

def cleardictionary(dict1):
    dict1.clear()
    print(dict1)

def copydictionary(dict1):
    dict3=dict1.copy()
    print(dict3)

def getvalueatindex(dict1):
    print(dict1.get(1))

def getitems(dict1):
    print(dict1.items())

def getkeys(dict1):
    print(dict1.keys())

def updatedictionary(dict1,dict2):
    dict1.update(dict2)
    print(dict1)

def getvalues(dict1):
    print(dict1.values())



dict1={'1':"abc",'2':"def",'3':"ghi"}

dict2={'1':"abc",'4':"mno",'5':"pqr"}

getlength(dict1)
print()

converttostring(dict1)
print()

gettype(dict1)
print()

copydictionary(dict1)
print()

getvalueatindex(dict1)
print()

getitems(dict1)
print()

getkeys(dict1)
print()

updatedictionary(dict1,dict2)
print()

getvalues(dict1)
print()