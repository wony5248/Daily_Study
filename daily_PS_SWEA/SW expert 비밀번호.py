for i in range(10):
    num, lst = list(input().split())
    stack = list()
    result = list()
    for k in range(len(lst)):
        stack.append(lst[k])
    num = int(num)
    while True:
        count = 0
        for j in range(len(stack)-1):
            if stack[j] == stack[j+1]:
                del stack[j]
                del stack[j]
                stack.append("O")
                stack.append("X")
                count = 1
                break
        if count == 0:
            break
    for l in stack:
        if l != "O" and l != "X":
            result.append(l)

    print("#%d %s" %(i+1, "".join(result)))
#
# for test_case in range(1):
#     stack = []
#     n, nums = input().split()
#     nums = list(nums)
#     for num in nums:
#         if not stack:
#             stack.append(num)
#         else:
#             if stack[-1] == num:
#                 stack.pop()
#             else:
#                 stack.append(num)
#
#     print('#' + str(test_case), ''.join(stack))