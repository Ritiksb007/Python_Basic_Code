# If Else Statements
a = int(input("Enetr Your Age: "))
print("Your Age is ",a)
#Conditional operators:
# >, <, >=, <=, ==, !=
print(a>18)
print(a<18)
print(a>=18)
print(a>=18)
print(a!=18)

if(a>=18):
    print("You Can Drive!!")
else:
    print("You Are not elegible to drive!!")
print("Hello")

#If & Elif Statement
num = int(input("Enter The Number: "))
if(num<0):
    print("Number is Negative.")
elif(num>0):
    print("Number is Positive.")
elif(num==0):
    print("Number is Equal to Zero")
else:
    print("Everything is all right")

#Nested If Statement
num1 = 10
if(num1<0):
    print("Number is Negative")
elif(num1> 0):
    if(num<=10):
        print("Number is Negative.")
    elif(num>10):
        print("Number is Positive.")
    else:
        print("Number is Greater Than 20")
else:
        print("Everything is all right")