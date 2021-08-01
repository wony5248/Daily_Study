T = int(input())
A,B,C =0,0, 0
isflag = 0
while T:
    if T >= 300:
        A += T // 300
        T -= 300 * (T // 300)
    elif T >= 60:
        B += T // 60
        T -= 60 * (T // 60)

    elif T < 60 and T % 10 == 0:
        T -= 10
        C += 1
    else:
        isflag = 1
        break
if isflag == 0:
    print(A, B, C)
else:
    print(-1)

#
# T = int(input())
# A,B,C =0,0, 0
# isflag = 0
# while T:
#     if T >= 300:
#         T -= 300
#         A += 1
#     elif T >= 60:
#         T -= 60
#         B += 1
#     elif T < 60 and T % 10 == 0:
#         T -= 10
#         C += 1
#     else:
#         isflag = 1
#         break
# if isflag == 0:
#     print(A, B, C)
# else:
#     print(-1)