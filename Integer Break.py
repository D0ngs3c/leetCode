#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$


'''
https://leetcode.com/problems/integer-break/description/

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
'''
'''
正整数从1开始，但是1不能拆分成两个正整数之和，所以不能当输出。

那么2只能拆成1+1，所以乘积也为1。

数字3可以拆分成2+1或1+1+1，显然第一种拆分方法乘积大为2。

数字4拆成2+2，乘积最大，为4。

数字5拆成3+2，乘积最大，为6。

数字6拆成3+3，乘积最大，为9。

数字7拆为3+4，乘积最大，为12。

数字8拆为3+3+2，乘积最大，为18。

数字9拆为3+3+3，乘积最大，为27。

数字10拆为3+3+4，乘积最大，为36。
'''
#找规律
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 3 :
            return n - 1    

        res = 1
        while n > 4:
            res *= 3
            n -= 3

        return res * n

# Time complexity O(n)
# Space complexity O(1)

#公式法 
class Solution1(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 3:
            return n - 1

        if (n == 4):
            return 4
        n -= 5

        return (3 ** (n / 3 + 1)) * (n % 3 + 2)

# Time complexity O(1)
# Space complexity O(1)

#观察上面列出的10之前数字的规律，还可以发现数字7拆分结果是数字4的三倍，而7比4正好大三，数字8拆分结果是数字5的三倍，而8比5大3，后面都是这样的规律。那么可以把数字6之前的拆分结果都列举出来，然后之后的数通过查表都能计算出来。
class Solution2(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis = [0,0,1,2,4,6,9]
        for i in range(7, n+1):
            lis.append(3 * lis[i - 3])

        return lis[n]

# Time complexity O(n)
# Space complexity O(n)

#测试实例
if __name__ == '__main__':
    a = Solution2()
    n = 9
    n1 = 10
    print a.integerBreak(n)
    print a.integerBreak(n1)