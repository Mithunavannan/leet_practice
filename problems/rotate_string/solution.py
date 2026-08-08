class Solution(object):
    def rotateString(self, s, goal):
        for i in range(len(s)):
            if s[i:] +s[:i] == goal:
                return True
        return False