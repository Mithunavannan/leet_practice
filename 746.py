cost = [10,15,20]

def minCostClimbingStairs(self, cost):
    if not cost:
        return 0
    for i in range(2, len(cost)):
        prev, curr = 0, 0
        cost[i] += min(cost[i - 1] + cost[i - 2] + prev)
    return curr