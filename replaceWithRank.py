nums = [20, 15, 26, 2, 98, 6]

for num in nums:
    result = []

    for i in range(len(nums)):
        smaller = set()

        for j in range(len(nums)):
            if nums[j] < nums[i]:
                smaller.add(nums[j])
        rank = len(smaller) + 1
        result.append(rank)
print(result)