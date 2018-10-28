class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums,[],res)
        return res
    def dfs(self,nums,path,res):
        if not nums:
            if path not in res:
                res.append(path)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)
