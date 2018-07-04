#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/range-sum-query-immutable/description/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:
1.You may assume that the array does not change.
2.There are many calls to sumRange function.
'''

#暴力法:直接计算从i到j的总和。 提交的时候 Time Limit Exceeded。
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        s = 0
        for k in range(i,j+1):
            s += self.nums[k]
        return s

# Time complexity O(n)
# Space  complexity O(1)



#预先计算
class NumArray1(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.s= [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.s[i+1] = self.s[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.s[j+1] - self.s[i]

# Time complexity O(1)
# Space  complexity O(n)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


#测试实例
if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    obj1 = NumArray1(nums)
    print obj.sumRange(0,2)
    print obj.sumRange(2,5)
    print obj.sumRange(0,5)
    print '==============='
    print obj1.sumRange(0,2)
    print obj1.sumRange(2,5)
    print obj1.sumRange(0,5)
