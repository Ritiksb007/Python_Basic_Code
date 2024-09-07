#Function is very usefull for using repatative code or a repeatative block of code
#Function is a block of code that performs a specific block of code whenever it is called.

#Note: It can be used to reduce number of lines of code.

#Built In function are: min(),max(),len(),sum(),type(),range(),dict(),list(),tuple(),set(),print(),etc,etc.

#Syntax: def FunctionName(variables):
        #   parameter and arguments along with rules to run the function and proper indentation must be given.

#Function can be defined as:
# def calculateGmean(a,b):
#     mean = (a*b) / (a+b)
#     print(mean)
# a=12
# b=2
# calculateGmean(a,b)

# c=21
# d=21
# calculateGmean(c,d)

print("Read Comments for info.")
def calculateGmean(a,b):
    mean = (a*b) / (a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First Number is Greater.")
    else:
        print("Second Number is Greater.")

def isLesser(a,b):
    pass


a=12
b=2
isGreater(a,b)
calculateGmean(a,b)

c=21
d=20
isGreater(c,d)
calculateGmean(c,d)