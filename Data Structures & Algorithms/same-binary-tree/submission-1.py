# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1, res2 = [], []

        def inorder(node, res):
            if not node:
                res.append(None)
                return 
            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)
        def preorder(node, res):
            if not node:
                res.append(None)
                return
            res.append(node.val)
            preorder(node.left, res)
            preorder(node.right, res)
    
        inorder(p,res1), inorder(q, res2)
        preorder(p, res1), preorder(q, res2)
        return res1 == res2 