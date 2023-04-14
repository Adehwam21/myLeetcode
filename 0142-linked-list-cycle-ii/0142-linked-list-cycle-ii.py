# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using the idea of Floyd's Tortoise and Hare 
        
        p1 = head   #slow
        p2 = head   #fast
        
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            
            if p1 == p2:
                checker = head  #to check the pos of the list node the tail connects to
                
                while p1 != checker:
                    checker = checker.next
                    p1 = p1.next
                return checker
            
        return None