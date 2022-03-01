import sys
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
result = 0
words.sort(key= lambda x : len(x))

for i in range(len(words)):
    isflag = 0
    for j in range(i+1, len(words)):
        if words[i] == words[j][:len(words[i])]:
            isflag = 1
            break
        else:
            continue
    else:
        result += 1

print(result)