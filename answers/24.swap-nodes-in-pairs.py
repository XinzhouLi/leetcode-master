#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head
        dummy = head.next
        p0 = None
        p1 = head
        p2 = head.next
        p3 = head.next.next

        while p3 != None:
            p1.next = p3
            p2.next = p1
            if p0 != None:
                p0.next = p2
            if p3.next == None:
                return dummy
            p0 = p1
            p1 = p3
            p2 = p1.next
            p3 = p2.next

        if p0 != None:
            p0.next = p2
        p2.next = p1
        p1.next = p3
        print(p2.val, p1.val)
        return dummy
        
# @lc code=end

