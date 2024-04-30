import time
def OddGen(n,m):
    while n<m:
        yield n
        n += 2
def OddList(n,m):
    lst =[]
    while n<m:
        lst.append(n)
        n+=2
    return lst

#the time it takes to perform sum on an iterator
t1=time.time()
sum(OddGen(1,1000000))
print("Time to sum an iterator: %f" % (time.time() - t1))
#the time it takes to build and sum a list
t1=time.time()
sum(OddList(1,1000000))
print("Time to build and sum a list: %f" % (time.time() - t1))

lst1 = [1,2,3,4,5,6]
gen1 = (10**i for i in lst1)
print(gen1)
# for x in gen1:
#     print(x)
print(list(gen1))

# Generators
def count_upto(n):
    count = 1
    while count <= n:
        yield count
        count += 1

counter = count_upto(8)
for i in counter:
    print(i)

# Co-Routines
'''
Coroutines
In coroutines, the yield keyword is used for both sending and receiving values. 
Coroutines are similar to generators, but they also allow bidirectional communication
between the coroutine and the caller. Coroutines are created using the async def syntax in Python.
'''

async def greet():
    print("Hello")
    name = await get_name()
    print(f"Hell0 {name}")
async def get_name():
    return "Alice"

import asyncio
asyncio.run(greet())

