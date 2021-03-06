'''
py3.5
谷歌扔鸡蛋
题目：有一个100层高的大厦，你手中有两个相同的鸡蛋。从这个大厦的某一层扔下鸡蛋就会碎，
用你手中的这两个鸡蛋，提出一个策略, 要保证能测出鸡蛋恰好会碎的楼层, 并使此策略在最坏情况下所扔次数最少
动态规划
1）最坏情况下所扔次数最少。比較绕口。想表达的意思是。在不明白知道哪一层会碎的情况下。要找到一种策略，通过最少的试验次数，得到临界楼层（恰好不会碎的楼层）。不明白知道。就须要考虑最糟糕的情况，并且这样的策略与其它策略相比是最糟糕的情况下，最少的试验次数。
2）假设一种扔法：第一个鸡蛋，从50楼扔下去。

假设碎了，第二个鸡蛋必须从1~49层逐层试验。假设第i层为临界层。且i≤49，这个时候，要试验的总次数是1 +（i - 1）。由于必须保证在没找到临界楼层之前，鸡蛋不能碎。假设没碎，则第一个鸡蛋能够接着从75层扔。

由于即使这次碎了，还有个鸡蛋，能够继续逐层试验。对第一个鸡蛋的继续从中间分，就比較合理。


3）假设到代数：假设第一枚鸡蛋扔下去的层数为i，则碎了的情况，须要扔的总次数最糟糕的情况是1 + ( i - 1 )；假设没碎，剩下的两个鸡蛋都在，须要扔的次数一定为1 + 用两枚鸡蛋来解决剩下的100 - i层的次数（这个问题跟原题是一样的。可是层数少了一些）。也就是 假设用f ( 100 )表示100层的最坏情况下的最少次数，那么从第i层扔鸡蛋的最糟糕的试验次数是 1+ Max( i - 1, f ( 100 - i ) )，Max表示这两者之间的最大值，是最最糟糕的情况了。

 而 f ( 100 ) 就是对全部从1到100的全部i里。 1+ Max( i - 1, f ( 100 - i ) )的值最小的那个。

4）迭代公式： f ( 100 ) = Min ( 1 + Max ( i - 1, f (100 - i ) ) ) .   当中Max是针对的 i-1、 f ( 100 - i ) 两者 。 而Min是针对的全部的从1到100的i。


5）初始状态： 假设有一层，从第一层扔下去，无论碎不碎。最糟糕的情况也仅仅须要推断一次。 即 f ( 1 ) = 1。而如题所述，第0层不会碎，则 不用扔也知道，即f(0) = 0。


6）终于结论：题目变成了分析一个迭代公式的值。翻译成了计算机语言，剩下的就能够交给计算机了。

基于数学方程的方法

假设最少尝试次数为x，那么，第一个鸡蛋必须要从第x层扔下，因为：如果碎了，前面还有x - 1层楼可以尝试，如果没碎，后面还有x-1次机会。

如果没碎，第一个鸡蛋，第二次就可以从x +（x - 1）层进行尝试，为什么是加上x - 1，因为，当此时，第一个鸡蛋碎了，第二个鸡蛋还有可以从x+1 到 x + (x - 1) - 1层进行尝试，有x - 2次。如果还没碎，那第一个鸡蛋，第三次从 x + (x - 1) + (x - 2)层尝试。碎或者没碎，都有x - 3次尝试机会，依次类推。那么，x次的最少尝试，可以确定的最高的楼层是多少呢？ x + (x - 1) + (x - 2) + … + 1 = x(x+1) / 2 那反过来问，当最高楼层是100层，最少需要多少次呢？x(x+1)/2 >= 100, 得到x>=14，最少要尝试14次
'''

def dropegg(layer):
    if layer == 0:
        return 0
    if layer ==1:
        return 1
    MIN = layer
    for i in range(1,layer):
        temp = 1 + max(i-1,dropegg(layer-i))
        if MIN > temp :
            MIN =temp
    return MIN


if __name__=='__main__':
    l = 20
    res = dropegg(l)
    print(res)


