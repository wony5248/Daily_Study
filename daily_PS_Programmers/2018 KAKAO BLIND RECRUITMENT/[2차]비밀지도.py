def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a12 = str(bin(arr1[i]|arr2[i])[2:])
        a12=a12.zfill(n)
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

#
# def solution(n, arr1, arr2):
#     answer = [["" for _ in range(n)] for _ in range(n)]
#     arr3 = []
#     arr4 = []
#     for i in range(n):
#         arr3.append(list(str(format(arr1[i], 'b')).zfill(n)))
#         arr4.append(list(str(format(arr2[i], 'b')).zfill(n)))
#
#     for i in range(n):
#         for j in range(n):
#             if arr3[i][j] == "1" or arr4[i][j] == "1":
#                 answer[i][j] = "#"
#             elif arr3[i][j] == "0" and arr4[i][j] == "0":
#                 answer[i][j] = " "
#     for i in range(n):
#         answer[i] = "".join(answer[i])
#
#     return answer