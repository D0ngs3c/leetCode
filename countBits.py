#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/counting-bits/description/
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
Credits:
Special thanks to @ syedee for adding this problem and creating all test cases.
'''
'''
   0000    0
-------------
   0001    1
-------------
   0010    1
   0011    2
-------------
   0100    1
   0101    2
   0110    2
   0111    3
-------------
   1000    1
   1001    2
   1010    2
   1011    3
   1100    2
   1101    3
   1110    3
   1111    4

除去前两个数字0个1，从2开始，2和3，是[21, 22)区间的，值为1和2。
而4到7属于[22, 23)区间的，值为1,2,2,3，前半部分1和2和上一区间相同，2和3是上面的基础上每个数字加1。
再看8到15，属于[23, 24)区间的，同样满足上述规律，
  '''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]

        res = [0, 1]
        k = i = 2
        while i <= num:
            for i in range(2**(k-1), 2**k):
                if i > num:
                    break
                tmp = (2**k - 2**(k-1))/2
                if i < (2**(k-1) + tmp):
                    res.append(res[i-tmp])
                else:
                    res.append(res[i-tmp] + 1)
            k += 1
        return res


#递推式：ans[n] = ans[n >> 1] + (n & 1)
class Solution1(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for x in range(1, num + 1):
            ans += ans[x >> 1] + (x & 1),  # x>>1 等价于x/2 , x&1 判断奇偶性：结果1为奇，0为偶。
        return ans

# Time complexity O(n)
# Space complexity O(n)


#递推式：ans[n] = ans[n & (n - 1)] + 1
class Solution2(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for x in range(1, num + 1):
            ans += ans[x & (x - 1)] + 1,
        return ans

# Time complexity O(n)
# Space complexity O(n)


#测试实例
if __name__ == '__main__':
    a = Solution()
    b = Solution1()
    c = Solution2()
    num = 10
    print a.countBits(num)
    print b.countBits(num)
    print c.countBits(num)
