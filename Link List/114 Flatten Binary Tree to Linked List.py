'''
For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

递归地把左子树移到右边
'''


def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    if not root:
        return
    if root.left != None:
        temp = root.right
        root.right = root.left
        root.left = None
        self.flatten(root.right)
        while root.right != None:
            root = root.right
        root.right = temp
    self.flatten(root.right)