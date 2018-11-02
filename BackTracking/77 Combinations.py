'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        Runtime: 1092 ms, faster than 13.07% of Python3 online submissions for Combinations.
        """
        nums = [i+1 for i in range(n)]
        res = []
        self.help(k,nums,[],res)
        return res
    def help(self,k,nums,path,res):
        if k ==0:
            res.append(path)
        else:
            for i in range(len(nums)):
                self.help(k-1,nums[i+1:],path+[nums[i]],res)



class Solution2:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        Runtime: 128 ms, faster than 95.34% of Python3 online submissions for Combinations.
        当x大于n时弹出上一个末尾值+1
        """
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1


test = Solution2()
n = 6
k = 2
res = test.combine(n,k)
print(res)

