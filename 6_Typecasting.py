# Typecasting: Convertion of one data type into another data type.
# Note: Python Support a wide varity of functions or methods like: int(), float(), str(), ord(), hex(), oct(), dict(),etc,. for the type casting in python.
a= "1"
# a=1
b="3"
# c=3
print(int(a)+int(b))

#Types of TypeCasting 
#1. Implisite function: Which python does on its own by using python interpritor
#2. Explicite Function: Which we do saperately or manually.
#Eg. Explicite Function
string="15"
number=7
string_number= int(string)
sum= number + int(string_number)
print("The Sum: ", sum)

#Implisite function
a=7
print(type(a))
b=55.26
print(type(b))
print((a+b))