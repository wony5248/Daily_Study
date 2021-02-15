
TC = int(input())
result = [0 for _ in range(TC)]
lst = []

for i in range(TC):
    count = 0
    lst.append(list(input()))
    for j in range(len(lst[i])):
        if lst[i][j] == "O":   # O이 연속적으로 1개면 1 증가 2개면 2 증가 하게끔 count를 1씩 증가시키면서 result배열의 값엔 count증가
            count += 1
            result[i] += count
        elif lst[i][j] == "X":  # X면 count 0으로 초기화
            count = 0
for i in range(TC):
    print(result[i])
