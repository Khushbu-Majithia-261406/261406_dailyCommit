# to change the position of every n-th value with the (n+1)th in a lis


mylist=[1,2,3,4,5]

newlist=[]


def changepos(mylist):
    
    for i in range(0,len(mylist)):
        if(i==len(mylist)-1):
            newlist.append(mylist[0])

        else:
            newlist.append(mylist[i+1])


    print(newlist)

changepos(mylist)