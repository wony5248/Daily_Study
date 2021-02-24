from itertools import permutations
N = input()

lst = list(N)   # 입력받은 숫자 하나씩 따로 저장


def solution(numbers):
    global prime
    prime = []
    result = []
    for i in range(1, len(numbers)+1):
        numlst = permutations(numbers, i)      # 0 ~ numbers 자릿 수만큼 해당 자릿수의 모든 조합의 숫자 추출
        for k in numlst:                       # permutations 는 쌍으로 나오기에 하나의 숫자로 만들어줌 -. join이용
            allnum = "".join(k)
            result.append(int(allnum))         # result 에는 모든 조합의 수 가 들어감
    result = set(result)                       # 중복 제거하기 위해 set으로 해주고 다시 list로 변환
    result = list(result)

    for i in result:                           
        isprime = 1                            # result에서 해당 수가 소수인지 아닌지 판단하는 조건
        for j in range(2, i):
            if i % j == 0:                     # 1을 제외하고 나눠지는 숫자가 있다면 이 수는 소수가 아니다.
                isprime = 0
                break
        if isprime == 1 and i > 1:             # isprime = 1 이면 소수  and 1은 조건 만족하지만 소수가 아님
            prime.append(i)                    # 소수들만 넣는 배열
    answer = len(prime)                        # 해당 배열 길이 출력
    return answer




print(solution(lst))
print(prime)