'''
Follow up for ” 26Remove Duplicates”: What if duplicates are allowed at most twice?
For example, Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3]
加一个变量记录一下元素出现的次数即可。这题因为是已经排序的数组，所以一个变量即可解
决。如果是没有排序的数组，则需要引入一个 hashmap 来记录出现次数。
'''


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for n in nums:
            if index < 2 or n > nums[index - 2]:
                nums[index] = n
                index += 1
        return index

test  =Solution()
input = [0,0,1,1,1,1,2,3,3]
res =test.removeDuplicates(input)
print(res)
print(input)