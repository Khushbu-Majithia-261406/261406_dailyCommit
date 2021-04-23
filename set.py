def gettype(s):
    print(type(s))

def addelement(s):
    s.add(20)
    print(s)

def addmultipleelements(s):
    s.update([100,200,300])
    print(s)

	
	max and min value in set
	
	merge 2 dictio
	
	conv list to nested diction of keys
	
	find repeeated items of tuple
	
	convert list of tuples to dictionary
	
	
def remove(s):
    s.discard(200)
    s.remove(100)
    print(s)

def removelastelement(s):
    s.pop()
    print(s)


def clearset(s):
    s.clear()
    print(s)


def merge(s):
    s2=(45,55,65)
    print(s+s2)


def intersect(s):
    s2=(300,67,78)
    print(s-s2)


s=(1,2,3)

gettype(s)
addelement(s)
addmultipleelements(s)
remove(s)
removelastelement(s)
clearset(s)
merge(s)
intersect(s)