N, K = map(int, input().split())
bottle = [1 for _ in range(N)]

result = []
cnt = N             # 처음 물병의 갯수
while True:         # N개 물병부터 병 1개씩 추가하면서 조건 만족할때 까지 탐색
    count = 0      
    tmp = cnt
    while tmp !=0:
        div = tmp // 2    # 둘로 합쳐지는 병들
        mod = tmp % 2     # 둘로 못합치고 남는 병
        count += mod      # 합칠때마다 남는 병 더해줌
        tmp = div
    if count <= K:          # 남은 병 총합이 K보다 작거나 같다면 => 다 합쳤을때 남는 병수가 K보다 작다면
        print(cnt-N)
        break
    cnt += 1           # 물병 갯수+1



