N = int(input())
lst = [["A","B","C","D","E"],
       ["B","B","B","C","C"],
       ["C","C","C","B","B"],
       ["C","C","C","B","B"],
       ["B","B","B","C","C"]]

for i in range(N):
    str = input()
    count = 0
    for j in range(3):
        for k in range(3):
            if lst[j][k]== str[0]:
                if lst[j][k+1] == str[1] or lst[j+1][k] == str[1] or lst[j+1][k+1] == str[1]:
                    if lst[j][k+2] == str[2]:
                        count+=1
                    if lst[j+2][k] == str[2]:
                        count+=1
                    if lst[j + 2][k + 2] == str[2]:
                        count+=1
    print("%s %d" %(str, count))
