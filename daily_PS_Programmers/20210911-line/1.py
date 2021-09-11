a = ["abaaaa", "aaa", "abaaaaaa", "fzfffffffa"]
b = 2
c = 2
def solution(research, n, k):
    answer = ''
    lst = []
    for i in range(0, len(research)-n+1, 1):
        for j in range(97, 123, 1):
            isissue = 0 
            cnt = 0
            for l in range(i, i+n):
                if research[l].count(chr(j)) >= k:
                    cnt += research[l].count(chr(j))
                else:
                    isissue = 1
            print(chr(j))
            print(cnt)
            print(isissue)
            if isissue == 0:
                if cnt >= 2 * n * k:
                    lst.append([chr(j), cnt])
    # lst.sort(key=lambda x:(x[1],x[0]))
    return answer

print(solution(a, b, c))