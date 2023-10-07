#set
set ={"str",12,True,"str","12"}
# print(len(set1))
# Access Set Items
# for x in set1:
#     print(x)
# print(3 in set1)
# Add Set Items
# by .add()
set1 = {"Python","Java","JavaScript","HTML/CSS","C++"}
set1.add("C")
# print(set1)
# by .update()
set2 = {"SQL","Ruby","PHP","Swift","Go"}
set1.update(set2)
# print(set1)
# Remove Set Items
set3 = {"w3 school","codecademy","coursera","edx"}
# by remove
# print(set3)
# set3.remove("edx")
# print(set3)
# by discard
# set3.discard("coursera")
# print(set3)
# by pop
# set3.pop()
#by clear
# set3.clear()
# print(set3)
# Loop Sets
# for x in set3:
#     print(x)
# Join Sets
#by union
set4 = {"str",12,3,True,False,12.8}
set5 = {"str","int","float","bool",1,1.2,True,False}
# print(set4.union(set5))
# by update
set5.update(set4)
print(set5)