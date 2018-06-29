#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

#统计一个十进制数的二进制表示中1的个数
#（逐最低位与1进行与运算&，后再往右移一位。直到该数为0）
class Solution():
    def counterbit(self, n):
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>=  1
        return count


#测试实例
if __name__ == '__main__':
    a = Solution()
    n = 5
    print a.counterbit(n)



