# convert list to nested dictionary of keys

mylist = [1, 2, 3, 4]
dict1 = newdict={}


for i in mylist:
    newdict[i] = {}
    newdict = newdict[i]
    
print(dict1)