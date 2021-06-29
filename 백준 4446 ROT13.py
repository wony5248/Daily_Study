import sys
# input = sys.stdin.readline

mo = ["a", "i", "y", "e", "o", "u", "a", "i", "y"]
ja = ["b", "k", "x", "z", "n", "h", "d", "c", "w", "g", "p", "v", "j", "q", "t", "s", "r", "l", "m", "f", "b", "k", "x", "z", "n", "h", "d", "c", "w", "g"]

while True:
    idx = 0
    string = input().rstrip()
    result = []
    if not string:
        break
    else:
        for j in string:
            if j.lower() in mo:
                idx = mo.index(j.lower()) + 3
                if j.isupper():
                    result.append(mo[idx].upper())
                else:
                    result.append(mo[idx])
            elif j.lower() in ja:
                idx = ja.index(j.lower()) + 10
                if j.isupper():
                    result.append(ja[idx].upper())
                else:
                    result.append(ja[idx])
            else:
                result.append(j)
    print("".join(result))