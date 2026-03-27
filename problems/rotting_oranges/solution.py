class Solution(object):
    def orangesRotting(self, grid):
        if not grid:
            return -1
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        minutes = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_x, new_y = x+dx, y+dy
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh -= 1
                        queue.append((new_x, new_y))
            minutes += 1
        return minutes if fresh == 0 else -1