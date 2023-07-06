import java.util.HashSet;

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        HashSet<ListNode> nodesSeen = new HashSet<ListNode>();

        ListNode node = head;
        while(node != null){
            if(nodesSeen.contains(node)){
                return node;
            }
            else{
                nodesSeen.add(node);
                node = node.next;
            }
        }
        return null;
    }
}