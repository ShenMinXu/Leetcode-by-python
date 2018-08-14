#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n,k
    # n,k = int(sys.stdin.readline().strip().split())
    nk = '6 3 '.split()
    n,k =int(nk[0]),int(nk[1])
    #读取评分
    scores = [1,3,5,2,5,4]
    #读取是否清醒
    awake = [1,1,0,1,0,0]
    scores_max = 0
    res = 0
    for i in range(len(awake)):
        if awake[i] == 1:
            res += scores[i]
        else:
            flag = 0
            tmp = 0
            while i + flag < len(scores) and flag <k:
                if awake[i+flag] == 0:
                    tmp += scores[i+flag]
                flag +=1
            scores_max = max(scores_max,tmp)
    print(res+scores_max)




