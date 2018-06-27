#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

# 最大连续子序列乘积
# 题目描述：
# 给一个浮点数序列，取最大乘积连续子串的值，例如 -2.5，4，0，3，0.5，8，-1，则取出的最大乘积连续子串为3，0.5，8。也就是说，上述数组中，3 0.5 8这3个数的乘积30.58=12是最大的，而且是连续的。

# 分析：
# 若暴力求解，需要O(n^3)时间，太低效。
# 故使用动态规划:
# 设data[i]：第i个数据，dp[i]:以第i个数结尾的连续子序列最大乘积，
# 若题目要求的是最大连续子序列和，则易确定状态转移方程为：
# dp[i]=max(data[i]，dp[i-1]+data[i])(dp[i]为以第i个数结尾的连续子序列最大和)<br>
# 但乘积存在负负得正的问题，即原本很小的负数成了一个负数反而变大了，（负数逆袭了），

# 故不能照抄加法的转移方程，为了解决这个问题，需要定义两个数组：
# dp1[i]:以第i个数结尾的连续子序列最大乘积<br>
# dp2[i]:以第i个数结尾的连续子序列最小乘积
# 转移方程:<br>
# dp1[i]=max(data[i],dp1[i-1]*data[i],dp2[i-1]*data[i]);<br>
# dp2[i]=min(data[i],dp1[i-1]*data[i],dp2[i-1]*data[i]);

# 最后遍历dp1得到最大值即为答案。


class Solution:
    def MaxProductSubstring(self,a):
        if len(a) == 1 :
            return a[0]
        if  not a:
            return None
        dp1 = a[0]
        dp2 = a[0]
        ans = a[0]
        n = len(a)
        # i = 1
        for i in range(1,n):
            dpmax = max(a[i], max(dp1 * a[i], dp2 * a[i]))
            dpmin = min(a[i], min(dp1 * a[i], dp2 * a[i]))

            dp1 = dpmax
            dp2 = dpmin
            ans = dp1 if dp1 > ans else ans
        return ans

           
#测试
if __name__ == '__main__':
    a = Solution()
    s1 = [-2.5,4,0,3,0.5,8,-1]
    s2 = [-2.5]
    s3 = []
    print a.MaxProductSubstring(s1)
    print a.MaxProductSubstring(s2)
    print a.MaxProductSubstring(s3)

