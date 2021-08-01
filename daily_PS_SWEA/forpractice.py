# for i in range(3,11):
#     print(i, end=" ")
# print("")
# for i in range(10,2,-1):
#     print(i, end=" ")
# print("")
# for i in range(2, 18, 2):
#     print(i, end=" ")
# print("")
# for i in range(15,0,-3):
#     print(i, end=" " )
#
#
# arr = [4, 2, 5, 1, 6, 3, 4]
# j=0
# for i in range(len(arr)):
#     print(arr[i], end=" ")
# print("")
# for i in arr:
#     print(i, end =" ")
# print("")
#
# arr.reverse()
# print(arr, end=" ")
# print("")
# arr.reverse()
# while j < 7:
#     print(arr[j], end=" ")
#     j += 1

arr = [4, 2, 5, 1, 6, 3, 4]
for i in arr:
    if i % 2 == 0:
        print(i, end="")
print("")
arr.reverse()
for i in arr:
    if i % 2 != 0:
        print(i, end="")
print("")
arr.reverse()
for i in arr:
    if 4 <= i <= 6:
        print(i, end="")