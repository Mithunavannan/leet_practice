class Solution(object):
    def frequencySort(self, nums):
        for num in nums:
            count = {}
            for num in nums:
                count[num] = count.get(num, 0) + 1
            nums.sort(key = lambda x: (count[x], -x))

            return nums