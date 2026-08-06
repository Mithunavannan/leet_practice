class Solution(object):
    def findDuplicates(self, nums):
        nums.sort()
        new_num = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                new_num.append(nums[i])
        return new_num