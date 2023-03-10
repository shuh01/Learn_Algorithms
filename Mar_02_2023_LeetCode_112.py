112. Path Sum

Related Topics: Tree, BFS/DFS, Binary Tree

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

First Atempt:

Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, targetSum):
            summ = 0
            stack = [root]
            while len(stack) != 0:
                s = stack.pop()
                if s != None:
                    summ += s.val
                    stack.append(s.right)
                    stack.append(s.left)
                    if s.right == None and s.left == None:
                        if summ == targetSum:
                            return True
                        if summ != targetSum:
                            summ -= s.val
            return False


        return dfs(root, targetSum)
        
 Feedbacks: This code fails to solve problem if pathsum exists at right side of the tree. Since I couldn't figure out this question by myself, I 
 looked up for the suggested solutions.
 
 Suggested Solutions: 
 
 #1. Recursion
 
 Code:
 
 class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        elif not root.left and not root.right:
            if root.val == sum:
                return True
            else:
                return False
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        
#2. DFS

Code:

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root,sum - root.val)]
        while stack:
            u = stack.pop()
            if not u[0].left and not u[0].right:
                if u[1] == 0:
                    return True
            if u[0].left:
                stack.append((u[0].left, u[1]-u[0].left.val))
            if u[0].right:
                stack.append((u[0].right, u[1]-u[0].right.val))
        return False

Feedbacks: Need to work more on dfs/bfs problems. Solve again this problem later.
