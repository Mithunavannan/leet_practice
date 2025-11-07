class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged_num = nums1+nums2
        print(merged_num)
        merged_num.sort()
        print(merged_num)
        n = len(merged_num)
        if n%2 == 1:
            return float(merged_num[n // 2])
        else:
            return(merged_num[n // 2 - 1] + merged_num[n // 2]) / 2.0