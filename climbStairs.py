#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/climbing-stairs/description/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

# 备忘录算法
class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)

        for i in range(n+1):
            if i < 3:
                dp[i] = i
            else:
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# Time complexity O(n)
# Space complexity O(n)



# 动态规划求解
class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n

        Stairs1 = 1
        Stairs2 = 2
        for i in range(3,n+1):
            Stairs1, Stairs2 = Stairs2, Stairs1 + Stairs2
        return Stairs2

# Time complexity O(n)
# Space complexity O(1)
# 相较于备忘录算法，优化了空间复杂度。

#测试实例
if __name__ == '__main__':
    a = Solution1()
    b = Solution2()
    n1 = 10
    print a.climbStairs(n1)
    print b.climbStairs(n1)
