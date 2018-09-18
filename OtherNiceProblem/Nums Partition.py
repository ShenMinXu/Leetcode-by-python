'''
数组 (分段和) 的 (最大值) 最小问题
题目
题目：给定一个数组，和一个值k，数组分成k段。要求这k段子段和最大值最小。求出这个值。

题目分析：算法1，暴力搜索。本题暴力搜索算法并不是很明显，可以使用递归实现暴力搜索。递归首先要有递归式：

M[n,k]=minj=1n(max{M[j,k−1],∑i=jnAi})

n表示数组长度，k表示数组分成几段。初始化条件：

M[1,k]=A0

M[n,1]=∑i=0n−1Ai

很容易发现上述的递归算法拥有指数时间的复杂度，并且会重复计算一些M值。这类的算法一般可以使用动态规划进行优化。使用数组保存一些已经计算得到
的值，采用从低向上进行计算。这就是算法2。文章中还给出了第三种很牛的算法，我是想不到的。这就是使用二分查找应用到这个题目。大牛真是太牛了！！
下面是代码：
'''
def sum(A,form,to):
    total = 0
    for i in range(form,to+1):
        total +=A[i]
    return total
def partition(A,n,k):
    if (k == 1):
        return sum(A, 0, n-1)
    if (n == 1):
        return A[0]
    best = 99999
    for j in range(1,n):
        best = min(best, max(partition(A, j, k-1), sum(A, j, n-1)));

    return best;

A = [10,20,30,40,50,60,70,80,90]
n = len(A)
k  = 3
res = partition(A,n,k)
print(res)


'''
/改进的动态规划算法
//时间复杂度：O(kN2)
//空间复杂度：O(kN) 
const int MAX_N = 100; 
int findMax(int A[], int n, int k) { 
    int M[MAX_N+1][MAX_N+1] = {0}; 
    int cum[MAX_N+1] = {0}; 
    for (int i = 1; i <= n; i++) 
        cum[i] = cum[i-1] + A[i-1]; 

    for (int i = 1; i <= n; i++) 
        M[i][1] = cum[i]; 
    for (int i = 1; i <= k; i++) 
        M[1][i] = A[0]; 

    for (int i = 2; i <= k; i++) { 
        for (int j = 2; j <= n; j++) { 
            int best = INT_MAX; 
            for (int p = 1; p <= j; p++) { 
                best = min(best, max(M[p][i-1], cum[j]-cum[p])); 
            } 
            M[j][i] = best; 
        } 
    } 
    return M[n][k]; 
}


int getMax(int A[], int n) { 
    int max = INT_MIN; 
    for (int i = 0; i < n; i++) { 
        if (A[i] > max) max = A[i]; 
    } 
    return max; 
} 

int getSum(int A[], int n) { 
    int total = 0; 
    for (int i = 0; i < n; i++) 
        total += A[i]; 
    return total; 
} 

int getRequiredPainters(int A[], int n, int maxLengthPerPainter) { 
    int total = 0, numPainters = 1; 
    for (int i = 0; i < n; i++) { 
        total += A[i]; 
        if (total > maxLengthPerPainter) { 
            total = A[i]; 
            numPainters++; 
        } 
    } 
    return numPainters; 

'''

'''

二分查找
二分查找法分析
自己的分析：此题可以想象成把数据按顺序装入桶中，m即是给定的桶数，问桶的容量至少应该为多少才能恰好把这些数装入k个桶中（按顺序装的）。

首先我们可以知道，桶的容量最少不会小于数组中的最大值，即桶容量的最小值（小于的话，这个数没法装进任何桶中），假设只需要一个桶，那么其容量应该是数组所有元素的和，即桶容量的最大值；其次，桶数量越多，需要的桶的容量就可以越少，即随着桶容量的增加，需要的桶的数量非递增的（二分查找就是利用这点）；我们要求的就是在给定的桶数量m的时候，找最小的桶容量就可以把所有的数依次装入k个桶中。在二分查找的过程中，对于当前的桶容量，我们可以计算出需要的最少桶数requiredPainters，如果需要的桶数量大于给定的桶数量k，说明桶容量太小了，只需在后面找对应的最小容量使需要的桶数恰好等于k；如果计算需要的桶数量小于等于k，说明桶容量可能大了（也可能正好是要找的最小桶容量），不管怎样，该桶容量之后的桶容量肯定不用考虑了（肯定大于最小桶容量），这样再次缩小查找的范围，继续循环直到终止，终止时，当前的桶容量既是最小的桶容量。

对于数组 1 2 3 4 5 6 7，假设k=3，最小桶容量为7（要5个桶），最大桶容量为28（一个桶）

单桶容量	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26
桶数量	    5	5	4	4	3	3	3	3	2	2	2	2	2	2	2	2	2	2	2	2
第一行表示桶容量，第二行表示需要的桶数
即要求桶数量恰为k的最小桶容量；

因为桶数量增加时，桶容量肯定减小（可以想象把装的最多的桶拆成两个桶，那么装的第二多的桶就变成了之后的桶容量），所以找对应k的最小容量；

'''
'''
int getMax(int A[], int n) { 
    int max = INT_MIN; 
    for (int i = 0; i < n; i++) { 
        if (A[i] > max) max = A[i]; 
    } 
    return max; 
} 

int getSum(int A[], int n) { 
    int total = 0; 
    for (int i = 0; i < n; i++) 
        total += A[i]; 
    return total; 
} 

int getRequiredPainters(int A[], int n, int maxLengthPerPainter) { 
    int total = 0, numPainters = 1; 
    for (int i = 0; i < n; i++) { 
        total += A[i]; 
        if (total > maxLengthPerPainter) { 
            total = A[i]; 
            numPainters++; 
        } 
    } 
    return numPainters; 
} 


//想不到的二分查找算法
//时间复杂度：O(N log ( ∑ Ai )).
//空间复杂度：0(1)
int BinarySearch(int A[], int n, int k) { 
    int lo = getMax(A, n); 
    int hi = getSum(A, n); 

    while (lo < hi) { 
        int mid = lo + (hi-lo)/2; 
        int requiredPainters = getRequiredPainters(A, n, mid); 
        if (requiredPainters <= k) 
            hi = mid; 
        else
            lo = mid+1; 
    } 
    return lo; 
}
int main()
{
    enum{length=9};
    int k=3;
    int a[length]={9,4,5,12,3,5,8,11,0};
    cout<<partition(a,length,k)<<endl;
    cout<<findMax(a,length,k)<<endl;
    cout<<BinarySearch(a,length,k)<<endl;
    return 0;
}
'''