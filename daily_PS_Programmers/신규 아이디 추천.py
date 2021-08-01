def solution(new_id):
    answer = ''
    oper = ["-", "_", "."]
    new_id = new_id.lower()
    for c in new_id:
        if c.isalpha() or c.isdecimal() or c in oper:
            answer += c
    while '..' in answer:
        answer = answer.replace('..', '.')
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer = 'a'
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    while len(answer) < 3:
        answer += answer[-1]
    return answer