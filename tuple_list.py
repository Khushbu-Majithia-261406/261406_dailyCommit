#list

def list_functions(mylist):
    print("LIST FUNCTIONS")
    print(mylist)
    print(len(mylist))
    mylist.append(5)
    print(mylist)
    print(type(mylist))
    print(min(mylist))
    print(max(mylist))
    c=mylist.count(200)
    print(c)
    i=mylist.index(200)
    print(i)
    mylist.insert(1,10)
    print(mylist)
    mylist.pop()
    print(mylist)
    mylist.remove(10)
    print(mylist)
    mylist.reverse()
    print(mylist)
    mylist.sort()
    print(mylist)
    print()

def tuple_functions(mytuple):
    print("TUPLE FUNCTIONS")
    print(len(mytuple))
    print(max(mytuple))
    print(min(mytuple))


mylist=[200,300,100]
list_functions(mylist)


mytuple=(200,300,100)
tuple_functions(mytuple)