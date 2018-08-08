'''
Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree.
For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
根据二叉树的前序和中序遍历结果，反推这个树，假设只有一个这样的树。
先序遍历：遍历顺序规则为【根左右】
中序遍历：遍历顺序规则为【左根右】
后序遍历：遍历顺序规则为【左右根】
通过先序遍历和中序遍历、中序遍历和后序遍历 是可以还原该二叉树结构的。
1因为先序中的节点为根节点,所以取出先序的第一个节点
2用先序的第一个节点可以将中序分成左右子树，然后取出先序的第二个节点将左右子树再次划分
3当将中序全部划分为单个点时就结束
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        return self.dfs(pbegin=0, pend=len(preorder), ibegin=0, iend=len(inorder))
    def dfs(self,pbegin, pend, ibegin, iend):
        '''
        :param pbegin:前序开始节点
        :param pend: 前序结束节点
        :param ibegin: 中序开始结点
        :param iend: 中序结束节点
        :return:
        '''
        if pbegin >= pend:
            return None
        if pbegin + 1 == pend:
            return TreeNode(self.preorder[pbegin])
        i = self.inorder.index(self.preorder[pbegin]) #找到pbegin在中序中的位置
        i = i - ibegin #计算中序起始点移动多少距离为根节点
        ans = TreeNode(self.preorder[pbegin])
        ans.left = self.dfs(pbegin + 1, pbegin + i + 1, ibegin, ibegin + i)
        ans.right = self.dfs(pbegin + i + 1, pend, ibegin + 1 + i, iend)
        return ans



test= Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
res = test.buildTree(preorder,inorder)
print(res)