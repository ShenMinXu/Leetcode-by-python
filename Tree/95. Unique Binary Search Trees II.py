'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.dfs(1, n)
    def dfs(self, start, end):
        if start > end: return [None]
        res = []
        for rootval in range(start, end + 1):# rootval为根节点的值，从start遍历到end
            LeftTree = self.dfs(start, rootval - 1)
            RightTree = self.dfs(rootval + 1, end)
            for i in LeftTree:  # i遍历符合条件的左子树
                for j in RightTree: # j遍历符合条件的右子树
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res


test = Solution()
res = test.generateTrees(5)
print(res)
print(len(res))