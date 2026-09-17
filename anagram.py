def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count_1 = {}
    count_2 = {}

    for char in s:
        count_1[char] = count_1.get(char, 0) + 1
    for char in t:
        count_2[char] = count_2.get(char, 0) + 1

    return count_1 == count_2


s = "anagram"
t = "nagaram"

print(is_anagram(s, t))