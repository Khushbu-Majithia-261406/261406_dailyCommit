# map

def func1(a):
    return a*a

x = map(func1, (1,2,3,4))  # x is the map object
print(x)
print(set(x))


# map with lambda

tuple1= (5,10,15,20,25,30)
tuple2 = tuple(map(lambda x: x+3 , tuple1)) 
print(tuple2)