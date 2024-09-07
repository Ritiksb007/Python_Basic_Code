#List is used to collect a number of entities in a single place
#List ids the ordered collection of data items
#They Stores multiple items in a single variable
#List item are saperated by common and enclosed within square brackets[]
#List are changeable meaning we can alter them after creation
#In List indexing starts from "0"
#In Negative indexing

marks = [1,2,3,6,"Ritik",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
#Negative Indexing 
print(marks[-3])
print(marks[len(marks)-3])

#Possitive indexing
print(marks[5-3])
print(marks[2])

if 6 in marks:
    print("Yes")
else:
    print("No")

if "Ri" in "Ritik":
    print("Yes")

#Slicing Concept
print(marks)
print(marks[1:-1])
print(marks[1:4])
print(marks[1:6:2]) #This Jump index print(marks[initial:final:jump by value])

#List Comprehension 
#List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets and even in arrays and strings
#Syntax List=[Expression(item) for item in iterablenif Condition]
lst = [i for i in range(5)]
print(lst)
lst = [i*i for i in range(10)]
print(lst)
lst =[i*i for i in range(10) if i%2==0]
print(lst)

#Eg.
#Accepts items with the small letter "o" in the list
names = ['Ritik','Ankush','Sohai','Ketan']
namesWith_o=[item for item in names if "o" in item]
print(namesWith_o)