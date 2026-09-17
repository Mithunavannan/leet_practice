nums = [1,2,-1,1,3,1]

seen = set()
result = set()
for num in nums:
    if num in seen:
        result.add(num)
    else:
        seen.add(num)

non_repeating = []
for num in nums:
    if num not in result and num not in non_repeating:
        non_repeating.append(num)

print(non_repeating)