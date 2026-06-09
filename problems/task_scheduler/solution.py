class Solution(object):
    def leastInterval(self, tasks, n):

        freq = Counter(tasks)
        max_freq = max(freq.values())

        countMax = 0

        for value in freq.values():
            if value == max_freq:
                countMax += 1
        return max(len(tasks), (max_freq - 1) * (n+1) + countMax)