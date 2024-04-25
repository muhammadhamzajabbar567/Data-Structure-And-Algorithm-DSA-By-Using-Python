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

