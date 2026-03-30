class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        cache = [[0] * cols for _ in range(rows)]
        def dfs(i, j):
            if cache[i][j] != 0:
                return cache[i][j]
            max_length = 1
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                new_i, new_j = i + dx, j + dy
                if 0 <= new_i < rows and 0 <= new_j < cols and matrix[new_i][new_j] > matrix[i][j]:
                    length = 1+ dfs(new_i, new_j)
                    max_length = max(max_length, length)
            cache[i][j] = max_length
            return max_length

        longest_path = 0
        for i in range(rows):
            for j in range(cols):
                longest_path = max(longest_path, dfs(i, j))
        return longest_path