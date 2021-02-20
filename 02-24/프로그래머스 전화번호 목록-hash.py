N = list(input().split())
# def solution(phone_book):   #  시간 초과 정확성은 통과
#     answer = True
#     count = 0
#     lst = list(map(int, phone_book))
#     lst.sort()
#     phone_book = list(map(str, lst))
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[j].find(phone_book[i]) ==  0:
#                 answer = False
#
#     return answer


def solution(phone_book):
    answer = True
    count = 0
    phone_book.sort()    # 문자 배열 sort 하면 앞자리 같으면 다음자리 큰순 으로 정렬되기에 접두사가 되려면(있다면) 자신 다음 인덱스여야함
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            answer = False

    return answer


print(solution(N))





# s = "119"
# s1 = "119119119119119119"
