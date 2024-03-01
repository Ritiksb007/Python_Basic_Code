import time
timestamp= time.strftime("%H:%M:%S")
print(timestamp)

if (0<= int(timestamp[:2])<3):
    print("Its Bed Time!!")
elif(3<= int(timestamp[:2])<12):
    print("Good Morning Sir!!")
elif (12<= int(timestamp[:2])<16):
    print("Good After-Noon Sir")
elif(16<= int(timestamp[:2])<21):
    print("Good Eveaning Sir")
elif(21<= int(timestamp[:2])<23):
    print("Good Night Sir")


#Code 2
timestamp= time.strftime("%H:%M:%S")
# hour = int(time.strftime('%H'))
hour = int(input("Enter Hour: "))
print(timestamp)
if(hour>=0 and hour<=3):
    print("Its Bed Time!!")
elif(hour>=4 and hour<=12):
    print("Good Morning Sir!!")
elif(hour>=12 and hour<=16):
    print("Good After-Noon Sir!!")
elif(hour>=17 and hour<=21):
    print("Good Eveaning Sir!!")
elif(hour>=22 and hour<=23):
    print("Good Night Sir!!!")

#Note: In indexing x:Y then while printing a string x to y-1 string will be printed in console or in terminal

# elif(timestamp < 16 and timestamp == 12):
#     print("Good After-Noon Sir")
# elif(timestamp < 21 and timestamp == 16):
#     print("Good Eveaning Sir")
# else:
#     print("Good Night Sir")

# timestamp= time.strftime("%H")
# print(timestamp)
# timestamp= time.strftime("%M")
# print(timestamp)
# timestamp= time.strftime("%S")
# print(timestamp)

