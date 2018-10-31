'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row_i,row_j = 0,len(matrix)-1
        col_i,col_j = 0,len(matrix[0])-1
        m_row,m_col = (row_i+row_j)//2,(col_i+col_j)//2
        while m_row <= len(matrix)-1 
            k = matrix[m_row][m_col]
            if k == target:
                return True
            if  k>target:
                print(1)
            elif k<target:
                print(1)
print(3/2)