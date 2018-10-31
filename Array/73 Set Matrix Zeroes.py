'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        用一个列表保存存在为0的列
        """
        m,n = len(matrix),len(matrix[0])
        mark = []
        for i in range(m):
            flag = 0
            for j in range(n):
                if matrix[i][j] ==0:
                    flag = 1
                    if j not in mark:
                        mark.append(j)
            if flag ==1:
                matrix[i] = [0 for k in range(n)]

        for j in mark:
            for i in range(m):
                matrix[i][j] = 0
test = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
test.setZeroes(matrix)
print(matrix)
