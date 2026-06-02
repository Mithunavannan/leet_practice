
nums = [1, 3, 5, 6]
target = 5

def searchInsert(nums, target):
    if target in nums:
        print(nums.index(target), "")
    else:
        return nlargest(nums, target)