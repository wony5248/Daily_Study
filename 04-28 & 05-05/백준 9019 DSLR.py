from collections import deque
import sys
input = sys.stdin.readline
T = int(input())


def bfs(start, end):
    queue = deque()
    queue.append([start, ""])
    while queue:
        x, step = queue.popleft()

        if int(x) == int(end):
            return step
        for d in range(4):
            if d == 0:
                string = str(int(x) * 2 % 10000).zfill(4)                # D 일경우 *2%1000을 넣어주고 step + D
                if visit[int(string)] == 0:
                    queue.append([string, step + "D"])
                    visit[int(string)] = 1
                    # print(d, string)
            elif d == 1:
                if int(x) == 0:
                    string1 = "9999"
                else:
                    string1 = str(int(x) - 1).zfill(4)
                if visit[int(string1)] == 0:
                    visit[int(string1)] = 1
                    queue.append([string1, step + "S"])
                    # print(d, string)
            elif d == 2:
                string2 = x.zfill(4)
                string2 = (string2[1:] + string2[0]).zfill(4)
                if visit[int(string2)] == 0:
                    visit[int(string2)] = 1
                    queue.append([string2, step + "L"])
                    # print(d, string2)
            elif d == 3:
                string3 = x.zfill(4)
                string3 = (string3[-1] + string3[0:-1]).zfill(4)
                if visit[int(string3)] == 0:
                    visit[int(string3)] = 1
                    queue.append([string3, step + "R"])
                    # print(d, string3)
        # print()







for i in range(T):
    visit = [0 for _ in range(10000)]
    A, B = input().rstrip().split()
    print(bfs(A,B))

