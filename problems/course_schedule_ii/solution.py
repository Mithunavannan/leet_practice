class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)

        visit= [0] * numCourses
        result=[]

        def dfs(course):
            if visit[course] == 1:
                return False
            if visit[course] == 2:
                return True

            visit[course] = 1

            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visit[course] = 2
            result.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result