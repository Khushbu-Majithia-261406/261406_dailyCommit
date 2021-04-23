# find repeated items of a tuple

mytuple=(10,20,10,45,10,34,20,67)
repeated=[]

print("repeated elements= ")


for i in mytuple:
    if mytuple.count(i) > 1:
       if(i not in repeated):
           repeated.append(i)


print(repeated)