'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]



'''


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def search(n):
            #二分查找从左至右第一个出现的target
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        lo = search(target)
        return [lo, search(target + 1) - 1] if target in nums[lo:lo + 1] else [-1, -1] #找到比targe大一的左边那个，再减1就得到最右边那个

test = Solution()
input = [1]
res = test.searchRange(input,target=1)
print(res)