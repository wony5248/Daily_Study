# T = int(input())
# for i in range(T):
#     tc, num= map(str, input().split())
#     lst = list(map(str, input().split()))
#     for j in range(len(lst)):
#         if lst[j] == "ZRO":
#             lst[j] = 0
#         elif lst[j] == "ONE":
#             lst[j] = 1
#         elif lst[j] == "TWO":
#             lst[j] = 2
#         elif lst[j] == "THR":
#             lst[j] = 3
#         elif lst[j] == "FOR":
#             lst[j] = 4
#         elif lst[j] == "FIV":
#             lst[j] = 5
#         elif lst[j] == "SIX":
#             lst[j] = 6
#         elif lst[j] == "SVN":
#             lst[j] = 7
#         elif lst[j] == "EGT":
#             lst[j] = 8
#         elif lst[j] == "NIN":
#             lst[j] = 9
#     lst.sort()
#     for j in range(len(lst)):
#         if lst[j] == 0:
#             lst[j] = "ZRO"
#         elif lst[j] == 1:
#             lst[j] = "ONE"
#         elif lst[j] == 2:
#             lst[j] = "TWO"
#         elif lst[j] == 3:
#             lst[j] = "THR"
#         elif lst[j] == 4:
#             lst[j] = "FOR"
#         elif lst[j] == 5:
#             lst[j] = "FIV"
#         elif lst[j] == 6:
#             lst[j] = "SIX"
#         elif lst[j] == 7:
#             lst[j] = "SVN"
#         elif lst[j] == 8:
#             lst[j] = "EGT"
#         elif lst[j] == 9:
#             lst[j] = "NIN"
#     print("#%d" %(i+1) )
#     for j in lst:
#         print(j, end= " ")
#     print()


K = int(input())
for _ in range(1, K + 1):
    tc, N = input().split()


    Dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0, "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0}
    num_list = list(input().split())
    for num in num_list:
        Dict[num] += 1

    print("%s" %tc)
    for key in Dict.keys():
        for i in range(Dict[key]):
            print(key, end=" ")
    print()