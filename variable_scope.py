x=10

def func1():
    x=20
    print(x)


func1()
print(x)


def func2():
    global x
    print(x)


func2()