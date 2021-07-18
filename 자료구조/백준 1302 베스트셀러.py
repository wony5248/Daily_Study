import sys
input = sys.stdin.readline
books = dict()
N = int(input())
for i in range(N):
    book = input().rstrip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

sbooks = list(sorted(books.items()))
sbooks.sort(key = lambda x: (-x[1], x[0]))
print(sbooks[0][0])