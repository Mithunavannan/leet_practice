arr = [1, 1, 2, 2, 3, 3, 3,3, 4, 4, 5]

def arr_freq(arr):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    return freq_dict
print(arr_freq(arr))
