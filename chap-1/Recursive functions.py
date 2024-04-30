import sys
print(f"The Limit Of Recursion Function Is: {sys.getrecursionlimit()}")
# Set the recursion limit
print(f"The New Limit Of Recursion Function Is: {sys.setrecursionlimit(200)},{sys.getrecursionlimit()}")

i = 0
def demo():
    global i
    i = i+1
    print("Hello World",i)
    demo()
# demo()

def natural_Numbers(n):
    if n==0:
        return
    print(n)
    return natural_Numbers(n-1)
natural_Numbers(5)

def itertest(low,high):
    while low <= high:
        print(low)
        low = low + 1

print(itertest(45,90))


def recurtest(low,high):
    if low <= high:
        print(low)
        recurtest(low +1, high)

print(recurtest(45,90))

import timeit

# Define the itertest function
def itertest(low, high):
    while low <= high:
        low = low + 1

# Define the recurtest function
def recurtest(low, high):
    if low <= high:
        recurtest(low + 1, high)

# Measure the execution time of the itertest function
itertest_time = timeit.timeit("itertest(45, 90)", globals=globals(), number=10000)

# Measure the execution time of the recurtest function
recurtest_time = timeit.timeit("recurtest(45, 90)", globals=globals(), number=10000)

# Print the execution times
print("Execution time of itertest:", itertest_time)
print("Execution time of recurtest:", recurtest_time)

'''
Iterative Approach Functions:
Factorial Calculation:
'''
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(f"Iterative Factorial Of 5 is: {factorial_iterative(5)}", )

'''
Recursive Approach Functions:
Factorial Calculation
'''
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)

print(f"Recursive Factorial of 5 is: {recursive_factorial(5)}")

'''
Iterative Approach Function
Sum of Squares:
'''

def sum_of_squares_iterative(n):
    result = 0
    for i in range(1, n+1):
        result += i ** 2
    return result
print(f"Sum of Squares By Using Iterative Approach of 5 is: {sum_of_squares_iterative(5)}")
print(f"Sum of Squares By Using Iterative Approach of 5 is: {sum_of_squares_iterative(4)}")

'''Recursive Approach Function
Sum of Squares:
'''
def sum_of_squares_recursive(n):
    if n == 0:
        return 0
    else:
        return n **2 + sum_of_squares_recursive(n-1)

print(f"Sum of Squares By Using Recursive Approach of 5 is: {sum_of_squares_recursive(5)}")
print(f"Sum of Squares By Using Recursive Approach of 4 is: {sum_of_squares_recursive(4)}")

'''Iterative Approach Functions:
Fibonacci Series:
'''
def fibonacci_iterative(n):
    fib_sequence = [0,1]
    for i in range(2, n+1):
         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return  fib_sequence
print(f"Fibonacci Series Of 8 By Using Iterative Approach is: {fibonacci_iterative(8)}")
print(f"Fibonacci Series Of 7 By Using Iterative Approach is: {fibonacci_iterative(7)}")

'''
printing n to 1 sequence
'''
n = int(input("Enter The Value Of n: "))
def natural_numbers(n):
    if n == 0:
        return
    print(n)
    return natural_Numbers(n-1)

print(natural_numbers(n))

'''
Syntax Of Recursion

def func():
    base condition:
          return
    #code
    return [recursive call]
    
call func()
'''

'''
Indirect Recursion:
A Function Calls another function which then calls the first function again
'''
def num(n):
    if n <= 0:
        return
    print(n,end="")
    num1(n-1)
def num1(n):
    print(n,end="")
    num(n-1)

print(num1(n))


'''
Recursion Factorial
'''
n = int(input("Enter The Value Of n: "))
def rec_fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * rec_fact(n-1)
print(rec_fact(n))

'''
Print 10 Times Your Name Without using Loop or manually
'''
count = 1
def rec_name(name):
    global count
    if count<=10:
        print(name)
        count += 1
        rec_name(name)
print(rec_name("Hamza"))

'''
Power Of Number Using Recursion
'''
def power_of_number(n,p):
    if p ==0 :
        return 1
    else:
     return n* power_of_number(n,p-1)

print(f"Power Of Number Using Recursion:  {(power_of_number(2,5))}")

