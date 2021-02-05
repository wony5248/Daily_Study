from collections import deque
for t in range(10):
    num = list()
    oper = list()
    TC = int(input())
    cal = input()
    ioper = {"*": 2, "+": 1, "(": 3}
    ooper = {"*": 2, "+": 1, "(": 0}
    for i in range(TC):
        if cal[i].isdecimal():
            num.append(cal[i])
        else:
            if not oper:
                oper.append(cal[i])
            else:
                if cal[i] == ")":
                    while oper[-1] != "(":
                        num.append(oper.pop())
                    oper.pop()
                elif ioper[cal[i]] > ooper[oper[-1]]:
                    oper.append(cal[i])
                else:
                    while ioper[cal[i]] <= ooper[oper[-1]]:
                        num.append(oper.pop())
                    oper.append(cal[i])

    for i in range(len(num)):
        if num[i].isdecimal():
            oper.append(num[i])
        else:
            num1 = int(oper.pop())
            num2 = int(oper.pop())

            if num[i] == "+":
                result = num1 + num2
            elif num[i] == "*":
                result = num1 * num2
            oper.append(str(result))

    print("#%d %s" %(t+1, oper[0]))
