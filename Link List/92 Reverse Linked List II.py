'''
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.
Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        Runtime: 36 ms, faster than 94.16% of Python3 online submissions for Reverse Linked List II.
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        for i in range(m - 1):
            p = p.next
        s = p.next
        sh = p.next
        f = s.next  # sh record the head of the [m,n] part, s and f completes the reverse
        for i in range(n - m):
            t = f.next
            f.next = s
            s = f
            f = t
        p.next = s
        sh.next = f
        return dummy.next