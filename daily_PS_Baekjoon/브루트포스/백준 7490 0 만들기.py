import sys
import copy


def operator(list, n):
    if len(list) == n:
        operator_list.append(copy.deepcopy(list))
        return
    list.append(' ')
    operator(list, n)
    list.pop()

    list.append('+')
    operator(list, n)
    list.pop()

    list.append('-')
    operator(list, n)
    list.pop()


test = int(sys.stdin.readline())

for _ in range(test):
    operator_list = []
    n = int(sys.stdin.readline())
    operator([], n - 1)

    nums = [i for i in range(1, n + 1)]

    for operators in operator_list:
        string = ''
        for i in range(n - 1):
            string += str(nums[i]) + operators[i]
        string += str(nums[-1])
        if eval(string.replace(' ', '')) == 0:
            print(string)
    print()