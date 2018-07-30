#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Version : $python2.7$

'''
https://leetcode.com/problems/stone-game/description/

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.
Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:
Input: [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

Note:
2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
'''

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        su = sum(piles)
        ma,mi = {},{}
        def getmax(i,j):
            if i==j: 
                return piles[i]
            if (i,j) in ma: 
                return ma[(i,j)]

            ma[(i,j)] = max(piles[i]+getmin(i+1,j), piles[j]+getmin(i,j-1))
            return ma[(i,j)]
        def getmin(i,j):
            if i==j: 
                return 0
            if (i,j) in mi: 
                return mi[(i,j)]

            mi[(i,j)] = min(getmax(i+1,j), getmax(i,j-1))
            return mi[(i,j)]
        
        return  getmax(0,len(piles)-1)>su//2


#测试实例
if __name__ == '__main__':
    piles = [5,3,4,5]
    a = Solution()

    print a.stoneGame(piles)
