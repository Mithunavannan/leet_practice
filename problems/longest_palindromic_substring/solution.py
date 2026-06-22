class Solution(object):
    def longestPalindrome(self, s):
        res = ""
        max_len = 0

        def expand(left, right):
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left + 1:right]
        for i in range(len(s)):
            odd = expand(i, i)

            if len(odd) > max_len:
                res = odd
                max_len =  len(odd)
            
            even = expand(i, i+1)
            if len(even) > max_len:
                res = even
                max_len = len(even)
        return res