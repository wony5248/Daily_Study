T = int(input())
for i in range(T):
    string = input()
    result = []
    for j in range(1,10):
        if string[0] == string[j]:
            if string[0:j] == string[j:j+j]:
                result.append(j)
    print("#%d %d" %(i+1, min(result)))

