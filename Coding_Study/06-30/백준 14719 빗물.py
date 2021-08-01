H, W = map(int, input().split())
block = list(map(int, input().split()))
i = 0
result = 0
for i in range(len(block)):
    leftV = max(block[:i+1])
    rightV = max(block[i:])
    minV = min(leftV, rightV)
    result += abs(minV - block[i])

print(result)