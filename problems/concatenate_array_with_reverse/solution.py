class Solution(object):
    def concatWithReverse(self, nums):
        rev_num = nums[::-1]
        return nums + rev_num