class Solution {
    public boolean isPalindrome(ListNode head) {
        if (head == null || head.next == null) return true;

        ListNode slow=head;
        ListNode fast=head;


        while(fast!=null && fast.next!=null ){
            slow=slow.next;
            fast=fast.next.next;
        }

        //revers the second half

        ListNode prev=null;
        ListNode curr=slow;
        while(curr!=null){
            ListNode next=curr.next;
            curr.next=prev;
            prev=curr;
            curr=next;
        }

        //comaring first && second half;
        ListNode fval=head;
        ListNode sval=prev;
        while(sval!=null&fval!=null){
            if(fval.val!=sval.val)return false; 
            fval=fval.next;
            sval=sval.next;
        }

        return true;

    }
}







































//         // Step 1: Find middle
//         ListNode slow = head;
//         ListNode fast = head;
//         while (fast != null && fast.next != null) {
//             slow = slow.next;
//             fast = fast.next.next;
//         }

//         // Step 2: Reverse second half
//         ListNode prev = null;
//         ListNode curr = slow;
//         while (curr != null) {
//             ListNode nextTemp = curr.next;
//             curr.next = prev;
//             prev = curr;
//             curr = nextTemp;
//         }

//         // Step 3: Compare both halves
//         ListNode firstHalf = head;
//         ListNode secondHalf = prev; // head of reversed second half
//         while (secondHalf != null && firstHalf != null) {
//             if (firstHalf.val != secondHalf.val) return false;
//            firstHalf = firstHalf.next;
//            secondHalf = secondHalf.next;
// }


//         return true;