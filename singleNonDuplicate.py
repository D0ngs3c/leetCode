#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once.
Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.

题目大意：
给定一个递增有序的整数数组，其中除一个元素外，剩余元素均出现两次。找出那个单独的元素。

注意：你的解法应当满足O(log n)时间和O(1)空间约束。

解题思路：
二分查找（Binary Search）

从数组递增有序和O(log n)时间复杂度推断，题目可以采用二分查找求解。
'''
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        head = 0
        tail = len(nums)-1
        while head < tail:
            mid = (head + tail) / 2
            if nums[mid] == nums[mid + 1]:
                if ((mid) % 2):
                    tail = mid - 1
                else:
                    head = mid + 2
            elif nums[mid] == nums[mid - 1]:
                if ((mid-1) % 2):
                    tail = mid - 2
                else:
                    head = mid + 1
            else:
                return nums[mid]
        return nums[head]


#测试
if __name__ == '__main__':
    a = Solution()
    l1 = [1,1,2,3,3,4,4,8,8]
    l2 = [0,1,1]
    l3 = [3,3,7,7,10,11,11]

    print a.singleNonDuplicate(l1)
    print a.singleNonDuplicate(l2)
    print a.singleNonDuplicate(l3)

#https://leetcode.com/problems/single-element-in-a-sorted-array/description/
