'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"
Example 2:
Input: 4
Output: "1211"
'''


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = '1'
        for _ in range(n - 1):
            num = self.generate_next(num)
        return num

    def generate_next(self, num):
        count = 1
        res = ''
        for i in range(len(num)):
            number_temp = num[i]
            if i < len(num) - 1 and num[i] == num[i + 1]:
                count += 1
            if (i < len(num) - 1 and num[i] != num[i + 1]) or i == len(num) - 1:
                res += str(count)
                res += str(number_temp)
                count = 1
        return res

test = Solution()
input = 2
res =test.countAndSay(2)
print(res)