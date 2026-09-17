from collections import Counter
nums = [1,2,3,2,4,3,1,2]

counts = Counter(nums)

sorted_nums = sorted(nums, key = lambda x: (-counts[x], x))
print(sorted_nums)