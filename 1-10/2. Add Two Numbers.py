# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def iter(l1, l2, remain):
            if l1 == None and l2 == None and remain == 0: return None
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            sum = n1+n2+remain
            node1 = l1.next if l1 else None
            node2 = l2.next if l2 else None
            return ListNode(sum%10,iter(node1, node2, sum//10))
        
        return iter(l1,l2,0)