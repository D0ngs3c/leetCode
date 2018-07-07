#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/combinations/description/
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
#深度优先
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        def dfs(start, valuelist):
            if self.count == k:        #count就等于组合的长度
                ret.append(valuelist)
                return                 #return 返回？？？
            for i in range(start, n + 1):
                self.count += 1
                dfs(i + 1, valuelist + [i])
                self.count -= 1

        ret = []
        self.count = 0   #全局变量
        dfs(1, [])
        return ret


#测试实例
if __name__ == '__main__':
    a = Solution()
    n, k = 4, 2

    print a.combine(n, k)