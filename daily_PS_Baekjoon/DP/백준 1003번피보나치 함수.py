def fibonacci(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
N = int(input())


print(fibonacci(N))

# N = int(input())
# arr = [0 for i in range(N+1)]
# for j in range(N+1):
#     if N == 0:
#         arr[0] = 0
#     elif N ==1:
#         arr[1] = 1
#     else:
#         arr[0] = 0
#         arr[1] = 1
#         arr[j] = arr[j-1] + arr[j-2]
# print(arr[N])