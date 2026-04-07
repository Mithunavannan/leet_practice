class Solution(object):
    def jump(self, nums):

        
        
        jumps = 0
        prev = 0
        curr = 0

        for i in range(len(nums) - 1):
            curr = max(curr, i + nums[i])
            if i == prev:
                jumps += 1
                prev = curr
        return jumps
            