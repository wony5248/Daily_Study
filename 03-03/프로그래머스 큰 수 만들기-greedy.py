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
    stack = []
    count = 0
    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
        else:
            while stack:
                if count == k or number[i] <= stack[-1]:
                    break
                if number[i] > stack[-1]:
                    stack.pop()
                    count += 1
            stack.append(number[i])
    while count != k:
        stack.pop()
        count += 1
    answer = "".join(stack)

    return answer

