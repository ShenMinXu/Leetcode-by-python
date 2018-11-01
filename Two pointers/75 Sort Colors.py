'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
'''


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.

        三个个指针，一个i从前往后，一个j从后往前，遇到0和i换，遇到2和j换
        """
        i = 0
        j = len(nums)-1
        key = 0
        while key<=j:
            if nums[key] ==0:
                nums[key],nums[i] = nums[i],nums[key]
                i += 1
                key += 1
            elif nums[key] == 1:
                key +=1
            else:
                nums[key],nums[j] = nums[j],nums[key]
                j -= 1
        return nums




test = Solution()
a =  [2,0,1]
res = test.sortColors(a)
print(res)
