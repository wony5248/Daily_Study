N = list(input().split())
def solution(phone_book):
    answer = True

    result = ""
    for i in range(len(phone_book)):
        result += phone_book[i]
    for i in  range(len(phone_book)):
        if result.count(phone_book[i]) > 1:
            answer = False
    return result
print(solution(N))
# s = "119"
# s1 = "119119119119119119"
