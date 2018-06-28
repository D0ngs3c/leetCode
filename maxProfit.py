#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
#暴力破解：遍历数组，找出最大价格差。由于时间复杂度过大，在LeetCode中可以通过运行测试但不能通过提交。
class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        Maxprice = 0
        for i in range(len(prices)-1):
            for j in range(i,len(prices)):
                price = prices[j] - prices[i]
                if price > Maxprice:
                    Maxprice = price 

        return Maxprice

# Time complexity O(n^2)
# Space  complexity O(1)


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #设Min为正无穷大数。另外负无穷为float('-Inf')、-float('Inf')
        Min = float("inf")
        Max = 0

        #在买入的价格足够小的情况下，判断价格差最大
        for i in range(len(prices)):
            if prices[i] < Min:
                Min = prices[i]
            elif prices[i] - Min > Max:
                Max = prices[i] - Min 
        return Max

# Time complexity O(n)
# Space  complexity O(1)

# 测试实例
if __name__ == '__main__':
    a = Solution1()
    b = Solution2()
    price1 = [7,1,5,3,6,4]
    price2 = [7,6,4,3,1]
    price3 = []
    price4 = [1,2]


    print a.maxProfit(price1)
    print b.maxProfit(price1)
    print "+++++++++"
    print a.maxProfit(price2)
    print b.maxProfit(price2)
    print "+++++++++"
    print a.maxProfit(price3)
    print b.maxProfit(price3)
    print "+++++++++"
    print a.maxProfit(price4)
    print b.maxProfit(price4)