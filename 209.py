arr_1 = [2, 3, 1, 2, 4, 3]
target = 7

for i in range(len(arr_1)):
    for j in range(i + 1, len(arr_1)):
        if arr_1[i] + arr_1[j] == target:
            print(arr_1[i], arr_1[j])