#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. 

Note that the answer must be a substring, "pwke" is a subsequence and not a substring
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

       # 当s长度为0或1时

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        #设置两个指针 一个从0开始指向子字符串的起始位置  另一个从1开始（s[0,1]就是第一个子字符串）向后遍历
        beginPointer = 0
        endPointer = 1
        #设置一个res存储结果
        res = 0

        while endPointer < len(s):
            index = s.find(s[endPointer], beginPointer, endPointer)

            if index != -1:  # 如果endPointer指向的字符在之前的字串中
                res = max(res, endPointer - beginPointer)
                beginPointer = index + 1 #这里beginPointer直接指向index+1 例如'abcdefdh'，
                                         # 遍历第一遍得到'abcdef'，如果从b开始遍历获得'bcdef' 肯定比之前短
                                         # 所以我们直接跳到重复字符d的下一个e开始遍历

            endPointer = endPointer + 1

        #遍历到s中最后一个字符也没有出现重复的情况（即 最后一个没有重复字母的子字符串）
        if s.find(s[len(s) - 1], beginPointer, len(s) - 1) == -1:
            return max(res, len(s) - beginPointer)

        return res
#测试
if __name__ == '__main__':
    a = Solution()
    s1 = 'abcabcbb'
    s2 = 'bbbbbb'
    s3 = 'pwwkew'
    print a.lengthOfLongestSubstring(s1)
    print a.lengthOfLongestSubstring(s2)
    print a.lengthOfLongestSubstring(s3)