# #list
# li = [1,2,3]
# print(li)
# li[1] = 10
# print(li)
# lis = ["Samiul","Muztaba","Arko"]
# print(lis)
# list = ["True","False","True","False"]
# print(type(list))
# #Access List Items
# langlist = ["Python","Java","JavaScript","HTML/CSS"," C++"," SQL","Ruby","PHP","Swift","Go","bhjb"]
# langlist[10] = "C"
# print(langlist[10])
# #Change List Items
# langlist[8] = "C#"
# print(langlist)
# #Add List Items
# #Append
# langlist.append("swift")#int too
# print(langlist)
# #Insert
# langlist.insert(12,"etc")#index number,data(any type of data)
# print(langlist)
# # Remove List Items
# #by remove
# newlist = ["Samiul","Muztaba","Arko","soft","Programmer",25]
# newlist.remove("Programmer")#not a comment!!!
# print(newlist)
# #by pop
# newlist.pop(2)
# print(newlist)
# #by del
# del newlist[3]
# print(newlist)
# #by clear
# print(newlist)
# newlist.clear()
# print(newlist)
# #Loop List Item
# #by for
# looplist = ["clay","color","thermocol ball","anticutter","glue"]
# for schoolproject in looplist:
#     print(schoolproject)
# #by range and len
# for cell in range(len(looplist)):
#     print(cell)
# #by while
# looplist = ["clay","color","thermocol ball","anticutter","glue","cell","will","be","made","by"]
# y = 0
# while y < 10:
#     print(looplist[y])
#     y = y + 1
# #List Comprehension
# num = [1, 2, 3, 4, 5]
# for i in num:
#     print(i * 2)
# Double = [i * 2 for i in num]#any calculation
# print(Double)
# #Sort Lists
# #by sort
# number = [8,85,26,45,86,46,65,66,25]
# eng = ["b","p","v","s","f","r","o","w"]
# number.sort()
# eng.sort()
# print(number)
# print(eng)
# #by reverse
# num = [1,3,2,4,6,5,7,9,0,8]
# num.sort(reverse= True)
# print(num)
# #Copy Lists
# #by copy
# number = [1,2,3,4,5,6,7,8,9]
# num2 = number.copy()
# print(number)
# print(num2)
# Join Lists
# by + operator
num1 = [1,2,3]
num2 = [4,5,6]
# num3 = num1 + num2
# print(num3)
#by extend()
num1.extend(num2)
print(num1)#not only int but also str too
#List Methods
# append() 	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
a = ["apple","cherry",10,20,True,False]
a.append(30)
print(a)
# a.clear()
print(a)
b = a.copy()
print(b)
c = ["extend",20,True]
c.extend(a)
print(c)
c.index("apple")
print(c)
a.insert(1,"banana")
print(a)
c.pop(1)
print(c)
c.remove("extend")
print(c)
d = [1,2,3]
d.sort(reverse=True)
print(d)
e = ["a","d","r","b","y","i"]
e.sort()
print(e)
