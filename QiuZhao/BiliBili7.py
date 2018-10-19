#5 2
#1 3 4 5 9

import heapq
line = list(map(int,input().strip().split()))
n = line[0]
k = line[1]
ability = sorted(list(map(int,input().strip().split())))


class TopKHeap(object):
    def __init__(self, k):
        self.k = k
        self.data = []

    def push(self, elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)
        else:
            topk_small = self.data[0]
            if elem > topk_small:
                heapq.heapreplace(self.data, elem)
    def topk(self,p):
        return self.data[-p]

th = TopKHeap(n)
for i in range(5):
    for j in range(i+1,5):
        th.push(ability[i]*ability[j])
print(th.topk(k))
