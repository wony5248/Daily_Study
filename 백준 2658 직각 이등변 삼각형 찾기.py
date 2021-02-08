lst = [[0 for _ in range(11)] for _ in range(11)]
for i in range(10):
    lst[i] = list(map(int, input()))
# for i in range(10):
#     for j in range(10):
slist = sorted(lst)
print(max(lst).index(1)+1)
print(10-max(slist).index(1))
print(lst)