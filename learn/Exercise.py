# #list
# # Print the second item in the fruits list.
# fruits = ["apple", "banana", "cherry"]
# print(fruits[1])
# Change the value from "apple" to "kiwi", in the fruits list.
# fruits = ["apple", "banana", "cherry"]
# fruits[0] = "kiwi"
# print(fruits)
# Use the append method to add "orange" to the fruits list.
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# print(fruits)
# #tuple
# Use the correct syntax to print the first item in the fruits tuple.
# fruits = ("apple", "banana", "cherry")
# print(fruits[0])
# Use the correct syntax to print the number of items in the fruits tuple.
# fruits = ("apple", "banana", "cherry")
# print(len(fruits))
# Use negative indexing to print the last item in the tuple
# fruits = ("apple", "banana", "cherry")
# print(fruits[-1])
# fruit = ("apple", "banana", "cherry","orange","kiwi","melon","mango")
# print(fruit[2:5])
# #Sets
# Check if "apple" is present in the fruits set.
# fruits = {"apple", "banana", "cherry"}
# if "apple" in fruits:
  # print("Yes, apple is a fruit!")
# Use the add method to add "orange" to the fruits set.
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)
# Use the correct method to add multiple items (more_fruits) to the fruits set.
# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits)
# print(fruits)
# Use the remove method to remove "banana" from the fruits set.
# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)
# Use the discard method to remove "banana" from the fruits set.
# fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")
# print(fruits)
# dictionary
# Use the get method to print the value of the "model" key of the car dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(car.get("model"))
# Change the "year" value from 1964 to 2020
car["year"] = 2020
# print(car)
# Add the key/value pair "color":"red" to the car dictionary
car["color"] = "red"
# print(car)
# Use the pop method to remove "model" from the car dictionary.
car.pop("model")
print(car)
# Use the clear method to empty the car dictionary.
car.clear()
print(car)