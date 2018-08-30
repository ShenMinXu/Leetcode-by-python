'''
3. 小a和小b玩一个游戏，有n张卡牌，每张上面有两个正整数x，y。取一张牌时，个人积分增加x，团队积分增加y。求小a，小b各取若干张牌，使得他们的个人积分相等，且团队积分最大。

输入描述：

第一行n

接下来n行，每行两个正整数x，y

输出描述：

一行一个整数

表示小a的积分和小b的积分相等时，团队积分的最大值

例：输入

4

3 1

2 2

1 4

1 4

输出：10

说明：当a抽取（2,2），b抽取（1,4），（1,4）时，两人个人积分都是2，团队积分最大，为10分

https://blog.csdn.net/XX_123_1_RJ/article/details/81808305
# dp状态转换方程如下：

dp[i][j]=max(d[i-1][j], d[i-1][j-x[i-1]) + y[i-1], d[i-1][j+x[i-1]] + y[i-1])

# dp[i][j]表示前 i 张卡牌中，且两人得分的差为 j 时团队得分的最大值
'''

class Solution():
    def maxscore(self,n,x,y):
        '''

        :param n:卡片数
        :param x:卡片个人分 list
        :param y:卡片团队分 list
        :return:
        '''
        mx = max(x)  # 获取最大值，作为差的边界

        dp = [[0] * (mx + 1) for _ in range(n + 1)]  # 初始化dp

        for i in range(1, n + 1):
            for j in range(mx + 1):
                tmp1, tmp2 = 0, 0
                if j - x[i - 1] >= 0:  # 这张卡牌给小a
                    tmp1 = dp[i - 1][j - x[i - 1]] + y[i - 1]

                if j + x[i - 1] <= mx:  # 这张卡牌给小b
                    tmp2 = dp[i - 1][j + x[i - 1]] + y[i - 1]

                dp[i][j] = max(dp[i - 1][j], tmp1, tmp2)  # 三种状态的最高得分

                if i == 1 and j == 0:  # 只有一张卡牌时
                    dp[i][j] = 0
        return dp[n][0]

if __name__ == '__main__':
    test = Solution()
    n = 4
    x = [3, 2, 1, 1]
    y = [1, 2, 4, 4]
    print(test.maxscore(n, x, y))