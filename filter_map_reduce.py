# filter within map

c = map(lambda x:x+x,filter(lambda x: (x>0), (-1,2,-3,4)))
print(list(c))


# map within filter

c = filter(lambda x: (x>0),map(lambda x:x+x, (-1,2,-3,4)))  #lambda x: (x>=3)
print(list(c))

# map and filter within reduce

d = reduce(lambda x,y: x+y,map(lambda x:x+x,filter(lambda x: (x>0), (-1,2,-3,4)))) 
print(d)