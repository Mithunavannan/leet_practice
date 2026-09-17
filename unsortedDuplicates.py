nums = [2,3,1,9,3,1,3,9]


seen = {}
result = []
for num in nums:
    if num not in seen:
        result.append(num)
        seen[num] = True
print(result)