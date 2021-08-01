N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


# for i in B:   # set 이용 하는게 속도 빠름
#     if i in A:
#         print(1)
#     else:
#         print(0)



A.sort()
for i in B:          # 이분 탐색
    low = 0
    high = N - 1
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if A[mid] == i:          # B배열의 숫자가 A배열의 중간값과 비교후
            result = 1
            break
        elif A[mid] < i:         # 찾고자 하는 숫자가 중간값보다 클 경우
            low =mid + 1         # 그 지점 + 1과 마지막 부분의 중간을 탐색
        else:                    # 중간값보다 작을경우
            high = mid -1        # 그지점 -1 과 작은 값의 중간을 탐색
    print(result)


