import sys

input = sys.stdin.readline
X = int(input())
order = list(input().rstrip())
club = []
if order:
    club.append(order.pop(0))
mcount = 0
wcount = 0


def counting():               # 클럽안 남녀 차이 계산해주는 함수
    global mcount
    global wcount
    mcount = 0
    wcount = 0
    for j in range(len(club)):
        if club[j] == "W":
            wcount += 1
        else:
            mcount += 1


while order:                  
    counting()
    if wcount == mcount:               # 남녀 숫자 같으면 맨처음 입장
        club.append(order.pop(0))
    elif mcount < wcount and wcount - mcount < X:          # 여자가 더많고 기억할수있는 차이 이내일때
        club.append(order.pop(0))                          # 처음 사람 입장
    elif mcount < wcount and wcount - mcount >= X:         # 여자가 더 많고 기억할수 있는 최대 차이일떄
        if order[0] == "M":                                # 첫사람 남자면 입장
            club.append(order.pop(0))
        elif len(order) > 1 and order[0] == "W" and order[1] == "M":  # 첫사람 여자인데 다음사람 남자면 다음사람 입장
            club.append(order.pop(1))
        else:                                              # 아닐 경우 종료
            break
            
    elif wcount < mcount and mcount - wcount < X:          # 남자가 더 많을때 위에랑 남여만 반대로
        club.append(order.pop(0))
    elif wcount < mcount and mcount - wcount >= X:
        if order[0] == "W":
            club.append(order.pop(0))
        elif len(order) > 1 and order[0] == "M" and order[1] == "W":
            club.append(order.pop(1))
        else:
            break


print(len(club))

