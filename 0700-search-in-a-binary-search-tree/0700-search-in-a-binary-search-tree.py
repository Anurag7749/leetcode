# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        while root is not None and root.val!=val:
            if val<root.val:
                root=root.left
            else:
                #val>root.val
                root=root.right
        return root