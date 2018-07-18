# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

3. 无重复字符的最长子串
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。

"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_str = ""
        longest_count = 0
        for ch in s:
            if ch not in sub_str:
                sub_str += ch
            else:
                if len(sub_str) > longest_count:
                    longest_count = len(sub_str)
                sub_str = sub_str[sub_str.find(ch)+1:] + ch
                
        if len(sub_str) > longest_count:
            longest_count = len(sub_str)
            
        return longest_count
    


a = Solution()

b = a.lengthOfLongestSubstring('abc')
print(b)