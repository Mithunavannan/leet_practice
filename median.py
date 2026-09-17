nums = [2,4,1,3,5]

nums.sort()
n = len(nums)
if n % 2 == 0:
    median = (nums[n//2 - 1] + nums[n//2]) / 2
else:
    median = nums[n//2]
print(median)