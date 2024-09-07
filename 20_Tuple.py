#Tupple is imutable and it is similar to List
#Tuples are ordered collection of data items. They store multiple items in a single variable.Tuple items are separated by commas and enclosed with round brackets 0. Tuples are unchangeable meaning we can not alter them after creation.
#Tuple dows not allow object assignment.
#Tuple is mostly used when the user does not want that no one else change the item list then tuple is used.
#Note: If we want to create a Tuple with single item them we need to give comma to show we are creating tuple.
 
tup = (1,)
print(type(tup),tup)

print(len(tup))

tup1 =(1,2,3,342,"Blue",True)

print(type(tup1),tup1)

print(tup1[2])
print(tup1[:4])

#If Condition
if 342 in tup1:
    print("Yes 342 is present in the Tuple")

#Slicing
tup2 = tup1[1:4]
print(tup2)