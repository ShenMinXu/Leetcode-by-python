'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res= []
        self.help(candidates,target,[],-1,res)
        return res
    def help(self,nums,target,path,index,res):
        if target == 0:
            res.append(path)
        if target < 0:
            return
        for i in range(index+1,len(nums)):
            if i>index+1 and nums[i] == nums[i - 1]:
                continue
            self.help(nums,target-nums[i],path+[nums[i]],i,res)

test = Solution()
candidates = [10,1,2,7,6,6,1,5]
target = 8
res = test.combinationSum2(candidates,target)
print(res)










