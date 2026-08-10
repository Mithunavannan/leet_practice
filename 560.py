def subarraySum(self, nums, k):
    count = 0
    sum_so_far = 0
    sum_counts = {0: 1}  # Initialize with sum 0 occurring once

    for num in nums:
        sum_so_far += num
        
        # Check if there is a subarray (ending at the current index) that sums to k
        if (sum_so_far - k) in sum_counts:
            count += sum_counts[sum_so_far - k]
        
        # Update the count of the current sum in the dictionary
        if sum_so_far in sum_counts:
            sum_counts[sum_so_far] += 1
        else:
            sum_counts[sum_so_far] = 1

    return count