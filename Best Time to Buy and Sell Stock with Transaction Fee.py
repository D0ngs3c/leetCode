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
某一天只有两种可能：手上持有一股、手上未持股。
设第i天未持股最大收益为cash[i]
设第i天持有一股时的最大收益为hold[i]

首先分析cash[i]：
    第i天未持股又分两种情况：
        1、假设第i-1天也未持股，第i天继续不持股（不买入）的收益与i-1天相同，即cash[i] = cash[i-1]
        2、假设第i-1天持有一股，第i天卖出股票的收益更高，即cash[i] = hold[i-1] + prices[i] - fee
    所以：第i天未持股的最大收益取这两种情况的最大值，即：cash[i] = max(cash[i], hold[i-1] + prices[i] - fee)

接下来分析hold[i]：
    第i天持有一股也分为两种情况：
        1、假设第i-1天未持股，第i天买入一股的收益更高，即hold[i] = cash[i-1] - prices[i]
        2、假设第i-1天持有一股，第i天继续持该股的收益与i-1天相同，即hold[i] = hold[i-1]
    所以：第i天持一股的最大收益去这两种情况的最大值，即：hold[i] = max(cash[i-1] -prices[i], hold[i])

最后cash[-1]为该题所求。

内存优化：
    由于第i天的情况只和i-1天有关，所以用两个变量cash和hold就可以，不需要用数组。

'''
class Solution(object):
    def maxProfit(self, prices, fee):

        cash, hold = 0, -prices[0]

        for i in range(1, len(prices)):

            cash = max(cash, hold + prices[i] - fee)
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