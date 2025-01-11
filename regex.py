import re
#REGULAR EXPRESSION

# ^ -- starts with
# $ -- ends with
# * -- 0 or more occurneces
# + -- 1 or more occurences
# ? -- 0 or 1 occurences
# {} -- exactly the specified number of occurences
# | -- either or
# . -- any character (except new line character) 


txt = "My name is sudhanva"
# check if the string starts with "My" and ends with "nva"
x = re.search("^My.+n*a$", txt)

if x:
    print("Yes we have a match")
else:
    print("No match")

#find all characters alphabetically between a-j
x1 = re.findall("[a-j]", txt)
print(x1)

# find all digit characters

text1 = "qweqkjds123"
x2 = re.findall("\d", text1)
print(x2)

# any character except new line character
txt2 = "hello planet"
x3 =  re.findall("he..o", txt2)
print(x3)

# check if the string starts with hello
txt3 = "hello planet"
x4 = re.findall("^hello", txt3)

if x4:
   print("Yes, the string starts with hello")
else:
    print("no match")

# check if the string starts with planet
txt4 = "hello planet"
x5 = re.findall("hello$", txt3)

if x5:
   print("Yes, the string starts with planet")
else:
    print("no match")