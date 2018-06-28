#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

#Kadane算法 
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ending_here = 0
        max_so_far = float("-inf") #负无穷大
        
        for i in range(len(nums)):
            if(max_ending_here < 0):
                max_ending_here = 0 
            max_ending_here += nums[i]
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    

# 利用动态规划的思想完成，时间复杂度为O(n)。已知0,..,k的最大和以后，0,...k+1的最大和为：
# 1）状态转移公式：sum[i]=max(sum[i-1]+nums[i], nums[i]) //局部最优解
#                  m = max(m, sum[i]) //全局最优解
# 2）sum[k+1]=A[k+1]。

class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0] #全局最优解
        s = nums[0] #局部最优解

        for i in range(1, len(nums)):
            s = max(s + nums[i], nums[i])
            m = max(m, s)
        return m


#分治法

#测试实例
if __name__ == '__main__':
    a = Solution()
    b = Solution1()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # print a.maxSubArray(nums)
    print b.maxSubArray(nums)