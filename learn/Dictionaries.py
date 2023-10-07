# dict = {
#     "SamiulMuztaba":{
#         "Email": "samiulmuztaba@gmail.com",
#         "Birth Date": "9/23/2010",
#         "First name": "Samiul",
#         "Last name": "Muztaba",
#         "Nickname": "Arko",
#         "Type of work": "student",
#         "programming experience time": "2 month"
#     },
#     "Python":{
#         "Paradigm":	"Multi-paradigm: object-oriented,procedural (imperative), functional, structured, reflective",
#         "Designed by": "Guido van Rossum",
#         "Developer": "Python Software Foundation",
#         "First appeared": "20 February 1991; 32 years ago",
#         "Stable release": "3.11.3",
#         "Preview release": "3.12.0a7",
#         "Typing discipline": "Duck, dynamic, strong typing;gradual (since 3.5, but ignored in CPython)",
#         "OS" : "Windows, macOS, Linux/UNIX, Android and more",
#         "License": "Python Software Foundation License",
#         "Filename extensions" : ".py, .pyi, .pyc, .pyd, .pyw, .pyz (since 3.5),.pyo (prior to 3.5)",
#         "Website": "python.org",
#     },
#     "year": 1991
# }
# print(dict["SamiulMuztaba"]["Email"])
# Access Dictionary Items
# normal
# print(dict["year"])
# get()
# x = dict.get("Python")
# print(x)
# keys()
# y = dict.keys()
# print(y)
# values
# print(dict.values())
# Change Dictionary Items
# Change Values
# dict["year"] = 2010
# print(dict["year"])
# Add Dictionary Items
# Update Dictionary
# dict.update({"Python":"Python is a great language"})
# print(dict["Python"])
# Remove Dictionary Items
# pop()
# dict.pop("Python")
# print(dict)
# popitem()
# dict.popitem()
# print(dict)
# del
# del dict["SamiulMuztaba"]
# print(dict)
# clear()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1962
}
# thisdict.clear()
# print(thisdict)
# Loop Dictionaries
dict1 = {
    "thisdict1":{
        "brand": "Ford",
        "model": "Mustang",
        "year": 1962
    },
    "thisdict2":{
        "brand": "python",
        "model": "best",
        "year": 2010
    }
}
dict2 = {
    "lang": "java",
    "population":"33%",
    "launched":"1995"
}
# for loop
# for c in dict2:
# print(c)
# values() method to return values of a dictionary
# for a in dict2.values():
# print(a)
# keys() method to return the keys of a dictionary
# for z in dict2.keys():
    # print(z)
# Loop through both keys and values, by using the items() method:
# for z,y in dict2.items():
#     print(z,y)
#Copy Dictionaries
print(dict2)
# copy()
copydict = dict2.copy()
# print(copydict)
#dict()
g = dict(dict2)
print(g)
# Add the key/value pair "color":"red" to the car dictionary