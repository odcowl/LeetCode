# 000.Two Sum(Easy)

> [Lien for LeetCode](https://leetcode.com/problems/two-sum/)

###### 思路 (实现为python3[])
我们需要找到在给定list中，两个数的总和为target的index。利用字典的解法则是，若list的value不在dict中，则在dict中写入dict[value]=index。
如果此时，我们的目标是找到target-value对应的value‘所在的index，此时利用字典就可以得到对应index。
