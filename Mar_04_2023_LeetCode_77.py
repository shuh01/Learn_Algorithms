77. Combinations

Related Topics: Backtracking

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.

*Backtracking Pseudocode:*

void findSolutions(n, other params) :
    if (found a solution) :
        solutionsFound = solutionsFound + 1;
        displaySolution();
        if (solutionsFound >= solutionTarget) : 
            System.exit(0);
        return

    for (val = first to last) :
        if (isValid(val, n)) :
            applyValue(val, n);
            findSolutions(n+1, other params);
            removeValue(val, n);
            
First Attempt:

Code:

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def combi(remain, comb, next):
            if remain == 0:
                ans.append(comb.copy())
            else:
                for i in range(next, n+1):
                    comb.append(i)
                    combi(remain-1, comb, i+1)
                    comb.pop()
        combi(k, [], 1)
        return ans
        
Feedbacks: Need to solve this problem again. Need to get used to backtracking algorithm.        
