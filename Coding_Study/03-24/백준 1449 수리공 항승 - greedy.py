N, L = map(int, input().split())
water = list(map(int, input().split()))
water.sort()
count = 1
tape = L
i = 1
while i < len(water):          
    if water[i] - water[i-1] <= tape - 1:   # 물이새는 파이프끼리의 간격이 테이프보다 작거나 같으면
        tape -= water[i] - water[i-1]       # 테이프 길이 파이프간격만큼 빼주고
        i += 1
    else:               # 아니라면
        tape = L        # 테이프 하나 썻다 하고 다음테이프 씀
        count += 1
        i+=1
print(count)