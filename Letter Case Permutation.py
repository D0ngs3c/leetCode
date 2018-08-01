#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/letter-case-permutation/description/

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.
'''

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S: 
            return [S]
        rest = self.letterCasePermutation(S[1:])

        if S[0].isalpha():
            return [S[0].lower() + s for s in rest] + [S[0].upper() + s for s in rest]
        return [S[0] + s for s in rest]



class Solution1(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        l = len(S)

        #替换字符串string中指定位置p的字符为c
        def rep(string,p,c):
            new = []
            for s in string:
                new.append(s)
            new[p] = c
            return ''.join(new)

        def backtrack(s, i, res):
            if i == l:
                res.append(s)
                return
            backtrack(s, i + 1, res)
            if s[i].isalpha():
                tmp = ord(s[i])
                tmp ^= (1 << 5)  #通过ASCII码的形式 改变大小写
                # tmp += 32
                s = rep(s, i, chr(tmp))  
                backtrack(s, i + 1, res)

        backtrack(S, 0, res)
        return res

if __name__ == '__main__':
    a = Solution1()
    S = "rmR"
    print a.letterCasePermutation(S)