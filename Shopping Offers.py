#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/shopping-offers/description/

Example 1:
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
Example 2:
Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
Output: 11
Explanation: 
The price of A is $2, and $3 for B, $4 for C. 
You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer #1), and $3 for 1B, $4 for 1C. 
You cannot add more items, though only $9 for 2A ,2B and 1C.
Note:
There are at most 6 kinds of items, 100 special offers.
For each item, you need to buy at most 6 of them.
You are not allowed to buy more items than you want, even if that would lower the overall price.
'''

# 记忆化搜索（Search + Memoization）

# 从needs出发，遍历special：
# dp[needs]初始化为sum(prices * needs)
# dp[needs] = min(dp[needs], dp[needs - special[:-1]] + special[-1])

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        dp = dict() #创建新字典
        def solve(tup):
            if tup in dp:
                return dp[tup]
            dp[tup] = sum(t * p for t, p in zip(tup, price)) #计算总价,dp[needs]初始化为sum(prices * needs)
            for sp in special:
                ntup = tuple(t - s for t, s in zip(tup, sp)) #需要购买的物品减去优惠券上的物品， 剩下还需购买的物品
                if min(ntup) < 0:                            #若还需购买的物品<0， 则此次优惠券不能用，跳出循环，继续下一次循环
                    continue                                 #跳过后续语句，重新循环
                dp[tup] = min(dp[tup], solve(ntup) + sp[-1])
            return dp[tup]
        return solve(tuple(needs))


#测试实例
if __name__ == '__main__':
    a = Solution()
    price, special, needs = [2,5], [[3,0,5],[1,2,10]], [3,2]
    price1, special1, needs1 = [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
    print a.shoppingOffers(price, special, needs)
    print a.shoppingOffers(price1, special1, needs1)