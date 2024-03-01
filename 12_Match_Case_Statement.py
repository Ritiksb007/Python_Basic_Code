# Mach Case is just a Switch Case Statement

x=int(input("Enter Your Input Value: ")) 
# Here x is the variable to match
match x:
    case 0: #If x = 0
        print("x is Zero")
    case 1:
        print("Case is 1")
    case 4:
        print("Case is 4")
    case _ if(x!=90):
        print(x,"is not 90")
    case _ if(x!=99):
        print(x,"is not 99")
    case _:
        print("Case is ",x)
