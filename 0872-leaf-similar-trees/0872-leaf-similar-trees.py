class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        
        def getLeaves(node, leaf_list):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                leaf_list.append(node.val)
                return
            
            getLeaves(node.left, leaf_list)
            getLeaves(node.right, leaf_list)
            
        leaves1 = []
        leaves2 = []
        
        getLeaves(root1, leaves1)
        getLeaves(root2, leaves2)
        
        return leaves1 == leaves2
