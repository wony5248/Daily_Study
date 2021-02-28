

n, t = map(int, input().split())
time = []
score = []
dp = [[0 for _ in range(t+1)] for _ in range(n+1)]
for i in range(n):
    k, s = map(int, input().split())
    time.append(k)
    score.append(s)


