class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        from collections import deque
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        queue = deque([(beginWord, 1)])

        while queue:
            currentWord, length = queue.popleft()
            if currentWord == endWord:
                return length
            for i in range(len(currentWord)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = currentWord[:i] + c + currentWord[i+1:]
                    if next_word in wordSet:
                        wordSet.remove(next_word)
                        queue.append((next_word, length + 1))
        return 0