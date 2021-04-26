# filter

def func(x):
    if(x>0):
        return x

y = filter(func, (-1,2,-3,4))  
print(y)
print(list(y))



# using lambda within filter

y = filter(lambda x: (x>0), (-1,2,-3,4))
print(list(y))