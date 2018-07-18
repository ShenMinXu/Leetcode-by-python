# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 17:07:18 2018

@author: Administrator

最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"



"""
class Solution:
    def palindrome(self,s,l,r):
        '''
        get the longest palindrome, l, r are the middle indexes   
        from inner to outer
        '''
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.palindrome(s,i,i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.palindrome(s,i,i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    
    
a = Solution()
b=a.longestPalindrome('abbaa')
print(b)
            
       
