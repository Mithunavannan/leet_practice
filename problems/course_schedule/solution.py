class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        for course, prereq in prerequisites:
            if course not in graph:
                graph[course] = []
            graph[course].append(prereq)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if course not in graph:
                return True
            visited.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True