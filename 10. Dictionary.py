# Dictionary:
# Dictionary is a in-built collection datatype, which is used to store multiple values in a single varaible.
# Dictionary stores the data in the form of key-values pairs.
# Each key is unique and works as an index to access its corresponding value.
# Keys are immutable(can't be changed once created), while values can be anything(mutable).
# Dictionary are: Ordered(From python 3.7+ version), Mutable, Do not allows the duplicate keys
# Syntax
# my_dict = {
#     "key1":"value1",
#     "key2":"value2",
#     "key3":"value3",
#     "key4":"value4"
# }
# print(my_dict)
# Characteristics of Dictionary:
# key-value pairs: 
# Every entry of Dictionary's element is a pair: keys and values. 
# { "name":"kkahmed"}
# Unique Keys: 
# example: 
# A = {"n":"kkahmed","n":"Anurag"}
# print(A) # {"n":"Anurag"}
# Keys must be immutable: 
# keys can be(valid keys): integer,float,string
# My_dict = {
#     1:"value1",
#     10.2:"value2",
#     "key3":"value3",
#     "key4":"value4"
# }

# Creating Dictionary:
# Normal Dictionary:
# BioData = {
#     "Name":"kkahmed",
#     "RollNo":32,
#     "Branch":"CSE-CS",
#     "Place":"siddipet"
# }
# print(BioData)
# Dictionary using Constructor: 
# BioData1 = dict( Name="kkahmed",Roll_No=32,Branch="CSE-CS")
# print(BioData1)
# Empty Dictionary:
# E_D = {}

# Accessing the Dictionary:
# -> To access an element we use key names inside the square brackets [] or we can use get() method.

# BioData = {
#     "Name":"KKAHMED",
#     "RollNo":32,
#     "Branch":"CSE-CS",
#     "Place":"SIDDIPET"
# } 
# square brackets []
# print(BioData["Name"]) # KKAHMED
# print(BioData["RollNo"]) # 32
# print(BioData["Branch"]) # CSE-CS
# print(BioData["Place"]) # SIDDIPET
# # using get() method:
# print(BioData.get("Name")) # KKAHMED
# print(BioData.get("RollNo")) # 32
# print(BioData.get("Branch")) # CSE-CS
# print(BioData.get("Place")) # SIDDIPET

# Adding and Updating Dictionary:
# Adding: You can insert a new key-value pari into a dictionary.
# Updating: You can update or change the values using exsisted keys in the dictionary. 
# BioData = {
#     "Name":"KKAHMED",
#     "RollNo":32,
#     "Branch":"CSE-CS",
#     "Place":"SIDDIPET"
# } 
# update:
# BioData["RollNo"] = 32
# BioData["Name"] = "KKAHMED"
# print(BioData)
# # add: 
# BioData["Role"] = "ETHICAL HACKER"
# print(BioData)

# Removing in Dictionary:
# Python gives mutliple ways to delete items from a dictionary. 
# pop(),popitem(),clear(), del(delete)

# BioData = {
#     "Name":"KKAHMED",
#     "RollNo":32,
#     "Blood grp":"A+",
#     "Branch":"CSE-CS",
#     "Place":"SIDDIPET",
#     "Role":"EH"
# }
# print(BioData)
# # pop() : Removes the key value
# BioData.pop("Blood grp")
# print(BioData)
# # popitem(): Removes the Last inserted item from the dictionary.
# BioData.popitem()
# print(BioData)
# BioData.popitem()
# print(BioData)
# BioData.popitem()
# print(BioData)
# BioData.popitem()
# print(BioData)
# BioData.popitem()
# print(BioData)
# # del(delete): Deletes the keys from dictionary. 
# del BioData["Place"]
# print(BioData)
# # clear(): Removes every item from the dictionary. 
# BioData.clear()
# print(BioData)

# Dictionary methods:
# Methods allow you to access dictionary data easily. 
# keys(),values(), items()
# BioData = {
#     "Name":"KKAHMED",
#     "RollNo":32,
#     "Blood grp":"A+",
#     "Branch":"CSE-CS",
#     "Place":"SIDDIPET",
#     "Role":"EH"
# }
# # keys(): It prints only the keys of dictionary
# print(BioData.keys()) #  n,r,blg,brn,plc,rol
# # values(): It prints only the values of dictionary
# print(BioData.values()) # nan,b+,csc,hy,sde
# # items(): It prints both the keys and values of dictionary
# print(BioData.items())
# # update: Manually we are assigning the values with seperate lines 
# BioData["RollNo"] = 16
# BioData["Name"] = "Nikhil"
# print(BioData)
# # updating update(): update the mutliple values (this is in built method to update mutliple keys )
# BioData.update({"Role":"Web Developer","Place":"Kamareddy"})
# print(BioData)

# Loops for Dictionary:
# We can loop over keys,values,items(both).
# CR = {
#     "Name":"KKAHME",
#     "RollNo":32,
#     "Blood grp":"A+",
#     "Branch":"CSE-CS",
#     "Place":"SIDDIPET",
#     "Role":"EH"
# }
# Loop through keys 
# by-default the loop iterate the keys from the dictionary.
# for i in CR:
#     print(i) # name,roll,bldgrp,braN,plc,role
# The loop iterates the mentioned methods elements. 
# for i in CR.keys():
#     print(i) # name,roll,bldgrp,braN,plc,role
# for i in CR.values():
#     print(i) 
# for i in CR.items():
#     print(i)

#  Nested  Dictionary:

students = {
    "CR":{"Name":"KKAHMED","RollNo":32},
    "GR":{"Name":"KKAHMED","RollNo":32} }
print(students["CR"]["Name"])

