class Solution(object):
    def partitionLabels(self, s):

        l_o = {char: i for i, char in enumerate(s)}

        result = []
        start = 0
        end = 0
        for i, char in enumerate(s):
            end = max(end, l_o[char])

            if i == end:
                result.append(i - start+1)
                start = i+1
        return result
                