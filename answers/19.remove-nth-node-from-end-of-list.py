#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1pos = 0
        p1 = head
        p2 = head
        while p1 != None:
            if p1pos > n :
                p2 = p2.next
            print(p1pos,p1.val,p2.val)
            p1 = p1.next
            p1pos += 1
        if p1pos == n:
            return head.next
        if p1pos == 1:
            return None
        else:
            p2.next = p2.next.next
        return head
        
# @lc code=end

