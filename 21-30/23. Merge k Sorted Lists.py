# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        
        while len(lists) >= 2:
            first = lists.pop()
            second = lists.pop()

            dummy = ListNode()
            cur = dummy
            while first and second:
                if first.val < second.val:
                    cur.next = ListNode(first.val)
                    first = first.next
                else:
                    cur.next = ListNode(second.val)
                    second = second.next
                cur = cur.next
            
            if first:
                cur.next = first
            else:
                cur.next = second
            
            lists.append(dummy.next)
        
        return lists[0]

