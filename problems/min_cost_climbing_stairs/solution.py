class Solution(object):
    def minCostClimbingStairs(self, cost):
        if not cost:
            return 0
        prev, curr = 0, 0
        for i in range(2, len(cost) + 1):

            prev,curr = curr, min(cost[i - 1] + curr, cost[i - 2] + prev)
        return curr