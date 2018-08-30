'''
4. 两个长度为n的序列a，b。问有多少个区间[l，r]满足max(a[l,r])<min(b[l,r])即a区间的最大值小于b区间的最小值数据范围：n<1e5，a(i),b(i)<1e9

输入描述：

第一行一个整数n

第二行n个数，第i个为a(i)

第三行n个数，第i个为b(i)

0<1<=r<n

输出描述：

一行一个整数，表示答案

例1：输入

3

3 2 1

3 3 3

输出： 3
对两个区间从左到右进行扫描，分别维护一个左端扫描起始位置和右端扫描结束位置以及a的最大值和b的最小值。
期初两个标记都在I处，然后开始移动右端flag，
每移动一个位置只需要将最大值和最小值和该位置的值做判断，直到该区间的a的最大值大于等于b的最小值时，
左端flag向右移动一个位置，右端flag回到此时左端flag的位置，以此类推直到r处。

'''

class Solution():
    def getres(self,list1,list2):
        l = 0
        r = 0
        res = 0
        while l < len(list1):
            while max(list1[l:r+1])<min(list2[l:r+1]) and r<len(list1):
                res += 1
                r += 1

            l+=1
            r = l
        return res

test = Solution()
list1 = [3,2,1]
list2 = [3,3,3]
res = test.getres(list1,list2)
print(res)



