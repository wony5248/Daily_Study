A, B = list(map(int, input().split()))
count = 1
while B != A:
    if B < A or (B % 2 != 0 and B % 10 !=1):      # B가 A보다 작아졌거나 (2로 못나누고 1을 못빼거나) -> B -> A 불가능
        count = -1
        break
    elif B % 2 == 0:    # 2로 나눠질경우
        B //= 2
        count += 1
    elif B % 2 != 0:      # 2로 못나누지만 맨뒤가 1일 경우
        B //= 10
        count += 1

print(count)







