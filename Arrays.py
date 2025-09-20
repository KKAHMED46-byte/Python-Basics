#arrays in pyton:
#an array is collection of elements of the same datatype stored in a continuous memory location.
#arrays are used to store multiple values in a single variable.
#why arrays?
#easy to managemultiple values
#allows faster operations like searching,sorting
#arrays vs lists:
#arrays have less memory consumption compared to lists
#important the array module
import array as arr
#creating an array:
numbers=arr.array('i',[1,2,3,4,5])
print(numbers)
print(type(numbers))
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# print(numbers[4])
#iterating the array using for loop

#adding an element:
#append:
numbers.append(6)
print(numbers)

#insert:
numbers.insert(3,10)
print(numbers)

# #deleting an element:
# #remove:
# numbers.remove(10)
# print(numbers)

# #pop:
# numbers.pop(3)
# print(numbers)

# #updating an element:
# numbers[0]=20
# print(numbers)

# #clearing the array:
# numbers.clear()
# print(numbers)

# #looping through array:
# for i in numbers:
#     print(i)

import array as arr
#creating an array:
numbers=arr.array('i',[1,2,3,4,5])
numbers.clear()
print(numbers)