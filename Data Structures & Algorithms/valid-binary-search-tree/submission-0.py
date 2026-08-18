# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return 
            left = dfs(node.left)
            res.append(node.val)
            right = dfs(node.right)
            return res
        dfs(root)
        flag = True
        for i in range(len(res)-1):
            if res[i+1]>res[i]:
                continue
            else:
                flag = False
        if flag == True:
            return True
        else:
            return False 
