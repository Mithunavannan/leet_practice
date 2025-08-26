# Definition for singly-linked list.
#class ListNode:
#   def __init__(self, val=0, next=None):
#        self.val = val
#       self.next = next
class Solution:
    def addTwoNumbers(self, l1,l2):
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        
        while l1 or l2 or carry:
            x = l1.val if l1 else 0   # ✅ get value, not node
            y = l2.val if l2 else 0   # ✅ get value, not node
        
            s = x + y + carry
            carry = s//10

            tail.next=ListNode(s % 10)
            tail = tail.next

            if l1:l1 = l1.next
            if l2:l2 = l2.next
        return dummy.next