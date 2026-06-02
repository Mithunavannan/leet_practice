def shortestPathBinaryMatrix(self, grid):
    from collections import deque
    if not grid or grid[0][0] != 0:
        return -1
    n = len(grid)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    queue = deque([(0, 0, 1)])  # (x, y, distance)
    visited = set((0, 0))
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == (n - 1, n - 1):
            return dist
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n and grid[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append((new_x, new_y, dist + 1))
    return -1
