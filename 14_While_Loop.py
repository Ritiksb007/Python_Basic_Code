# Loop continues till condition is true
i=int(input("Enter The Number: "))
while(i<=15 & i>=20):
    print(i)
print("Done With Printing.")
#Above code is not correct

count = 5
while(count>0):
    print(count)
    count=count-1
else:
    print("All is well")

#While loop first time executes irrespective of the condition
#In Python do while is not used only while loop is used
# Question For Interview 
    #Does Emulata do while loop in python
#Solution
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break