T = int(input())
for tc in range(T):
    exp = list(input())
    stack = ["("]                # 처음은 무조껀 "(" 로 시작         
    count = 0
    for i in range(1, len(exp)):     # i-1 번째 탐색위해 1부터
        if exp[i] == "(":             #"("는 stack에 넣어줌
            stack.append(exp[i])
        elif exp[i] == ")" and exp[i-1] == "(":     # i-1 이 "("면 레이져 => stack에 있는 막대기 수만큼 조각 증가
            stack.pop()
            count += len(stack)
        elif exp[i] == ")" and exp[i-1] != "(":     # 레이저가 아니면 막대기의 끝 1개의 조각 추가
            stack.pop()
            count += 1




    print("#%d %d" %(tc + 1, count))