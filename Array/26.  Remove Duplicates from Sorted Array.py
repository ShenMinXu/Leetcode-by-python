'''
Given a sorted array, remove the duplicates in place such that each element appear only once
and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example, Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]

'''
class Solution:#时间复杂度 O(n)，空间复杂度 O(1)
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        index = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[index]:
                index +=1
                nums[index] = nums[i]
        return index+1
