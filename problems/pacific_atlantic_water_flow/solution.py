class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights:
            return []
        m, n = len(heights), len(heights[0])

        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]

        def dfs(i, j, reachable):
            reachable[i][j] = True
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < m and 0 <= new_j < n and not reachable[new_i][new_j] and heights[new_i][new_j] >= heights[i][j]:
                    dfs(new_i, new_j, reachable)
        for i in range(m):
            dfs(i, 0, pacific_reachable)
            dfs(i, n-1, atlantic_reachable)
        for j in range(n):
            dfs(0, j, pacific_reachable)
            dfs(m-1, j, atlantic_reachable)
        result = []

        for i in range(m):
            for j in range(n):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])
        return result