# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=""
        while(head):
            s+=str(head.val)
            head=head.next
        rev_str=""
        for char in s:
            rev_str=char+rev_str
        if(rev_str==s):
            return True
        return False
        
        


        