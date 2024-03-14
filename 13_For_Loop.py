#Loops Can iterate a sequence of iterable objects
name="Ritik_Malviya"
for i in name:
    print(i)
    if(i=="i"):
        print("good to go")

color=["Red","Green","Blue"]
for color in color:
    print(color)
    for i in color:
        print(color)

for k in range(22):
    print(k)
for k in range(5,100):
    if k%5==0:
        print(k)

for k in range(0,20,5):
    print(k)