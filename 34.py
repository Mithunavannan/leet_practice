nums = [5,7,7,8,8,10]
target = 8

def searchRange(nums, target):
    if target not in nums:
        return [-1, -1]
    first = nums.index(target)
    last = len(nums) - 1 - nums[::-1].index(target)
    return [first, last]