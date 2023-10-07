import re

greet = "1 hello world"
a = "^1"
b = re.findall(a,greet)

print(b)

if b:
    print("it has 1 in sentence")

else:
    print("it has not 1 in sentence")

txt = "hello planet"

#Check if the string ends with 'planet':

c = re.findall("planet$", txt)
if c:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")

#Find all digit characters:
d = re.findall("\d",greet)
print(d)

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

e = re.findall("....o", greet)
print(e)

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

f = re.findall("he.*o", txt)

print(f)

g = re.findall("he.+o", txt)

print(g)

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

h = re.findall("he.?o", txt)

print(h)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

i = re.findall("he.{2}o", txt)

print(i)

#Check if the string contains either "world" or "planet":

j = re.findall("world|planet", greet)
print(j)

if j:
  print("Yes, there is at least one match!")
else:
  print("No match")