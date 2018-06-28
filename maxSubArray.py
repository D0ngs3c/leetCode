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
    

#分治法

#测试实例
if __name__ == '__main__':
    a = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print a.maxSubArray(nums)