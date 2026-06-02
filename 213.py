nums = [2,3,2]

def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    def circle_rob(nums):
        val(1) = val(last)
        nums = circle_rob(nums[1:])
        return max(nums[0], nums[1])
    return max(circle_rob(nums), circle_rob(nums[:-1]))