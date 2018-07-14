'''
11. 盛最多水的容器
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。画 n 条垂直线，使得垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

注意：你不能倾斜容器，n 至少是2。
如题意，垂直的两条线段将会与坐标轴构成一个矩形区域，较短线段的长度将会作为矩形区域的宽度，两线间距将会作为矩形区域的长度，而我们必须最大化该矩形区域的面积。

max(min(ai,aj)*(aj-ai))

方法二：双指针法
算法

这种方法背后的思路在于，两线段之间形成的区域总是会受到其中较短那条长度的限制。此外，两线段距离越远，得到的面积就越大。

我们在由线段长度构成的数组中使用两个指针，一个放在开始，一个置于末尾。 此外，我们会使用变量 maxareamaxarea 来持续存储到目前为止所获得的最大面积。 在每一步中，我们会找出指针所指向的两条线段形成的区域，更新 maxareamaxarea，并将指向较短线段的指针向较长线段那端移动一步。
'''


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        timpe O(n)
        space O(1)
        """
        i = 0
        j = len(height)-1
        area = (j-i)*min(height[i],height[j])
        while i<j:
            if height[i] <= height[j]:
                i+=1
            else:
                j-=1
            area = max(area,(j-i)*min(height[i],height[j]))
        return area