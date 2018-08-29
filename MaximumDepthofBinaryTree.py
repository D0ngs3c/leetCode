#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-29 21:44:12

'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

#DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #DFS
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        res = []
        if root.left:
            res.append(self.maxDepth(root.left))
        if root.right:
            res.append(self.maxDepth(root.right))
        return max(res) + 1
        
#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #BFS
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        depth = 0
        queue = [root, "tag"]
        while len(queue):
            node = queue.pop(0)
            if node == "tag":
                depth += 1
                if len(queue):
                    queue.append("tag")
                continue
            if node.left:
                queue.append(node.left)
                              
            if node.right:
                queue.append(node.right)
        return depth