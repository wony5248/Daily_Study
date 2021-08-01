def solution(files):
    answer = []
    result = [[] for _ in range(len(files))]
    nidx = 0
    tidx = 0
    for i in range(len(files)):
        for j in range(1, len(files[i])):
            if files[i][j].isdecimal() and not files[i][j - 1].isdecimal():
                result[i].append(files[i][:j])
                nidx = j
                if j == len(files[i]) - 1:
                    result[i].append(files[i][j])
            elif not files[i][j].isdecimal() and files[i][j - 1].isdecimal():
                result[i].append(files[i][nidx:j])
                tidx = j
                result[i].append(files[i][tidx:])
                break
            elif files[i][j].isdecimal() and j == len(files[i]) - 1:
                result[i].append(files[i][nidx:j + 1])
    result.sort(key=lambda x: (x[0].lower(), int(x[1])))
    for i in range(len(result)):
        answer.append("".join(result[i]))

    return answer