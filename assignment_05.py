# ask a user how many pizza slices they want.
# The pizzeria charges Rs 123.00 a slice.
# if user order even number of slices, price per slice is Rs 120.00. 
# Print the total price depending on how many slices user orders


costodd=123.00

costeven=120.00



def calculatecost(slices):
    price=0

    if(slices%2==0):
        price=price+(costeven*slices)


    else:
        price=price+(costodd*slices)


    print("total price= ",price)



slices=int(input("how many slices you want? "))


calculatecost(slices)