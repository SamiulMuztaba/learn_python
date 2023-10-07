# #Tuples
# newtuple = (10,43,7,"num",False)
# print(type(newtuple))
# Negative Indexing(comment)
# print(newtuple[-1])
# Range of Indexes(comment)
# print(newtuple[0:4])
# Note: The search will start at index 2 (included) and end at index 5 (not included).
# # Update Tuples
# thistuple = ("software","design","testing")
# a = list(thistuple)
# a.append("making")
# b = tuple(a)
# print(b)
# #Unpack Tuples
# fruits = ("apple", "banana", "cherry","damn","error","fast","game")
# (a,*b) = fruits
# print(b)
# #Python - Loop Tuples
#by using a for loop
# for x in fruits:
#     print(x)
# range() and len()
# for y in range(len(fruits)):
#     print(fruits[y])
# Using a While Loop
# tuple = ("apple", "banana", "cherry","damn","error","fast","game")
# x = 0
# while x < len(tuple):
#     print(tuple[x])
#     x = x + 1
# #Python - Join Tuples
tuple1 = (1,2,3,4)
# print(tuple1 * 5)
# #Tuple Methods
#index
# tuple = ("apple", "banana", "cherry","damn","error","fast","game","fast")
# index = tuple.index("cherry")
# print(index)
# count
# count = tuple.count("fast")
# print(count)
# #Tuple Exercise
# Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])
# Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))
# Use negative indexing to print the last item in the tuple
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
fruit = ("apple", "banana", "cherry","orange","kiwi","melon","mango")
print(fruit[2:5])