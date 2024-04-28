'''Functions that take other functions as arguments, or that return functions,
are called higher order functions. Python 3 contains two built-in higher order functions,
filter() and map().'''

lst = [1,2,3,4,5,6,7,8,9]
lst1 = list(map(lambda x: x**3, lst))
print(lst1)

lst = [1,2,4,6,7,9,5,8,3]
list1 = (list(map(lambda x: x**5,lst1)))
print(list1)

lst_2 = [1,2,4,6,7,9]
lst_2 = list(filter(lambda x: x>=3,lst_2))
print(lst)

lst_1 = [1, 2, 4, 6, 7, 9, 5, 8, 3]
lst_2 = [1, 2, 4, 6, 7, 9]
lst_1_2 = list(filter(lambda x: x[0] >= 3, zip(lst_1, lst_2)))
print(lst_1_2)

lst_1 = [1, 2, 4, 6, 7, 9, 5, 8, 3]
lst_2 = [1, 2, 4, 6, 7, 9]
lst_1_2 = list(map(lambda x: x[0] >= 3, zip(lst_1, lst_2)))
print(lst_1_2)

lst = str.split(f"The Longest Word In This Sentence")
print(sorted(lst, key=len))

lst = "1 4 6 7 8 9 10 11 12".split()
print(sorted(lst, key=len))

'''
Here is another example for case-insensitive sorting
'''
s = ['A','b','a','B','C','c']
s.sort(key=str.lower)
print(s)

s = ['A','b','a','B','C','c']
s.sort()
print(s)

lst = [["Rice",'2 KG', 400], ['Flour','1 KG',250],['Corn','1 KG',150]]
lst.sort(key = lambda item: item[1])
print(lst)

numbers = [15, 8, 10, 27, 6]

# Sort numbers based on their remainder when divided by 5
sorted_numbers = sorted(numbers, key=lambda x: x % 5)

print(sorted_numbers)


nums = [1,5,6,89,3,23,4,9]
sorted_nums = sorted(nums, key=lambda x: x%5)
print(sorted_nums)

# squares
squares = [x**2 for x in range(1,10)]
print(squares)

numbers = [1,2,3,4,5,6,7,8,9,10]
filter_even_numbers = [x for x in numbers if x%2 ==0]
print(filter_even_numbers)

filter_odd_numbers = [x for x in numbers if x %2 != 0]
print(filter_odd_numbers)

# list of tiples

pairs = [(x,x**2) for x in range(1,20)]
print(pairs)

pairs = [(x, x**2) for x in range(1,20)]
print(pairs)

pairs = [(lambda x: x**2)(x) for x in range(1, 20)]
print(pairs)

# Flattening a list of lists:
nested_lists = [[1,2,3],[4,5,6],[7,8,9]]
flattened_lists = [item for sublists in nested_lists for item in sublists]
print(flattened_lists)

# Converting strings to uppercase
words =  ["hello", "world", "python",'artificial intelligence',"machine learning","deep learning"]
upper_words = [word.upper() for word in words]
print(upper_words)

words =  ["hello", "world", "python",'artificial intelligence',"machine learning","deep learning"]
upper_words = [word.title() for word in words]
print(upper_words)

# Removing duplicates from a list
from collections import OrderedDict

numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers = list(OrderedDict.fromkeys(numbers))
print(unique_numbers)

numbers_new = [1, 2, 2, 3, 3, 4, 5, 5]
unique_numbers_new = list(set(numbers_new))
print(unique_numbers_new)

# Creating a list of even-length strings
words = ["apple", "banana", "orange", "kiwi", "grape"]
even_length_words = [word for word in words if len(word)%2 == 0]
print(even_length_words)

# Generating a list of tuples with conditional logic
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
result = [(x,"even") if x%2 == 0 else(x,"odd") for x in numbers]
print(result)


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
result = [
    (x, "even") if x % 2 == 0 else
    (x, "prime") if x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) else
    (x, "odd")
    for x in numbers
]
print(result)

# Creating a list of squares using a generator expression
number_range = range(0,111)
squares_range = [x**2 for x in number_range]
print(squares_range)

# Extracting vowels from a string
sentence = "Python is awesome!"
vowels = [char for char in sentence if char.lower() in 'aeiou']
print(vowels)

# Generating Fibonacci sequence using generator functions
# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b,a + b
#
# fib = [x for x in fibonacci()]
# print(fib)

# Generating prime numbers
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = (x for x in range(2, 101) if is_prime(x))

# Generating random numbers
import random
random_numbers = (random.randint(1,100) for _ in range(1,30))
print(list(random_numbers))

# Generating combinations of letters:
import itertools
letter_combinations = (''.join(comb) for comb in itertools.permutations('abc',2))
print(list(letter_combinations))


letter_combination_2 = (''.join(comb) for comb in itertools.permutations('I Love The Educators',2))
print(list(letter_combination_2))

letter_combination_3 = (''.join(comb) for comb in itertools.permutations('I Love The Educators',3))
print(list(letter_combination_3))

#for unique numbers
numbers = [1, 2, 3, 4, 5, 1, 2, 3]
unique_numbers = (x for x in set(numbers))


# Generating dates for a specific range
import datetime
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)
dates = (start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1))
print(list(dates))

#
import datetime
start_date = datetime.date(2022, 1, 1)
end_date = datetime.date(2022, 12, 31)
dates = (start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1))
