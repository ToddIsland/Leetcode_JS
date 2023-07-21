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
            mergedLists = []
            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i + 1] if i + 1 < len(lists) else None

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

                mergedLists.append(dummy.next)
            lists = mergedLists

        return lists[0]
