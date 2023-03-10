116. Populating Next Right Pointers in Each Node

Related Topics: Linked List, Tree, DFS/BFS, Binary Tree

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Example 1:


Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []
         
First Attempt:
         
Code:
         
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def bfs(root):
            visited = []
            tmp = 0
            prev = root
            myqueue = deque()
            myqueue.append((root,0))
            while len(myqueue) != 0:
                curr = myqueue.popleft()
                if curr[0] != None:
                    print(tmp, curr[1],curr[0].val, prev.val)
                    if curr[1] != tmp:
                        tmp += 1
                    else: 
                        prev.next = curr[0]
                    prev = curr[0]
                    if curr[0].left and curr[0].right:
                        myqueue.append((curr[0].left, curr[1]+1))
                        myqueue.append((curr[0].right, curr[1]+1))
                    print(prev.val)
            return root

        return bfs(root)
         
Feedbacks: I tried to use bfs to solve this problem, but there was some logical problem in my code, so it did not work.
         
Second Attempt:
         
Code:
         
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def bfs(root):
            myqueue = deque()
            myqueue.append((root,0))
            tmp = (Node(),0)
            while len(myqueue) != 0:
                count = len(myqueue)
                if count == 1:
                    curr = myqueue.popleft()
                    if curr[0] != None:
                        if curr[0].left and curr[0].right:
                                curr[0].left.next = curr[0].right
                        if curr[0].left:                              
                            myqueue.append((curr[0].left,curr[1]+1))
                        if curr[0].right:
                            myqueue.append((curr[0].right,curr[1]+1))
                else:
                    for i in range(1,count+1):
                        curr = myqueue.popleft()
                        if curr[0] != None:
                            if curr[0].left and curr[0].right:
                                curr[0].left.next = curr[0].right                           
                            if i%2==0 and i!=count:
                                tmp = curr
                            if i%2==1 and tmp[1]==curr[1]:
                                tmp[0].next = curr[0]
                        if curr[0].left:                              
                            myqueue.append((curr[0].left,curr[1]+1))
                        if curr[0].right:
                            myqueue.append((curr[0].right,curr[1]+1))
            return root
        return bfs(root)
            
Feedbacks: I fixed some of my logic from previous code. Since this is a perfect binary tree, which node always has two childs. So, I first all node's
         left child points to its right child. Then, I only need to make right child node which is not the end node to point to next left child node.
         I made a temp node to save right child node if it is not the end node. And I made it to point to another left child node. Problem Solved.
         
