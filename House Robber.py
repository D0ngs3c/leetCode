#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/house-robber/description/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''

'''
动态规划：从以下三点思考。
设dp[i]为nums[i]结尾的最佳rob money
1、最优子结构：dp[i] = max(dp[i-1], dp[i-2] + nums[i])

2、边界：dp[0] = nums[0]
         dp[1] = max(nums[0] + nums[1])

3、状态转移公式:dp[i] =  
                        dp[i] = nums[0];                          i = 0
                        dp[i] = max(nums[0] + nums[1];            i = 1
                        dp[i] = max(dp[i-1], dp[i-2] + nums[i]);  other

思路理清了，coding easy!
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp1 = nums[0]
        dp2 = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            dp2, dp1 = max(dp2, dp1 + nums[i]), dp2
        return dp2

#测试实例
if __name__ == '__main__':
    a = Solution()
    b = [1,2,3,1]
    c = [2,7,9,3,1]
    d = []
    e = [2,1,1,2]
    print a.rob(b)
    print a.rob(c)
    print a.rob(d)
    print a.rob(e)
