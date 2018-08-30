'''
5、小明在抖音里关注了N个主播，每个主播每天的开播时间是固定的，分别在S时刻开始开播，t时间结束。小明无法同时观看两个主播的直播。一天被分成了M个时间单位。请问小明每天最多能完整观看多少场直播？

输入描述：
第一行一个整数，代表N
第二行一个整数，代表M
第三行空格间隔的N*2个整数，代表s，t
输出描述：
一行一个整数，表示答案
例1：输入
3
10
0 3 3 7 7 0
输出：3
例2： 输入
3
10
0 5 2 7 6 9
输出：2
备注：数据范围1<=N<=10^5
2<=M<=10^6
0<=s(i),t(i)<M (s(i)!=t(i))
s(i)>t(i)代表时间跨天，但直播时长不会超过一天

这题的思路使用动态规划，同时维护过去区间的时间跨度
dp[i] =  1+dp[ timespan(i) 不与i冲突]如果冲突，则从后向前找一直找到不冲突的为止
'''

class Solution():
    def getres(self,N,M,st):
        '''

        :param N:N个主播
        :param M:一天分为M个时间单位
        :param st:第三行空格间隔的N*2个整数，代表s，t，s表示直播开始时间，t表示结束时间
        :return:
        '''
        Nlist = [(st[i],st[i+1]) for i in range(0,N*2,2)]
        Nlist.sort()
        res = [[0,0] for i in range(N)]
        res[0] = [1,Nlist[0][1]]
        print(res)
        for i in range(1,N):
            if Nlist[i][0] >= res[i-1][1]:
                res[i][0] = res[i-1][0]+1
                res[i][1] = Nlist[i][1]
            else:
                res[i][0] = res[i - 1][0]
                res[i][1] = Nlist[i-1][1]
        print(res[-1][0])
        return res[-1][0]




test = Solution()
N = 3
M = 10
st = [0,5,2,7,6,9]
res = test.getres(N,M,st)
print(res)