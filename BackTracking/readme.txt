回溯法中，首先需要明确下面三个概念：

约束函数：约束函数是根据题意定出的。通过描述合法解的一般特征用于去除不合法的解，从而避免继续搜索出这个不合法解的剩余部分。因此，约束函数是对于任何状态空间树上的节点都有效、等价的。

状态空间树：刚刚已经提到，状态空间树是一个对所有解的图形描述。树上的每个子节点的解都只有一个部分与父节点不同。

扩展节点、活结点、死结点：所谓扩展节点，就是当前正在求出它的子节点的节点，在DFS中，只允许有一个扩展节点。活结点就是通过与约束函数的对照，节点本身和其父节点均满足约束函数要求的节点；死结点反之。由此很容易知道死结点是不必求出其子节点的（没有意义）。

为什么用DFS
深度优先搜索（DFS）和广度优先搜索（FIFO）在分支界限法中，一般用的是FIFO或最小耗费搜索；其思想是一次性将一个节点的所有子节点求出并将其放入一个待求子节点的队列。通过遍历这个队列（队列在 遍历过程中不断增长）完成搜索。而DFS的作法则是将每一条合法路径求出后再转而向上求第二条合法路径。而在回溯法中，一般都用DFS。为什么呢？这是因 为可以通过约束函数杀死一些节点从而节省时间，由于DFS是将路径逐一求出的，通过在求路径的过程中杀死节点即可省去求所有子节点所花费的时间。FIFO 理论上也是可以做到这样的，但是通过对比不难发现，DFS在以这种方法解决问题时思路要清晰非常多。

回溯法可以被认为是一个有过剪枝的DFS过程，利用回溯法解题的具体步骤。
首先，要通过读题完成下面三个步骤：
(1) 描述解的形式，定义一个解空间，它包含问题的所有解。
(2) 构造状态空间树。
(3) 构造约束函数（用于杀死节点）。

然后就要通过DFS思想完成回溯，完整过程如下：
(1) 设置初始化的方案（给变量赋初值，读入已知数据等）。
(2) 变换方式去试探，若全部试完则转(7)。
(3) 判断此法是否成功（通过约束函数），不成功则转(2)。
(4) 试探成功则前进一步再试探。
(5) 正确方案还未找到则转(2)。
(6) 已找到一种方案则记录并打印。
(7) 退回一步（回溯），若未退到头则转(2)。
(8) 已退到头则结束或打印无解。

回溯方法的步骤如下：

定义一个解空间，它包含问题的解。
用适于搜索的方式组织该空间。
用深度优先法搜索该空间，利用限界函数避免移动到不可能产生解的子空间。