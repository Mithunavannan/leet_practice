arr_1 = [3, 3, 4, 3, 6, 3, 4]
k = 2
def top_frequent(arr, k):
    if k <= 0:
        return []
    else:
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        return sorted(count, key=count.get, reverse=True)[:k]