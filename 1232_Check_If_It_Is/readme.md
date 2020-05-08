# 1232.Check if it is a straight line(Easy)

> [Lien for LeetCode](https://leetcode.com/problems/check-if-it-is-a-straight-line/)

###### 思路 (实现为python3  [Solutions.py](https://github.com/odcowl/LeetCode/blob/master/1232_Check_If_It_Is/Solutions.py))
这道题需要判断多个点是否均在一条直线上，用的是cross product的方法。
最一开始应该先将前两个点(xO,y0)(x1,y1)提取出来，作为后期每一个点与点0（或点1）的关系判断。
如果coordinate仅包含两个点，那么一定满足，因为两点是构成一直线的基本条件。
如果coordinate不仅仅包含两个点，那么从第三个点开始，他必须在前两个点构成的直线上。
前两个点构成的直线斜率k可用公示k=(y1-y0)/(x1-x0)计算出，第三个点(x2,y2)则必须满足(y2-y0)/(x2-x0) = k = (y1-y0)/(x1-x0)
当然为了避免x2 == x0这种情况导致运算错误（除0），我们选择把上述式子转化为(y2-y0)(x1-x0)=(x2-x0)(y1-y0)。
在coordinates中的每一点都必须满足这个条件，所以(x2,y2)可以扩大为(x,y)

这道题很简单，但是过程中稍微注意一下不能除0和计算的时间长度。
