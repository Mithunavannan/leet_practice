nums = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 1]

seen = set()
result = set()
for num in nums:
    if num in seen:
        result.add(num)
    else:
        seen.add(num)
print(list(result))