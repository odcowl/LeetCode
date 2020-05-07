# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        bfs = [(root, None)]
        print(bfs)
        while bfs:
            cousins = [p for node, p in bfs if node.val in (x, y)]
            if cousins: return len(cousins) > 1 and cousins[0] != cousins[1]
            bfs = [(c, node.val) for node, _ in bfs for c in (node.left, node.right) if c]
