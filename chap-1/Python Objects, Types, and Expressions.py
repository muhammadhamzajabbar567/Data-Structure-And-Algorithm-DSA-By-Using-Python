# Variables and expressions
a = [1,2,4,5,7,9]
b = a
a.append(10)
print(b)

a = 1
b = 1.0
c = 'abc'
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Variable scope
a = 10
b= 20

def myfunction():
    global a
    a = 11
    b = 21
myfunction()
print(a)
print(b)

# Flow control and iteration
# By using If-elif-Else statements
x = 'one'
if x == 0:
    print('False')
if x == 1:
    print('True')
else:
    print("Something Else")

# By Using Loops

# by using whie
x = 0
while x < 3 :
    print(x)
    x += 1

# by using For Loop
x = 0
for x in range(0 ,3):
    print(x)
    x += 1

#strings and it's methods

# s.count(substring, [start,end])

# Define the string
s = "abracadabra"

# Define the substring to count occurrences of
substring = "abra"

# Specify the start and end indices for the search
start_index = 0  # Start searching from the beginning of the string
end_index = 6    # Search only within the first 6 characters of the string

# Count occurrences of the substring within the specified range
count_occurrences = s.count(substring, start_index, end_index)

# Print the count of occurrences
print("Occurrences of '{}' within the range ({}, {}): {}".format(substring, start_index, end_index, count_occurrences))

string = ' Pakistan'
substring = 'Pak'

start_index = 0
end_index = 6

count_occurrences = string.count(substring, start_index, end_index)
print("Occurrences of '{}' within the range ({}, {}): {}".format(substring, start_index, end_index, count_occurrences))


string = 'Pakistan'
substring = 'Pak'
string_lower = string.lower()  # Convert string to lowercase
substring_lower = substring.lower()  # Convert substring to lowercase

start_index = 0
end_index = 6

count_occurrences = string_lower.count(substring_lower, start_index, end_index)
print("Occurrences of '{}' within the range ({}, {}): {}".format(substring, start_index, end_index, count_occurrences))

# expandtabs()

s = 'Hello\tWorld\t!'

expanded_string_default = s.expandtabs()  #Default Size of expand tabs is 8
expanded_string_custom = s.expandtabs(4)

print(f"Original string: {s}")
print(f"Expanded String Default: {expanded_string_default}")
print(f"Expanded String Custom: {expanded_string_custom}")

# s.find(substring, [start, end])

s = 'Good Morning, Pakistan! Pakistan Zindabad'
substring = "Pakistan"
index = s.find(substring)
print(f"Index of the First occurrence of {substring} in {s} : {index}")


s = 'Good Morning, Pakistan! Pakistan Zindabad'
substring = "Pakistan"
# Define the start index for the search
start_index = 7  # Search from index 7 onwards

# Find the index of the first occurrence of the substring starting from start_index
index = s.find(substring, start_index)

# Print the index of the first occurrence of the substring
print("Index of the first occurrence of '{}' starting from index {}: {}".format(substring, start_index, index))

# s.isalnum()

# Define a string with alphanumeric characters
s1 = "Hello123"

# Define a string with non-alphanumeric characters
s2 = "Hello@123"

# Check if all characters in s1 are alphanumeric
result1 = s1.isalnum()

# Check if all characters in s2 are alphanumeric
result2 = s2.isalnum()

# Print the results
print("Is '{}' alphanumeric? {}".format(s1, result1))
print("Is '{}' alphanumeric? {}".format(s2, result2))

# s.isalpha()

# Define a string with alphabetic characters
s1 = "Hello"

# Define a string with non-alphabetic characters
s2 = "Hello123"

# Check if all characters in s1 are alphabetic
result1 = s1.isalpha()

# Check if all characters in s2 are alphabetic
result2 = s2.isalpha()

# Print the results
print("Is '{}' alphabetic? {}".format(s1, result1))
print("Is '{}' alphabetic? {}".format(s2, result2))

# s.isdigit()

# Define a string with numeric characters
s1 = "12345"

# Define a string with non-numeric characters
s2 = "123abc"

# Check if all characters in s1 are digits
result1 = s1.isdigit()

# Check if all characters in s2 are digits
result2 = s2.isdigit()

# Print the results
print("Is '{}' composed of digits? {}".format(s1, result1))
print("Is '{}' composed of digits? {}".format(s2, result2))

# s.join(t)

t = ['apple', 'orange', 'mango', 'cherry']
s = ', '
result = s.join(t)
print(result)

s = 'PakIstAN ZiNDaBaD'
print(s)
print(s.lower())
print(s.upper())

# s.replace(old, new [maxreplace])
# Define a string
s = "hello world, hello universe"

# Define the old substring to replace
old_substring = "hello"

# Define the new substring to replace with
new_substring = "hi"

# Replace all occurrences of the old substring with the new substring
result = s.replace(old_substring, new_substring)

# Print the result
print(result)


s = 'Hello, World!, Hello, Python'
old_substring = 'Hello'
new_substring = 'Hi'
result1 = f"Old String is: {s} "
result2 = f"New String is: {s.replace(old_substring, new_substring)}"
print(result1)
print(result2)

# s.strip([characters])

s1 = '      Hello, world          '
s2 = '******    Hello, world !!!!!!!'
result = s2.strip("*!")
print(f"Before Stripping (s1): {s1}")
print(f"After Stripping (s1): {s1.strip()}")
print(f"Before Stripping (s2): {s2}")
print(f"After Stripping (s2): {result}")

# s.split([separator], [maxsplit])
# Define a string
s = "apple,banana,orange"

# Use split() to split the string into a list of substrings using comma (,) as the separator
result = s.split(',')

# Print the result
print(result)


# Define a string
s = "apple,banana,orange,mango"

# Use split() to split the string into a list of substrings using comma (,) as the separator with a maximum of 2 splits
result = s.split(',', 2)

# Print the result
print(result)

greet = 'Hello World'  #string
print(greet[1])  #Indexing
print(greet[0:7]) #slicing
print(greet[0:8:2]) #stride
print(greet[0::2]) #stride

print(greet[1+2])
print(greet[len(greet)-1])
print(greet[10])

list = ['apple', 'banana', 'orange', 'mango']

#without enumerate
for i in range(len(list)):
    print(i,list[i])

#with enumerate
for i, fruit in enumerate(list):
    print(i,fruit)

for i in enumerate(greet[0:5]):
    print(i)

print(greet[0:5] + ' Wonderful ' + greet[5:])

x = '3'
y = '2'

print(x+y) #string
print(int(x) + int(y)) #integer

# list(s)
#
# # Create a string
# my_string = "hello"
#
# # Convert the string to a list of characters using list()
# Define the string
# my_string = "hello"
#
# # Convert the string to a list of characters
# char_list = list(my_string)
#
# # Print the resulting list
# print(char_list)


# s.append(x)
# Define an empty list
s = []

# Append elements to the list
s.append(1)
s.append(2)
s.append(3)

print(s)  # Output: [1, 2, 3]


s = []
for i in range(0, 20):
    s.append(i)
    print(s)

s = []
for i in range(0, 20):
    s.append(i)
print("\n",s)

s1 = [1,2,3,4,5,6,7,8,9]
s2 = [11,12,13,14,15,16,17,18,19]

s1.extend(s2)
print(s1)


s = [1,1,1,3,4,4,5,5,9]
print(s.count(1))
print(s.count(4))
print(s.count(5))

print(s.index(1))
print(s.index(4))
# print(s.index(1,3))

# s.insert(i,e)
# Define a list
s = [1, 2, 3, 4]

# Insert the element 5 at index 2
s.insert(2, 5)

print(s)  # Output: [1, 2, 5, 3, 4]

s = [1, 2, 5, 3, 4]
s.insert(-2,5)
print(s)

# s.pop(i)
s = [1, 2,3,4,5,6,7,8,9,10,11,12,13]
print(len(s)) # Output: []

s = [1, 1, 1, 3, 4, 4, 5, 5, 9]

try:
    index_of_0 = s.index(0, 3)
    print("Index of 0:", index_of_0)
except ValueError:
    print("Element 0 not found in the list.")


# s.pop(i)
s = [1, 1, 1, 3, 4, 4, 5]
s.pop(1)
print(s)
s.pop(4)
print(s)

# s.remove(x)
s = [1,1,4,6,7,7,0]
s.remove(4)
print(s)

# s.reverse()
s = [1,1,4,9,8,10,34]
s.reverse()
print(s)
print(s[::-1])

# List Comprehension
ls = [i for i in range(100) if i%3 == 0]
print(ls)

s = [1,2,3,4,5,6,7,8,9,10]
remove_number = 9
# By using List Comprehension we remove the 9 Number
ls = [i for i in s if i != remove_number]
print(ls)

# By using List Comprehension we add the 11 Number
s = [1,2,3,4,5,6,7,8,9,10]
add_number = 11

# ls = [i for i in s.append(add_number) in s]
# print(ls)

ls = [i for i in s] + [add_number]
print(ls)

# dict comprehension
dict1 = {i:f"item {i} " for i in range(10001)}
print(dict1)

dict2 = {i:f"item{i}" for i in range(1,101) if i % 2 == 0}
print("\n")
print(dict2)

# reverse dict
dict1 = {i:f"Item {i}" for i in range(1,11)}
print("\n",dict1)

dict2 = {value:key for key,value in dict1.items()} #reverse dictionary
print("\n",dict1,"\n",dict2)

# set comprehension
dresses = {dress for dress in {"dress1","dress1","dress2","dress1","dress2"}}
print("\n",dresses)
print(type(dresses))

# Generators Comprehensions
evens = (i for i in range(100) if i%2 ==0)
print("\n",evens)
print(type(evens))
print(evens.__next__())
print(evens.__next__())
for i in evens:
    print("\n",i)

# Task
# num_items = int(input("How many items do you want to enter? ")) # Prompting user for the number of items
# items = [input(f"Enter item {i+1}: ") for i in range(num_items)] # Getting input items using list comprehension
# range_input = int(input("Enter the range: ")) # Prompting user for the range
#
# # Ensuring the range_input is within the valid range for the loop
# if range_input > num_items:
#     range_input = num_items
#
# print("\nWhich kind of comprehension do you want to perform?")
# print("List Comprehension")
# print("Set Comprehension")
# print("Dict Comprehension")
# comprehension_type = input("Write the comprehension name you want to perform: ").strip() # Stripping whitespace from the user input
#
# # Performing the respective comprehension based on user input
# if comprehension_type == "List Comprehension":
#     result = [item for item in items[:range_input]] # List comprehension
# elif comprehension_type == "Set Comprehension":
#     result = {item for item in items[:range_input]} # Set comprehension
# elif comprehension_type == "Dict Comprehension":
#     result = {item: f"Item {item}" for item in items[:range_input]} # Dictionary comprehension
# else:
#     result = "Invalid comprehension type" # Handling invalid input
#
# print(result)

# s.sort(key ,[reverse])
ls = [3,234,12,11,1,3,7,9]
ls.sort()
print(ls)


# Define a list of tuples
s = [(2, 'b'), (1, 'a'), (3, 'c')]

# Sort the list based on the first element of each tuple in ascending order
s.sort(key=lambda x: x[0])

print(s)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Sort the list based on the second element of each tuple in descending order
s.sort(key=lambda x: x[1], reverse=True)

print(s)  # Output: [(3, 'c'), (2, 'b'), (1, 'a')]

x=1;y=2;z=3

list1 = [x,y,z]
list2 = list1
list2[1] = 4
print("\n",list1)

# nested lists or 2D lists
import numpy as np
lst = [["Rice",'2 KG', 500], ['Flour','1 KG',350],['Corn','1 KG',450]]
arr = np.array([[2,3,4,4],[1,4,5,7],[2,5,6,9]])
print(type(lst))
print(type(arr))

for item in lst:
    print(f"Product: %s \t Weight: %s  \t  Price: %i" % (item[0], item[1], item[2]))


lst1 = [["Muhammad Ali",'BS-CS',100,82], ["Muhammad Aun",'BS-CS',100,78],["Muhammad Shahid",'BS-CS',100,81]]

# Printing initial marks
for i in lst1:
    print("\n")
    print(f"Student Name: %s \t Program: %s \t Total Marks: %i \t Obtained Marks: %i" % (i[0], i[1], i[2], i[3]))

# Increasing the marks of Muhammad Aun
lst1[1][3] += 7
print(lst1[1][3])

lst = [2,4,6,8,10]
lst1 = [i**3 for i in lst]
print(lst1)

'''
List comprehensions can also be used to replicate the action of nested loops in a more
compact form. For example, we multiply each of the elements contained within list1 with
each other
'''

list = [[1,2,3,4,5],[6,7,8,9,10]]
list1 = [i * j for i in list[0] for j in list[1]]
print(list1)

words = 'Here is a sentence'.split()
lst =[[word,len(word)] for word in words]
print(lst)

s = "Python is a good programming language".split()
print(s)

lst = [[word,len(word)] for word in s]
print(lst)

