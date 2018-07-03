#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-03 21:27:16
# @Version : $python2.7$

'''
https://leetcode.com/problems/maximum-length-of-pair-chain/description/

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.
Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
'''
'''
由于规定了链对的首元素一定小于尾元素，我们需要比较的是某个链表的首元素和另一个链表的尾元素之间的关系，
如果整个链对数组是无序的，那么就很麻烦，所以我们需要做的是首先对链对数组进行排序，按链对的尾元素进行排序，小的放前面。
这样我们就可以利用Greedy算法进行求解了。
我们可以用一个栈，先将第一个链对压入栈，然后对于后面遍历到的每一个链对，
我们看其首元素是否大于栈顶链对的尾元素，
如果大于的话，就将当前链对压入栈，这样最后我们返回栈中元素的个数即可，
'''
#Greedy(贪婪算法)
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        stack = []
        l = len(pairs)
        pairs.sort(key=lambda x: x[-1])

        for i in range(l):
            if stack == []:
                stack.append(pairs[i])
            else:
                top = stack[-1]
                if pairs[i][0] > top[-1]:
                    stack.append(pairs[i])
        return len(stack)

# Time complexity O(n)
# Space complexity O(len(stack))
#测试实例
if __name__ == '__main__':
    a = Solution()
    b = [[1,2], [2,3], [3,4]]
    print a.findLongestChain(b)

