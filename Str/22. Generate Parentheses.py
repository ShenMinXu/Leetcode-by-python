'''
22. 括号生成
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.helper(res, 1, 0, n, "(")
        return res

    def helper(self, res, i, j, n, path):
        if i > n:
            return

        if i == n and j == n:
            res.append(path)
            return

        elif i > j:
            self.helper(res, i + 1, j, n, path + "(")
            self.helper(res, i, j + 1, n, path + ")")

        elif i == j:
            self.helper(res, i + 1, j, n, path + "(")