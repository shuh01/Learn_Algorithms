226. Invert Binary Tree

Related Topics: Tree, BFS/DFS, Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
  
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
  
Example 3:

Input: root = []
Output: []
  
---------------------------------------------------
  
First Attempt:
  
Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        newroot = root
        visited=[]
        def dfs(root):
            stack = [root]
            while len(stack) != 0:
                s = stack.pop()
                if s!= None:
                    if s.val not in visited:
                        visited.append(s.val)
                        stack.append(s.left)
                        stack.append(s.right)
            # print(visited)
        newvisited=[]
        def change(newroot):
            count = 0
            stack = [newroot]
            while len(stack) != 0:
                s = stack.pop()
                if s!= None:
                    s.val = visited[count]
                    if s.val not in newvisited:
                        newvisited.append(s.val)
                        stack.append(s.right)
                        stack.append(s.left)
                    count+=1
            # print(newvisited)


        
        dfs(root)
        change(newroot)
        return newroot
      
Feedbacks: I first tried to solve this question with DFS iterative, but it could not be working becuase I made a duplicate of a tree, and if I
make changes on one tree, same changes are maken to another tree also. So I concluded that I should use recursion to solve this problem.

---------------------------------------------------

Second Attempt:
  
Code:
  
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root:
                tmp = root.left
                root.left = root.right
                root.right = tmp
                if root.left != None:
                    dfs(root.left)
                if root.right != None:
                    dfs(root.right)
        dfs(root)
        return root
      
Feedbacks: I used recursion this time. And I could solve this problem very easily. I should work on more DFS questions, so I can determine well
whether I should use recursion or iterative methods.
  
