class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        
        pCount = Counter(p)
        windowCount = Counter()

        result = []
        left = 0

        for right in range(len(s)):
            windowCount[s[right]] += 1
            if right - left + 1 > len(p):
                windowCount[s[left]] -= 1

                if windowCount[s[left]] == 0:
                    del windowCount[s[left]]
                left += 1
            
            if windowCount == pCount:
                result.append(left)
        return result