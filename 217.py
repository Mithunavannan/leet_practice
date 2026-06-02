arr_1 = [1, 2, 3, 3]
def find_duplicates(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        else:
            seen.add(item)
    return False
print(find_duplicates(arr_1))