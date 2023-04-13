# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
         # Using the idea of Floyd's Tortoise and Hare 
        
        p1 = head   #slow
        p2 = head   #fast
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            
            if p2 == p1:
                return True
        return False