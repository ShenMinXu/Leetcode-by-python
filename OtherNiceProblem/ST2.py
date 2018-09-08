n = int(input())
sample_1 = []
sample_0 = []
recall = [0.3,0.4,0.5,0.6,0.7,0.8,0.9]
for i in range(n):
    line = list(map(float,input().strip().split()))
    if line[0] >0:
        sample_1.append((line[1],line[0]))
    else:
        sample_0.append((line[1],line[0]))
sample_1.sort()
sample_0.sort()
for each in recall:
    recall_num = round(len(sample_1)*each)
    score = sample_1[-1*recall_num][0]
    TP = recall_num
    TN = len([1 for sample,sample_score in sample_0 if sample_score >= score])
    res = TP/(TP+TN+1)
    print(res)







