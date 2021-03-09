
# def solution(phone_book):
#     answer = "YES"
#     count = 0
#     lst = list(map(int, phone_book))
#     lst.sort()
#     phone_book = list(map(str, lst))
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[j].find(phone_book[i]) ==  0:
#                 answer = "NO"
#
#     return answer

import sys


def solution(phone_book):
    global answer
    answer = "YES"
    phone_book.sort()    # 문자 배열 sort 하면 앞자리 같으면 다음자리 큰순 으로 정렬되기에 접두사가 되려면(있다면) 자신 다음 인덱스여야함
    for k in range(len(phone_book) - 1):
        if phone_book[k] in phone_book[k + 1] and phone_book[k][0] == phone_book[k+1][0]:
            answer = "NO"
    # print(phone_book)
    result.append(answer)
    return answer

result = []
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    N = []

    for j in range(n):
        num = sys.stdin.readline().rstrip()
        N.append(num)
    # print(N)
    print(solution(N))






#
#
# s = "119"
# s1 = "119119119119119119"
