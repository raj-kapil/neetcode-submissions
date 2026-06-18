# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0 
        # left_depth = self.maxDepth(root.left)
        # right_depth = self.maxDepth(root.right)

        # return 1 + max(left_depth, right_depth)
        if not root:
            return 0 
        
        from collections import deque
        q = deque()
        # if root.left:
        #     q.append(root.left)
        # if root.right:
        #     q.append(root.right)
        q.append(root)
        depth = 0
        while q:
            for i in range(len(q)):
                element = q.popleft()
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            depth += 1
        
        return depth
            
        