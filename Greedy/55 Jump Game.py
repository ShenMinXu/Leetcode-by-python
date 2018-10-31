'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Going forwards. m tells the maximum index we can reach so far.
        """
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True


class Solution:
    '''
    Going backwards, most people seem to do that, here's my version.
    '''
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal





test = Solution()
a  = [3,2,1,0,4]
res =test.canJump(a)
print(res)

for i in range(5)[::-1]:
    print(i)