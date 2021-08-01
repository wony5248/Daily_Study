B = int(input())
Y = int(input())
def solution(brown, yellow):      
    answer = []
    all = brown + yellow
    for y in range(3, all):       # brown이 최소 2줄이고 yello가 한줄 있어야 하므로 최소 3 * 3 이상
        if all % y == 0:          # x * y는 전체 카펫 수   => y로 나누어 떨어질때
            x = all // y          
            if (x - 2) * (y - 2) == yellow:   # x * y  = 전체 카펫 수고 (x-2) * (y-2) = 노랑 카펫수
                answer = [max(x, y), min(x, y)]    # x, y 구하고  큰걸 가로에 작은걸 세로에

    return answer

print(solution(B, Y))