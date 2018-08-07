'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

先计算第一行以及第一列的路径，其他的路径 grid[i][j] = min(gird[i-1][j],grid[i][j-1])

'''


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        for i in range(1,m):
            grid[i][0]  += grid[i-1][0]
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
test= Solution()
input = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
res = test.minPathSum(input)
print(res)