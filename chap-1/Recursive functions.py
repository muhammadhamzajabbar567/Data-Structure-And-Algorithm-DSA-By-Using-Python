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
