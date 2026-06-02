head = [1,2,3,4,5]
n = 2

def removeNthFromEnd(head, n):
    if n in head:
        head.remove(n)