# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        dq = deque([root])
        count = 0
        if not root:
            return []
        while dq:
            count += 1
            temp = []
            for i in range(len(dq)):
                node = dq.popleft()
                temp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if count%2 == 0:
                res.append(reversed(temp))
            else:
                res.append(temp)
        return res 