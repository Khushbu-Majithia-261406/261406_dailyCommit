a=input()
b=int(input())
c=float(input())

def display():
    print(a)
    print(b)
    print(c)

def func1():
    if(b>0):
        print("positive no")
    else:
        print("negative no")



def printsum():
    sum=0
    for i in range(0,10):
        sum+=i+1

    print("sum=",sum)



def factorial():
    fact=1
    num=5
    i=1
    while(i<=num):
        fact*=i
        i+=1

    print("factorial=",fact)


display()
func1()
printsum()
factorial()