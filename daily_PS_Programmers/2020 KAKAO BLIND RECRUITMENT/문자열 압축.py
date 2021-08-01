def solution(string):

    answer = 1000
    length = len(string)
    for i in range(1,length//2 +1):

        result = ""
        count = 1

        first = string[:i]

        for j in range(i, length+i, i):
            if first == string[j:j+i]:
                count+=1
            else:
                if count > 1:
                    result = result + str(count)+ first
                else:
                    result = result + first

                first = string[j:j+i]
                count = 1

        answer = min(answer, len(result))

    return min(answer, len(string))