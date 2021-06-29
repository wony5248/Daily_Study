import sys
input = sys.stdin.readline
alpha = ["a", "e", "i", "o", "u"]

while True:
    passwd = input().rstrip()
    ismo = 1
    isja = 1
    check = 0
    even = 0
    isflag = 0
    if passwd == "end":
        break
    else:
        for i in range(len(passwd)):
            if passwd[i] in alpha:
                check = 1
        for i in range(1, len(passwd)):
            if ismo >= 3 or isja >= 3:
                isflag = 1
                break
            if passwd[i] == passwd[i-1]:
                if passwd[i-1] == "e" or passwd[i-1] == "o":
                    even = 0
                else:
                    even = 1
            if passwd[i] in alpha and passwd[i-1] in alpha:
                ismo += 1
            elif passwd[i] not in alpha and passwd[i-1] not in alpha:
                isja += 1
            elif passwd[i] in alpha and passwd[i-1] not in alpha:
                ismo = 1
            elif passwd[i] not in alpha and passwd[i-1] in alpha:
                isja = 1
        if ismo >= 3 or isja >= 3:
            isflag = 1

    if isflag == 1 or check == 0 or even == 1:
        print("<%s> is not acceptable." %passwd)

    else:
        print("<%s> is acceptable." % passwd)



    