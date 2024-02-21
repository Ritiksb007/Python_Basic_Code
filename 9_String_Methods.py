name = "Ritik Malviya"
print(len(name))
#slicing  of character
print(name[0:5]) #Including 0 But not 5
print(name[:5]) #Including 0 But not 5
print(name[1:4]) #Including 1 But not 4
print(name[0:len(name)-3]) #Including 0 But len(name)=13-3=10

#Quick Quiz:
name1="Harry"
print(name1[-4:-2]) #counts from end and moves left right

#String Methods
#Note Strings are immutibal
a="!!Harry!!!!!!!!!!"
print(len(a))
print(a.lower())
print(a.upper())
print(a.rsplit("!")) #Strips Trailing characters 
#Gives output as "'', '', 'Harry', '', '', '', '', '', '', '', '', '', ''"
print(a.replace('Harry',"Ritik"))
print(a.split(" "))

blog="how are you doing"
print(blog.capitalize())

str1="Wellcome to India !!!"
print(len(str1))
print(str1.endswith("!!!"))
print(str1.endswith("to",4 ,10))

print(str1.find("lcome"))
print(str1.index("lcome"))
print(str1.islower())
print(str1.istitle())
print(str1.isupper())
print(str1.swapcase())
print(str1.title())