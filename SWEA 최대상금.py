s = input


def dfs(start, cur, end, count):
    global result
    global cards
    if cur == count:
        tmp = int("".join(cards))
        if tmp > result:
            result = tmp
        return
    for i in range(start, end):
        for j in range(i + 1, end):
            if cards[i] <= cards[j]:
                cards[i], cards[j] = cards[j], cards[i]
                dfs(i, cur + 1, end, count)
                cards[i], cards[j] = cards[j], cards[i]


def solution(card, count):
    global cards
    cards = list(card)[:]
    length = len(cards)

    if length == 2:
        for _ in range(count % 2):
            cards[-1], cards[-2] = cards[-2], cards[-1]
        return int("".join(cards))

    global result
    result = 0
    dfs(0, 0, length, count)

    if result == 0:
        for _ in range(count % 2):
            cards[-1], cards[-2] = cards[-2], cards[-1]
        result = int("".join(cards))

    return result


if __name__ == "__main__":
    T = int(s()) + 1
    for t in range(1, T):
        N, M = s().split()
        print("#%d %d" % (t, solution(N, int(M))))