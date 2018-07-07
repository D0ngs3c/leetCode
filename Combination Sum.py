#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-06 16:21:46
# @Version : $python2.7$

'''
https://leetcode.com/problems/combination-sum/description/

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret = []
        if len(candidates) == 0 or target < 0:
            return self.ret

        curr = []
        candidates.sort()
        
        
        def backtracking(ret, curr, candidates, target, level):
            if target == 0:
                r = copy.copy(curr)    #浅拷贝，直接使用append会出错
                ret.append(r)
                # print ret
                return
            elif target < 0:
                return
            for i in range(level, len(candidates)):
                target -= candidates[i]
                curr.append(candidates[i])
                backtracking(ret, curr, candidates, target, i)
                curr.pop()
                target += candidates[i]

        backtracking(ret, curr, candidates, target, 0)
        return ret

#测试实例
if __name__ == '__main__':
    a = Solution()
    # candidates, target = [2,6,3,7], 7
    candidates = [2, 3, 5]; target = 8

    print a.combinationSum(candidates, target) 