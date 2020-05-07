# 993.Cousins in Binary Tree (Easy)

> [Lien for LeetCode](https://leetcode.com/problems/cousins-in-binary-tree/)

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

###### 思路：

用字典Dictionnaire来储存x和y出现的深度/层数及对应的parent，并判读x和y是否满足1.相同层数 2.parent互不相同 这两点条件。
