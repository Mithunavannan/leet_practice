class Solution(object):
    def rotate(self, nums, k):
       k = k%len(nums)

       rotated = nums[-k:] + nums[:-k]

       for i in range(len(nums)):
            nums[i] = rotated[i]

