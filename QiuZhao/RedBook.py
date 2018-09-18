#给定层序遍历和中序遍历，返回叶子节点，前序遍历，后序遍历
order = [3,5,4,2,6,7,1]
middle = [2,5,3,6,4,7,1]

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def construct_tree(pre_order, mid_order):
    # 忽略参数合法性判断
    if len(pre_order) == 0 or len(pre_order) != len(mid_order):
        return None
    # 前序遍历的第一个结点一定是根结点
    root_data = pre_order[0]
    i = mid_order.index(root_data)
    # 递归构造左子树和右子树
    left_tree = mid_order[:i]
    right_tree = mid_order[i+1:]
    left = construct_tree([each for each in order if each in left_tree],mid_order[:i])
    right = construct_tree([each for each in order if each in right_tree], mid_order[i+1:])
    return Node(root_data, left, right)

def getleaf(r,res):
    if not r.left and not r.right:
        res.append(r.data)
    if r.left:
        getleaf(r.left,res)
    if r.right:
        getleaf(r.right,res)
    return res

def preOrder(r,res):
    if r == None:
        return
    # 先打印根结点，再打印左结点，后打印右结点
    res.append(r.data)
    preOrder(r.left,res)
    preOrder(r.right,res)
    return res

def backOrder(r,res):
    if r == None:
        return
    # 先打印根结点，再打印左结点，后打印右结点
    backOrder(r.left,res)
    backOrder(r.right,res)
    res.append(r.data)
    return res
root = construct_tree(order , middle)
leaf = getleaf(root,[])
leaf = list(map(str,leaf))
print(' '.join(leaf))
preorder = preOrder(root,[])
preorder = list(map(str,preorder))
print(' '.join(preorder))
backorder = backOrder(root,[])
backorder  = list(map(str,backorder ))
print(' '.join(backorder))