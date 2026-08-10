class Solution(object):
    def missingNumber(self, nums):
        for num in nums:
            expected_sum = (len(nums) * (len(nums) + 1) // 2)
            actual_sum = sum(nums)

            OP = expected_sum - actual_sum
        return OP