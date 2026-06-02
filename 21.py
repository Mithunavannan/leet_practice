list1 = [1,2,4]
list2 = [1,3,4]

def mergeTwoLists(list1, list2):
    merged = list1 + list2
    merged.sort()
    return merged   