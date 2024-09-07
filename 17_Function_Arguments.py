#There are 4 types of arguments that we can provide a function:
#Default Arguments: We can provide a default value to a function. The function will ignore a default value if the values are externally provided to a function for call
def average(a=1,b=3):
    print("Average Value: ",(a+b)/2)
average() # This will take the default values
average(a=2,b=3) #This will accept the value inside the argument and ignores the default values
#Keyword Arguments: We can provide the argument with key-value, this will help the interpreter to recogenise the arguments by the paramenter name. Therefore the order in which  the arguments are passes does not matter
def average(a=12,b=11):
    print("The average value: ",(a+b)/2)

average(b=2)
average(b=22,a=5)
#Variable Length Arguments: 
def average(*numbers):   #* is used to define as Tuple
    print(type(numbers))
    sum=0
    for i in numbers:
        sum =sum+i
    print("Average: ",sum/len(numbers))

average(2,4,5,6,7)

def name(**name):       #** is used to define as Dictionary
    print(type(name))
    print("Hello: ",name["fname"], name["mname"],name["lname"])

name(mname="Radheshyam",lname="Malviya",fname="Ritik")

average(2,4,5,6,7)
#Required Arguments: In case we does not pass the arguments with a key = value syntax, then it is necessary to pass the argumantes in the correct possitional order and the number of argument =s passed shound matchwith the actual fuction defination.

def average(a,b,c=12):
    return (a+b+c)/3

c=average(23,6)