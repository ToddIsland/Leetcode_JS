/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if(head == null) return null;

    let stack = [];

    let node = head;
    while(node != null){
        stack.push(node.val);
        node = node.next;
    }

    let fakeHead = new ListNode();
    let temp = fakeHead;

    while(stack.length){
        let nextNode = new ListNode(stack.pop());
        temp.next = nextNode;
        temp = temp.next;
    }
    return fakeHead.next;
};