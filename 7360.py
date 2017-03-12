import math

def choose(n, k):
    num = math.factorial(n)
    denom = math.factorial(k)*math.factorial(n-k)
    return num//denom

P = int(input())

for x in range (0, P):
    N = int(input())//2
    sum = 0
    for x in range(0 + N%2, N//3 + 1, 2):
        n = (N + x)//2
        sum += choose(n, x)**2
    if N == 1:
        sum = 1
    print(sum)