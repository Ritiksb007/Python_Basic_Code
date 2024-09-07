#List Methods
l = [11,2,3,1,5,7,3,1]
print(l)
# 1) Append: Add element at the end of the list
l.append(45)
print(l)
# 2) Sort : Arrange the elements in assending order by default and if reverse= true is passed then it sorts elements in descending order
l.sort()
print(l)
l.sort(reverse=True)
print(l)
# 3) Count : Counts the recurrance of a particular element in a list
print(l.count(1))
# 4) Copy : It Returns the copy of the list
m=l.copy()
m[2]=55
print(l)
print(m)
# 5) insert and Index: Helps to insert given item/element at gien index
l.insert(6,65) # Here 6 is the index position and 65 is the item value
print(l)  
# 6) extends : It Adds an entire list or any other collection datatype like set, tuple, dictionary to the existing list
n= [45,78,2,3]
l.extend(n)
print(l) #List l is updated
print(n) #List n does not get affected
# 7) Concatinating two lists: Joins two lists
k=l+m
print(k)