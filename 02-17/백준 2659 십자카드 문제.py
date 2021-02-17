from collections import deque
num = list(map(int, input().split()))
lst1 = list() # 모든 십자수 추출하기 위해 이용하는 배열 (queue 로 활용)
result = list()  # 모든 십자수 저장하는 배열
min = 9999

for j in range(1, 10):                       # 1111 부터 9999까지 입력받으면서 각 숫자의 십자수 뽑아내서 result에 저장
    for k in range(1, 10):
        for l in range(1, 10):
            for m in range(1, 10):
                lst1 = list()
                lst1.append(j)
                lst1.append(k)
                lst1.append(l)
                lst1.append(m)
                min2 = 9999
                for n in range(4):
                    ten2 = lst1[0] * 1000 + lst1[1] * 100 + lst1[2] * 10 + lst1[3]
                    if min2 > ten2:
                        min2 = ten2
                    y = lst1.pop(0)
                    lst1.append(y)
                result.append(min2)
for i in range(4):
    ten = num[0] * 1000 + num[1] * 100 + num[2] * 10 + num[3]  # 입력받은 4개 숫자로 4자리 숫자 만들기
    if min > ten:  # min을 최댓값인 9999로 놓고 이것 보다 작을 시 min을 4자리 숫자로 변환하여 십자수 추출
        min = ten  # for문 이 끝났을시 min에는 입력받은 4자리 숫자의 십자수가 저장
    x = num.pop(0)
    num.append(x)

result.sort()
count = 1
for i in range(1, len(result)):   # 모든십자수가 들어있는 result 배열을 돌면서
    if min == 1111:   # 1111은 0번째 인덱스라 따로 예외처리
        print(1)
        break
    if result[i] == result[i-1]:   # 십자수 리스트에서 중복처리를 하기 위해 전 인덱스의 값과 비교하여 같으면 continue
        continue
    else:                         # 전 인덱스와 다를시 카운트 1 증가
        count += 1
        if result[i] == min:      # 입력받은 십자수와 같을시 count 출력
            print(count)
            break

