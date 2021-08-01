from itertools import combinations
L, C = map(int, input().split())
string = list(input().split())
result = list(combinations(string, L))

for i in range(len(result)):
    result[i] = set(result[i])
    if len(result[i].difference("a", "e", "i", "o", "u")) < 2 or len(result[i].difference("a", "e", "i", "o", "u")) == L:
        del result[i]
        result.insert(i, [])
    result[i] = list(result[i])

    result[i].sort()
    result[i] = "".join(result[i])
result.sort()
for i in range(len(result)):
    if result[i]:
        print(result[i])
