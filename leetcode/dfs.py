import time
start_time = time.time()
##################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = []
        def dfs(root):
            if root != None:
                if low <= root.val <= high:
                    result.append(root.val)
                if root.left != None or root.right != None:
                    dfs(root.left)
                    dfs(root.right)
            else:
                return
        dfs(root)
        return sum(result)
'''
##################################################
end_time = time.time()
print('time: ', end_time - start_time)