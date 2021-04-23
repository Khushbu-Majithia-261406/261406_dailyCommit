#finding second maximum no. from list

mylist=[3,5,1,7,2]


maximum=mylist[0]
secondmax=mylist[0]


def findsecondmax(mylist,maximum,secondmax):
    for i in range(0,len(mylist)):
        if(mylist[i]>=maximum):
            secondmax=maximum
            maximum=mylist[i]

        if(mylist[i]<maximum and mylist[i]>secondmax):
            secondmax=mylist[i]


    print(secondmax)

findsecondmax(mylist,maximum,secondmax)
