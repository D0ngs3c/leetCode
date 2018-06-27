#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

# 交替字符串
# 题目描述：
# 输入三个字符串 s1、s2 和 s3，判断第三个字符串 s3 是否由前两个字符串 s1 和 s2 交错而成，
# 即不改变 s1 和 s2 中各个字符原有的相对顺序。
# 例如当 s1 = “aabcc”，s2 = “dbbca”，s3 =“aadbbcbcac”时，则输出 true，
# 但如果 s3=“accabdbbca”，则输出 false。

# 动态规划分析与解法：
# 定义dp[i,j]表示s3[1...i+j]是否由s1[1...i]和s2[1...j]的字符组成：即dp[i,j]取值范围为true/false。
# 下面思考dp[i,j]如何才能取true呢？
# 1、若dp[i-1,j]==true，并且s1[i]==s3[i+j]，那么，dp[i,j]可以取true；
# 2、若dp[i,j-1]==true，并且s2[j]==s3[i+j]，那么，dp[i,j]可以取true；
# 3、其余情况，dp[i,j]只能取false；
# 4、此外，dp[0,0]初始化为true，表示当空串s1和空串可以合成空串s3；


class Solution:
    def IsInterleave(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)

        #s1和s2的长度和不等于s3，即合成失败。
        if (l1 + l2) != l3:
            return False

        # list3=[[""]*Width]*Height 二维数组初始化    
        dp = [[""] * (l1+1)] * (l2+1) 

        #认为空串为两个空串合成
        dp[0][0] = True 

        for i in range(l1):
            for j in range(l2+1):
                    #取s1字符串
                if ((i >= 0 and dp[i-1][j] and s1[i] == s3[i+j]) or 
                    #取s2字符串
                    (j >= 0 and dp[i][j-1] and s2[j-1] == s3[i+j])):

                    dp[i][j] = True
                else:
                    dp[i][j] = False

        return dp[l1][l2]



#测试实例
if __name__ == '__main__':
    a = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s4 = "accabdbbca"
    print a.IsInterleave(s1, s2, s3)
    print a.IsInterleave(s1, s2, s4)
    