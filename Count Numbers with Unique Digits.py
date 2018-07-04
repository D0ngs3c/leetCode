#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/count-numbers-with-unique-digits/description/

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])

Credits:
Special thanks to @memoryless for adding this problem and creating all test cases.
'''

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        res = 10
        count = 9
        for i in range(2, n + 1):
            count *= 11 - i
            res += count 

        return res 


#测试实例
if __name__ == '__main__':
    a = Solution()
    n = 0
    n1 = 1
    n2 = 2
    n3 = 3
    print a.countNumbersWithUniqueDigits(n)
    print a.countNumbersWithUniqueDigits(n1)
    print a.countNumbersWithUniqueDigits(n2)
    print a.countNumbersWithUniqueDigits(n3)