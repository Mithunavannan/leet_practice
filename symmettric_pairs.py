nums = [(1,2),(2,1),(3,4),(4,5),(5,4)]

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i][0] == nums[j][1] and nums[i][1] == nums[j][0]:
            print(f"({nums[i][1]} {nums[i][0]})", end=" ")