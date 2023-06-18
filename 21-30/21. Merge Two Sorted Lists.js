/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let head = new ListNode();
    let start = head;

    while(list1 != null || list2 != null) {
        if (list1 == null){
            while(list2 != null) {
                start.next = new ListNode(list2.val);
                list2 = list2.next;
                start = start.next;
            }
        }
        else if (list2 == null) {
            while(list1 != null){
                start.next = new ListNode(list1.val);
                list1 = list1.next;
                start = start.next;
            }
        }
        else if (list1.val < list2.val) {
            start.next = new ListNode(list1.val);
            list1 = list1.next;
            start = start.next;
        }
        else {
            start.next = new ListNode(list2.val);
            list2 = list2.next;
            start = start.next;
        }
    }
    return head.next;
};