"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        output = []
        
        while q:
            condition = q.popleft()
            output.append(condition.val)
            
            for c in reversed(condition.children):
                q.appendleft(c)
        return output
