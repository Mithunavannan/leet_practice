nums = [1, 2, 3, 4]

def product_except_self(nums):
    left = 0
    
    for i in range(len(nums)):
        left += 1
        while i in index(nums, left):
            nums[i] *= left
            left += 1
    return nums