#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest Tmp and return its Tmp.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest Tmp = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

#法一：Kadane算法 
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
    
# Time complexity O(n)
# Space  complexity O(1)

# 法二：利用动态规划的思想完成，时间复杂度为O(n)：
# 1）状态转移公式：Tmp[i]=max(Tmp[i-1]+nums[i], nums[i]) //局部最优解
#                  m = max(m, Tmp[i]) //全局最优解

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

# Time complexity O(n)
# Space  complexity O(1)

#法三：分治法（divide and conquer，D&C）
# 使用分治解决问题的过程包括两个步骤：
# 1.找出基线条件，这种条件必须尽可能简单
# 2.不断将问题分解，或者说缩小规模，直到符合基线条件

# 将数组均分为两个部分，那么最大子数组会存在于：
# 左侧数组的最大子数组
# 右侧数组的最大子数组
# 左侧数组的以右侧边界为边界的最大子数组+右侧数组的以左侧边界为边界的最大子数组

class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.solve(nums, 0, len(nums)-1)

    def solve(self, nums, low, high):
        if low == high:
            return nums[low]

        mid = (low + high)/2
        leftMax = self.solve(nums, low, mid)
        rightMax = self.solve(nums, mid+1, high)

        #计算左子串最右边的最大子串和
        leftSum = nums[mid]
        Tmp = nums[mid]
        for i in range(mid-1, low, -1):
            Tmp += nums[i]
            leftSum = max(leftSum, Tmp)

        #计算右子串最左边最大子串和
        rightSum = nums[mid + 1]
        Tmp = nums[mid + 1]
        for i in range(mid+2,high+1):
            Tmp += nums[i]
            rightSum = max(rightSum, Tmp)
            
        return max(leftSum + rightSum, max(leftMax, rightMax))

# Time complexity O(nlogn)
# Space  complexity O(1)


#测试实例
if __name__ == '__main__':
    a = Solution()
    b = Solution1()
    c = Solution2()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print a.maxSubArray(nums)
    print b.maxSubArray(nums)
    print c.maxSubArray(nums)