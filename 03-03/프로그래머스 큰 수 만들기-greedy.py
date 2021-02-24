# 
#   test 10 시간 초과
# def solution(number, k):
#     number = list(number)
#     count = 0
#     for i in range(k):
#         for j in range(len(number) - 1):
#             if number[j] < number[j + 1]:
#                 del number[j]
#                 count += 1
#                 break
#     if count == 0:
#         for i in range(k):
#             number.pop()
#     answer = "".join(number)
# 
#     return answer


def solution(number, k):
    answer = ''
    return answer