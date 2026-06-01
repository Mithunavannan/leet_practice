class Solution(object):
    def networkDelayTime(self, times, n, k):
        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        min_heap = [(0, k)]
        visited = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            visited[node] = time

            if node in graph:
                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(
                            min_heap,
                            (time + weight, neighbor)
                        )
        if len(visited) != n:
            return -1
        return max(visited.values())