#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
'''
'''
动态规划：
    状态转移公式：dp[i][j] 表示dp[i][j]表示字符串s1的前i个字符和字符串s2的前j个字符变相等所要删除的字符的最小ASCII码累加值。
                dp[i][j] = 
                            dp[i-1][j] + ord(s1[i])
                            dp[i][j-1] + ord(s2[j])
                            dp[i-1][j-1] + (0 if ord(s1[i]) == ord(s2[j]) else (ord(s1[i]) + ord(s2[j])))

'''
#自顶而下
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]

        for i in xrange(len(s1) - 1, -1, -1):
            dp[i][len(s2)] = dp[i+1][len(s2)] + ord(s1[i])
        for j in xrange(len(s2) - 1, -1, -1):
            dp[len(s1)][j] = dp[len(s1)][j+1] + ord(s2[j])

        for i in xrange(len(s1) - 1, -1, -1):
            for j in xrange(len(s2) - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]),
                                   dp[i][j+1] + ord(s2[j]))
        return dp[0][0]

# Time Complexity: O(M*N)
# Space Complexity: O(M*N)

class Solution1(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        a1, a2 = map(ord, s1), map(ord, s2)
        l1, l2 = len(s1), len(s2)
        dp = [0]
        for x in range(l1):
            dp.append(dp[-1] + a1[x])
        for x in range(1, l2 + 1):
            ndp = [dp[0] + a2[x - 1]]
            for y in range(1, l1 + 1):
                if a2[x - 1] == a1[y - 1]: ndp.append(dp[y - 1])
                else: ndp.append(min(dp[y] + a2[x - 1], ndp[y - 1] + a1[y - 1]))
            dp = ndp
        return dp[-1]

        
        
# #自底而上
class Solution2(object):
    def minimumDeleteSum(self, s1, s2):
        # dp = [[0] * (len(s2) + 1)] * (len(s1) + 1)
        dp = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (dp[i - 1][j - 1]  if s1[i - 1] == s2[j - 1] else min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1])))
        #     a = 0 if ord(s1[i-1]) == ord(s2[j-1]) else ord(s1[i-1]) + ord(s2[j-1])
        # #比较三种情况
        #     dp[i][j] = min(dp[i-1][j-1] + a, min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1])))

        return dp[len(s1)][len(s2)]



            
#测试实例
if __name__ == '__main__':
    a = Solution()
    b = Solution1()
    c = Solution2()
    s1 = "delete"
    s2 = "leet"
    print a.minimumDeleteSum(s1, s2)
    print b.minimumDeleteSum(s1, s2)
    print c.minimumDeleteSum(s1, s2)