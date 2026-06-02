nums = [1,2,3,1]

def rob(nums):
    if not nums:
        return 0
    for i in range(2, len(nums)):
        nums[i] += max(nums[i - 1], nums[i - 2])
    return max(nums[-1], nums[-2])