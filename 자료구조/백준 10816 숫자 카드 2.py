import sys
input = sys.stdin.readline
N = int(input())
num_card = list(map(int, input().split()))
M = int(input())
have_card = list(map(int, input().split()))
cnt_card = dict()
for i in have_card:
    cnt_card[i] = 0
for i in num_card:
    if i in cnt_card.keys():
        cnt_card[i] += 1
for j in have_card:
    print(cnt_card[j], end=" ")
