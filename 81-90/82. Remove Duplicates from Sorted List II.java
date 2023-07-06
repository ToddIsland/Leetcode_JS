/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode node = new ListNode(101, head);

        ListNode first = node;

        while(node.next != null){
            if(node.next.next == null){
                break;
            }
            if(node.next.val == node.next.next.val){
                ListNode temp = node.next.next;
                while(temp != null && node.next.val == temp.val){
                    temp = temp.next;
                }
                node.next = temp;
            }
            else{
                node = node.next;
            }
        }
        return first.next;
    }
}