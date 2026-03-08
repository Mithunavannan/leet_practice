class Solution(object):
    def topKFrequent(self, nums, k):
        if k<=0:
            return[]
        else:
            count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return sorted(count, key = count.get, reverse=True)[:k]