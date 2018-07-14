'''
将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：

P   A   H   N
A P L S I I G
Y   I   R
之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"

实现一个将字符串进行指定行数变换的函数:

string convert(string s, int numRows);
示例 1:

输入: s = "PAYPALISHIRING", numRows = 3
输出: "PAHNAPLSIIGYIR"
示例 2:

输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I

方法一：按行排序
思路

通过从左向右迭代字符串，我们可以轻松地确定字符位于 Z 字形图案中的哪一行。

算法



从左到右迭代 s，将每个字符添加到合适的行。可以使用当前行和当前方向这两个变量对合适的行进行跟踪。

只有当我们向上移动到最上面的行或向下移动到最下面的行时，当前方向才会发生改变。
'''


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l = len(s)
        if numRows == 1 or l <= numRows:
            return s
        res = ["" for i in range(numRows)]
        flag1 = 0
        flag2 = 1
        for i in range(l):
            res[flag1] += s[i]
            flag1 += flag2
            if flag1 == numRows - 1 or flag1 == 0:
                flag2 = flag2 * -1
        return ''.join(res)


if __name__=='__main__':
    test = Solution()
    print(test.convert('PAYPALISHIRING',4))