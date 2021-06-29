N, H, W = map(int, input().split())
string = ["" for _ in range(H)]
for i in range(H):
    string[i] = input().rstrip()
origin = ["?" for _ in range(N)]
for i in range(H):
    for j in range(0, N * W, W):
        for k in string[i][j:j+W]:
            if k.isalpha():
                origin[j//W] = k



print("".join(origin))

