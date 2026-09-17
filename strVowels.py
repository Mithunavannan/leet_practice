s = "oombu da punda"

vowels = ["a", "e", "i", "o", "u"]

vowel_count = 0
constant_count = 0
space_count = s.count(" ")
for ch in s:
    if ch in vowels:
        vowel_count += 1
    if ch not in vowels:
        constant_count += 1
    if ch == " ":
        space_count += 1
        
print("no of vowels are", vowel_count)
print("no of constants are", constant_count)
print("no of spaces are", space_count)