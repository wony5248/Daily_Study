import sys
input = sys.stdin.readline
# dic = dict()
dic = []
N = int(input())

words = [input().rstrip().split() for _ in range(N)]
for word in words:
   print(word[0])
    # if word[0] not in dic:
    #     dic.append(word[0])
print(words)