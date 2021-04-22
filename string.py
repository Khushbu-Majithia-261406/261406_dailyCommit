def checktype(mystring):
    print(type(mystring))
    
def character(mystring):
    for i in range(0,len(mystring)):
        print(mystring[i])

def stringrange(mystring):
    # Start Oth index to end  
    print(mystring[0:])  
    # Starts 1th index to 4th index  
    print(mystring[1:5])  
    # Starts 2nd index to 3rd index  
    print(mystring[2:4])  
    # Starts 0th to 2nd index  
    print(mystring[:3])  
    #Starts 4th to 6th index  
    print(mystring[4:7]) 
    print(mystring[-1])  
    print(mystring[-3])  
    print(mystring[-2:])  
    print(mystring[-4:-1])  
    print(mystring[-7:-2])  
    # Reversing the given string  
    print(mystring[::-1])  
    print(mystring[-12])




def string_concat(mystring):
    mystring2="how are you?"
    print(mystring+mystring2)


def escape_sequence(mystring):
    str =mystring, "Hello what's going on?"  
    print(str)  


def capital(mystring):
    print(mystring.capitalize)


def countvalue(mystring):
    x=mystring.count("name")
    print(x)


def find_value(mystring):
    x=mystring.find("name")
    print(x)


def get_index(mystring):
    x=mystring.index("name")
    print(x)


def typeofchars(mystring):
    print(mystring.isalnum())
    print(mystring.isalpha())
    print(mystring.isdigit())


def changecase(mystring):
    print(mystring.lower())
    print(mystring.upper())



def fillstring(mystring):
    x=mystring.zfill(30)
    print(x)



mystring=input()

checktype(mystring)
print()

character(mystring)
print()

stringrange(mystring)
print()

string_concat(mystring)
print()

escape_sequence(mystring)
print()

capital(mystring)
print()

countvalue(mystring)
print()

find_value(mystring)
print()

get_index(mystring)
print()

typeofchars(mystring)
print()

changecase(mystring)
print()

fillstring(mystring)
