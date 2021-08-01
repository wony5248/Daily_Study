lst = [0 for _ in range(1001)]
n = int(input())
lst[1] = 1
lst[2] = 2
for i in range(3, n+1):
   lst[i] = lst[i-1] + lst[i-2]
print(lst[n]%10007)
