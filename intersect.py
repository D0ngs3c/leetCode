#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, 
and the memory is limited such that you cannot load all elements into the memory at once?
'''
#1.暴力查找法，遍历第一个列表的每个元素，并在第二个列表中查找该元素是否出现，若出现且结果集中没有，则加入到结果集中。
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for k in nums1:
            index = -1
            for j in xrange(0, len(nums2)):
                if nums2[j] == k:
                    index = j
                    break
            if index != -1:
                res.append(k)
                del nums2[index]

        return res


#2.用字典统计第一个列表都出现了哪些数及出现的次数，然后顺序遍历第二个列表，
#发现同时出现的数则加入到结果列表中，同时将第一个列表中相应的出现次数减一。
class Solution1(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i]+1 if i in map else 1
        for j in nums2:
            if j in map and map[j] > 0:
                res.append(j)
                map[j] -= 1

        return res


# 3.先将两个数组排序，再维持两个指针分别扫描两个数组，寻找共同的元素
class Solution2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

        return res


#测试实例
if __name__ == '__main__':
    a = Solution()
    b = Solution1()
    c = Solution2()

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    print b.intersect(nums1, nums2)
    print c.intersect(nums1, nums2)
    print a.intersect(nums1, nums2)
