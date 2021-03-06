import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n = int(sys.stdin.readline().rstrip())       # public2 -> public1 을 만드는 법 찾으면 됨
    public1 = sys.stdin.readline().rstrip().split()
    public2 = sys.stdin.readline().rstrip().split()
    secret = sys.stdin.readline().rstrip().split()

