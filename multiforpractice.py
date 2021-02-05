# for i in range(12):
#     for j in range(60):
#         print("%d시 %d분" % (i, j))

# a =[]
# for i in range(5):
#     a.append([i, i, i, i, i])
#
# print(a)

# arr = [4, 2, 5, 1, 6, 3, 4]
#
# for i in range(3):
#     for j in arr:
#         print(j, end=" ")
#     print("")
# for i in range(3):
#     print(arr)
# arr.reverse()
# for i in range(3):
#     for j in arr:
#         print(j, end=" ")
#     print("")

# a = []
# for i in range(5):
#     a.append([0] * 5)
#
# n=1
# for i in range(0, 5):
#     for j in range(0, 5):
#         a[i][j] = n
#         n += 1
#
# print(a)
#
# k=25
# for i in range(0, 5):
#     for j in range(0, 5):
#         a[i][j] = k
#         k -= 1
# print(a)

# a = [i for i in range(10)]
# print(a)
# a = [i+2 for i in range(10)]
# print(a)
# a = [i**2 for i in range(10)]
# print(a)

a = [i for i in range(10) if i%2 ==0]

print(a)