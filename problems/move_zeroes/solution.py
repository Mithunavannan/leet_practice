class Solution(object):
    def moveZeroes(self, nums):

        write_ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write_ptr], nums[i] = nums[i], nums[write_ptr]
                write_ptr += 1
        