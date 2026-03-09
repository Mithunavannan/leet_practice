class Solution(object):
    def searchRange(self, nums, target):
        
        if target not in nums:
            return [-1, -1]
        first = nums.index(target)
        last = len(nums) - 1 - nums[::-1].index(target)
        return [first, last]