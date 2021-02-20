N = list(map(int, input().split()))


def solution(numbers):
    answer = ''
    string = list(map(str, numbers))
    string.sort(key=lambda x: x * 3, reverse=True)    ## 문자열로 sort하면 자릿수 상관없이 맨앞숫자 큰순으로 정렬 => 문자열로 합칠때 최대 되는 순서
    for i in range(len(string)):                      ## *3 안하면 9 랑 97 들어왔을때 97이 더 크다고 인식  9랑 99랑 999랑 같게끔 해줘야 함
        answer += string[i]
    result = int(answer)
    answer = str(result)
    return answer


print(solution(N))