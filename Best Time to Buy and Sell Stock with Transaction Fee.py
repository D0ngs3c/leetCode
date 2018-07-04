#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$


'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
'''



'''
动态规划

要从第一i天过渡到第一i+1天，
要么出售已有的股票，cash = max(cash, hold + prices[i] - fee)
要么买入股票，hold = max(hold, cash - prices[i])
由于第i天的情况只和i-1天有关，所以用两个变量cash和hold就可以，不需要用数组。
'''
class Solution(object):
    def maxProfit(self, prices, fee):
        # cash: 手头的现金，即总的赚的金额，同时也是未持股时的现金额
        # hold: 手中有持股时的现金，即总金额减去手中股票的买入价
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            # 如果卖出持股比未持股赚，则卖出
            cash = max(cash, hold + prices[i] - fee)
            # hold 其实代表买入的最低价
            hold = max(hold, cash - prices[i])
        return cash

# Time complexity O(n)
# Space complexity O(1)


#测试实例
if __name__ == '__main__':
    a = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print a.maxProfit(prices, fee)