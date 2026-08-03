# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ dummy = TreeNode(0)
        self.current = dummy

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            node.left = None

            self.current.right = node

            self.current = node

            inorder(node.right)

        inorder(root)

        return dummy.right """


        stack = []
        dummy = TreeNode(0)
        current = dummy

        while stack or root:

            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()

            root.left = None
            current.right = root
            current = root

            root = root.right
    
        return dummy.right