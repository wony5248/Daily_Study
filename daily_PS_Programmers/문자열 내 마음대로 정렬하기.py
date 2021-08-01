def solution(strings, n):
    answer = []
    answer = list(sorted(strings,key = lambda x : (x[n], x)))
    return answer