def solution(operations):
    lst = []
    for oper in operations:
        if oper[0] == "I":
            lst.append(int(oper[2:]))
        elif oper[0] == "D" and lst:
            if oper[2] == "-":
                lst.pop(lst.index(min(lst)))
            elif oper[2] != "-":
                lst.pop(lst.index(max(lst)))
        elif oper[0] == "D" and not lst:
            continue
    answer = [0, 0]
    if lst:
        answer[0] = max(lst)
        answer[1] = min(lst)

    return answer