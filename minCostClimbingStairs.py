#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-06-28 08:22:34
# @Version : $python2.7$

'''
https://leetcode.com/problems/min-cost-climbing-stairs/description/

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        f0 = f1 = f2 = 0
        for i in cost:
            f1, f2 = i + min(f1, f2), f1
        return min(f1, f2)
        # if not cost:
        #     return 0

        # if len(cost) == 1:
        #     return cost[0]

        # # dp = []    
        # # for i in range(len(cost)):
        # #     dp.append(cost[i])
        # a = 0
        # b = cost[0]
        # # return dp
        # for i in range(len(cost)):
        #     dp[i] = min(dp[i-1], dp[i-2] + cost[i])

if __name__ == '__main__':
    a = Solution()
    cost1 = [10, 15, 20]
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost3 = []

    print a.minCostClimbingStairs(cost1)
    print a.minCostClimbingStairs(cost2)
    print a.minCostClimbingStairs(cost3)