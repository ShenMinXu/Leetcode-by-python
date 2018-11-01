'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


class Solution:

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n. Make a right turn when the cell ahead is already non-zero.
        """
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            A[i][j] = k + 1
            if A[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A

test = Solution()
n = 3
res =test.generateMatrix(n)
print(res)
