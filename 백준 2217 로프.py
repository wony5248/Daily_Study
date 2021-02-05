N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
for i in range(N):
    rope[i] = rope[i] * (i+1)
result = max(rope)
print(result)