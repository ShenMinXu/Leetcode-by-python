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
        先对行二分查找出元素所在范围，再对列二分查找
        Runtime: 40 ms, faster than 91.89% of Python3 online submissions for Search a 2D Matrix.
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False
        row_i,row_j = 0,len(matrix)-1
        col_i,col_j = 0,len(matrix[0])-1
        while row_i<=row_j:
            m_row = (row_i+row_j)//2
            print(m_row)
            if matrix[m_row][0] > target:
                row_j = m_row-1
            elif matrix[m_row][-1]< target:
                row_i = m_row+1
            else:
                break
        if row_i > row_j:
            return False
        while col_i<=col_j:

            m_col  =(col_j+col_i)//2
            print(m_col)
            if matrix[m_row][m_col] == target:
                return True
            elif matrix[m_row][m_col] >target:
                col_j = m_col-1
            elif matrix[m_row][m_col] <target:
                col_i = m_col+1
        return False



test = Solution()
matrix = [[1]]
target = 0
res = test.searchMatrix(matrix,target)
print(res)
