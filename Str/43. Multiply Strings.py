'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理

模拟乘法，凤十进一

'''


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        pos = [0]*(m+n)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                sum = mul + pos[p2]

                pos[p1] += sum//10
                pos[p2] = sum % 10
        res = ''
        for p in pos:
            if not (len(res) == 0 and p == 0):
                res = res + str(p)
        if m+n > 0 and res =='':
            return '0'
        return res

test = Solution()
print(test.multiply('22','123'))
