/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
    let mergeLists = (a, b) => {
        const ans = new ListNode();
        let temp = ans;
        while (a != null && b != null) {
            if (a.val < b.val) {
                temp.next = a;
                a = a.next;
            } else {
                temp.next = b;
                b = b.next;
            }
            temp = temp.next;
        }
        if (a == null) {
            temp.next = b;
        }
        if (b == null) {
            temp.next = a;
        }
        return ans.next;
    };

    if (lists.length == 0) {
        return null;
    }
    while (lists.length > 1) {
        let a = lists.shift();
        let b = lists.shift();
        let temp = mergeLists(a, b);
        lists.push(temp);
    }
    return lists[0];
};
