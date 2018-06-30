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
class Solution():
    def countSubstrings(self, str):
        if not str:
            return 0
        res = 0
        for i in range(len(str)):
            j = i
            while  (i >= 0 and j < len(str) and str[i] == str[j]):
                i -= 1
                j += 1
                res += 1

        for i in range(len(str)):
            j = i + 1
            while  (i >= 0 and j < len(str) and str[i] == str[j]):
                i -= 1
                j += 1
                res += 1
        return res

# Time complexity O(n)
# Space complexity O(1)

#测试实例
if __name__ == '__main__':
    a = Solution()
    str = "aaa"
    str1 = "abc"
    str2 = "aa"
    print a.countSubstrings(str)
    print a.countSubstrings(str1)
    print a.countSubstrings(str2)