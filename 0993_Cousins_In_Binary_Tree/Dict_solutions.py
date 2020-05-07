# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        lookup = dict() #用来收集x,y在root里的层数（或深度）:i及对应parent:p
        def dfs(root,i=0,p=None):
            # 新函数dfs用来满足向lookup字典中有序添加，由于该函数不是直接完成题目需求，所以另设def
            # 层数起始为0，parent起始为没有parent
            if root: 
                #如果root存在
                if root.val in (x,y): lookup[root.val] = (i,p)
                    #如果root.val是x或y中其中任意一个数字
                #如果root.val不满足x或y，用root.left和root.right再次验证，注意此时层数+1，parent变为现root.val
                dfs(root.left,i=i+1,p=root.val)
                dfs(root.right,i=i+1,p=root.val)
        #对题目中给出的root进行dfs计算，此时lookup字典已经被填上
        dfs(root)
        if lookup[x][0] == lookup[y][0] and lookup[x][1] != lookup[y][1]:
            return True
