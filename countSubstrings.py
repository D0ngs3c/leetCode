#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/palindromic-substrings/description/

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
'''

'''
以字符串中的每一个字符都当作回文串中间的位置，然后向两边扩散，每当成功匹配两个左右两个字符，结果res自增1，然后再比较下一对。
注意回文字符串有奇数和偶数两种形式，如果是奇数长度，那么i位置就是中间那个字符的位置，所以我们左右两遍都从i开始遍历；
如果是偶数长度的，那么i是最中间两个字符的左边那个，右边那个就是i+1，这样就能cover所有的情况啦，而且都是不同的回文子字符串
'''

class Solution(object):
    # def __init__(self):
    #     self.res = 0
    def countSubstrings(self, str):
        if not str:
            return 0
        self.res = 0
        for i in range(len(str)):
            self.helper(str, i, i, self.res)
            self.helper(str, i, i + 1, self.res)
        return self.res

    def helper(self, str, i, j, res):
        while(i >= 0 and j < len(str) and str[i] == str[j]):
            i -= 1 
            j += 1
            self.res += 1 


# Time complexity O(n)
# Space complexity O(1)


#判断dp[i][j]是否为回文串
class Solution1():
    def countSubstrings(self,str):
        if not str:
            return 0
        s = []
        res = 0
        dp  = [[False] * len(str)] * len(str)
        for i in range(len(str)-1, -1, -1):
            for j in range(i, len(str)):
                dp[i][j] = (str[i] == str[j]) and (j - i <= 2 or dp[i + 1][j - 1])
                s.append(str[i:j+1])
                if dp[i][j]:
                    res += 1
        return res,s

# Time complexity O(n^2)
# Space complexity O(n)

#测试实例
if __name__ == '__main__':
    a = Solution2()
    str = "aaa"
    str1 = "abc"
    str2 = "aa"
    print a.countSubstrings(str)
    print a.countSubstrings(str1)
    print a.countSubstrings(str2)