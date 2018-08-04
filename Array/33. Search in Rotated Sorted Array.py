'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
二分法，先判断中值是属于哪边的升序序列，再根据端点值继续判断 target 该落在左边还是右边区域
'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[start]:  # 当nums[mid]属于左边升序序列时

                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            if nums[mid] < nums[end]:  # 当nums[mid]属于右边升序序列时

                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

test = Solution()
input = [4,5,6,7,0,1,2]
res = test.search(input,target=0)
print(res)