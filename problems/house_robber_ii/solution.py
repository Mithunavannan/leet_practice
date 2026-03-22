class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def helper(arr):
            curr = 0
            prev = 0

            for num in arr:
                prev, curr = curr, max(curr, prev + num)
            return curr
        return max(helper(nums[1:]), helper(nums[:-1]))