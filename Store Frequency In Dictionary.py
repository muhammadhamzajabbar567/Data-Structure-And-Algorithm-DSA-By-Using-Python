# Method 1
from collections import Counter
nums = [1,2,3,4,5,6,7,8,9,9,9,8,8,7,6,5,5,4,4,3,3,3,2,2,2,2,2,1,2,5,8,9,6,5,7,0,11,22,44,55,333]
frequency_map = Counter(nums)
print(frequency_map)

# Method 2

nums = [1,2,3,4,5,6,7,8,9,9,9,8,8,7,6,5,5,4,4,3,3,3,2,2,2,2,2,1,2,5,8,9,6,5,7,0,11,22,44,55,333]
frequency_map = dict()
for i in range(0, len(nums)):
    if nums[i] in frequency_map:
        frequency_map[nums[i]] += 1
    else:
        frequency_map[nums[i]] = 1
print(frequency_map)

# Method 3

nums = [1,2,3,4,5,6,7,8,9,9,9,8,8,7,6,5,5,4,4,3,3,3,2,2,2,2,2,1,2,5,8,9,6,5,7,0,11,22,44,55,333]
n = len(nums)
hash_map = dict()
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)