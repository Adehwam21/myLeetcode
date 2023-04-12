# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using the idea of two pointers where one pointer moves twice as fast as the other
        
        p1 = head   #slow
        p2 = head   #fast   
        
        while p2 and p2.next: # to make sure the pointers remain in bound
            p1 = p1.next
            p2 = p2.next.next
        return p1