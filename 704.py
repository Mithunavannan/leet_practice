nums = [-1, 0, 3, 5, 9, 2]
target = 9

def search(self, nums):
    if target in nums:
        return nums.index(target)
    else:
        return '-1'