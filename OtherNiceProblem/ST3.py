import numpy as np

n = int(input())
sample = []
for i in range(n):
    line = input().strip().split()
    sample.append(line)


def weightsUpdate(data, w, b, learning_rate=0.01):
    for x0, y0 in data:
        y = w*x0 + b
        w_gradient = (y - y0) * x0
        b_gradient = (y - y0)[0];
        w -= w_gradient * learning_rate
        b -= b_gradient
        loss = 0.5 * np.square(y - y0)
    return [w, b, loss[0][0]]


def linearRegressionTrain(data):
    w0 = np.random.randn(1, 1)
    b0 = np.random.randn(1)
    for i in range(1000):
        w0, b0, loss = weightsUpdate(data, w0, b0, 0.01)
        if (i % 100 == 0):
            print(loss)

    return [w0, b0]




data = sample
w0 = 1
b0 = 1
for i in range(100):
    w0, b0, loss = weightsUpdate(data, w0, b0, 0.01)
    if (i % 100 == 0):
        print(loss)
